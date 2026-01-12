import os
from dotenv import load_dotenv

from details.chat.telegram_chat import TelegramChat


class TestTelegramChat:
    def setup_method(self):
        load_dotenv()

    def test_send_message(self):
        bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
        chat = TelegramChat(bot_token)
        result = chat.send_message('привет')
        assert result['ok'] is True
