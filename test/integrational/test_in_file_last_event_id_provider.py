import os

from details.in_file_last_event_id_provider import InFileLastEventIdProvider


class TestInFileLastEventIdProvider:
    def setup_method(self):
        self.test_filename = "last_event_id.txt"
        self.provider = InFileLastEventIdProvider(self.test_filename)
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def test_get_set(self):
        assert self.provider.get() is None
        self.provider.set(123)
        assert self.provider.get() == 123
