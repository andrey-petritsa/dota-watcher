import os

from dotenv import load_dotenv

from details.app_facotry import AppFactory


class TestNotifyAboutDotaMatchCommand:
    def setup_method(self):
        self.test_filename = "last_event_id.txt"
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def test_execute(self):
        load_dotenv()
        cmd = AppFactory.create_notify_about_dota_match_command()
        cmd.execute('250798893')

        assert len(AppFactory.telegram_chat.responses) != 0

        AppFactory.telegram_chat.responses = []
        cmd.execute('250798893')
        assert len(AppFactory.telegram_chat.responses) == 0