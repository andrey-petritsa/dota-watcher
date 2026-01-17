import os

from core.notify_about_dota_match_command import NotifyAboutDotaMatchCommand
from details.dotabuff.dotabuff_watcher import DotabuffWatcher
from details.chat.event_chat import EventChat
from details.in_file_last_event_id_provider import InFileLastEventIdProvider
from details.chat.telegram_chat import TelegramChat

class AppFactory:
    @classmethod
    def create_notify_about_dota_match_command(cls):
        cmd = NotifyAboutDotaMatchCommand()
        bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
        chat_id = os.getenv('TELEGRAM_CHAT_ID')
        cls.telegram_chat = TelegramChat(bot_token, chat_id)
        cmd.chat = EventChat(cls.telegram_chat)
        cmd.event_watcher = DotabuffWatcher()
        cmd.last_event_id_provider = InFileLastEventIdProvider()

        return cmd
