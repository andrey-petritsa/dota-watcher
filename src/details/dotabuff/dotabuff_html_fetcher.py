import logging
import cloudscraper
import time

class DotabuffHtmlFetcher:
    def __init__(self, ):
        self.logger = logging.getLogger(__name__)

    def fetch(self, player_id):
        self.base_url = f"https://ru.dotabuff.com/players/{player_id}/matches"

        max_attempts = 5
        retry_delay = 5
        scraper = cloudscraper.create_scraper()
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        }

        for attempt in range(1, max_attempts + 1):
            try:
                self.logger.info(f"Попытка {attempt} из {max_attempts}: запрос к {self.base_url}")
                response = scraper.get(self.base_url, headers=headers)
                response.raise_for_status()
                self.logger.info(f"Успешно получен HTML (попытка {attempt})")
                return response.text
            except Exception as e:
                self.logger.warning(f"Попытка {attempt} не удалась: {e}")
                if attempt < max_attempts:
                    self.logger.info(f"Ожидание {retry_delay} секунд перед следующей попыткой...")
                    time.sleep(retry_delay)
                else:
                    self.logger.error(f"Все {max_attempts} попыток завершились ошибкой")
                    raise
