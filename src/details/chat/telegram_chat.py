import requests
import logging
import time

class TelegramChat:
    def __init__(self, bot_token, chat_id):
        self.logger = logging.getLogger(__name__)

        self.chat_id = chat_id
        self.base_url = f"https://api.telegram.org/bot{bot_token}"
        self.responses = []
        self.max_retries = 3
        self.retry_delay = 1

    def send_message(self, message):
        last_exception = None
        for attempt in range(1, self.max_retries + 1):
            try:
                self.logger.info(f"Попытка {attempt} отправить сообщение в Telegram")
                result = self.__send_message_to_tg_chat(message)
                self.logger.info(f"Сообщение успешно отправлено (попытка {attempt})")
                return result
            except requests.exceptions.RequestException as e:
                last_exception = e
                self.logger.warning(f"Ошибка при отправке сообщения (попытка {attempt}): {e}")
                if attempt < self.max_retries:
                    self.logger.info(f"Повтор через {self.retry_delay} секунд...")
                    time.sleep(self.retry_delay)
                else:
                    self.logger.error(f"Все {self.max_retries} попытки завершились ошибкой")
        raise last_exception


    def __send_message_to_tg_chat(self, message):
        url = f"{self.base_url}/sendMessage"
        data = {
            "chat_id": self.chat_id,
            "text": message,
            "parse_mode": "HTML"
        }
        response = requests.post(url, data=data)
        response.raise_for_status()
        self.responses.append(response)
        return response.json()

