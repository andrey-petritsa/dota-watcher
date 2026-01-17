import logging
import time
from playwright.sync_api import sync_playwright

class DotabuffHtmlFetcher:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.playwright = None
        self.browser = None
        self.context = None
        self._init_browser()

    def _init_browser(self):
        try:
            self.playwright = sync_playwright().start()
            self.browser = self.playwright.chromium.launch(
                headless=True,
                args=[
                    '--no-sandbox',
                    '--disable-setuid-sandbox',
                    '--disable-dev-shm-usage',
                    '--disable-gpu',
                    '--disable-software-rasterizer'
                ]
            )
            ua = (
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/133.0.0.0 Safari/537.36'
            )
            self.context = self.browser.new_context(
                user_agent=ua,
                viewport={'width': 1920, 'height': 1080}
            )
            self.context.set_default_timeout(15000)
            self.context.set_default_navigation_timeout(30000)
            self.logger.info("Браузер и контекст инициализированы")
        except Exception as e:
            self.logger.error(f"Ошибка при инициализации браузера: {e}")
            raise

    def fetch(self, player_id):
        url = f"https://ru.dotabuff.com/players/{player_id}/matches"
        
        max_attempts = 20  # Уменьшаем количество попыток
        retry_delay = 2   # Уменьшаем задержку
        
        for attempt in range(1, max_attempts + 1):
            try:
                self.logger.info(f"Попытка {attempt} из {max_attempts}: запрос к {url}")
                html_content = self._fetch_with_existing_context(url)
                self.logger.info(f"Успешно получен HTML (попытка {attempt})")
                return html_content
            except Exception as e:
                self.logger.warning(f"Попытка {attempt} не удалась: {e}")
                if attempt < max_attempts:
                    self.logger.info(f"Ожидание {retry_delay} секунд перед следующей попыткой...")
                    time.sleep(retry_delay)
                else:
                    self.logger.error(f"Все {max_attempts} попыток завершились ошибкой")
                    raise

    def _fetch_with_existing_context(self, url):
        if not self.context:
            raise RuntimeError("Контекст браузера не инициализирован")
        
        page = self.context.new_page()
        try:
            page.set_default_navigation_timeout(20000)
            page.set_default_timeout(15000)
            page.goto(url, wait_until='domcontentloaded')
            page.wait_for_timeout(500)
            html = page.content()
            return html
        finally:
            page.close()
