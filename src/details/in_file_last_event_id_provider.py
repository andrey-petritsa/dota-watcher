import os

class InFileLastEventIdProvider:
    def __init__(self, filename="last_event_id.txt"):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as f:
                f.write("")

    def get(self):
        try:
            with open(self.filename, 'r') as f:
                content = f.read().strip()
                if content == "":
                    return None
                return content
        except (ValueError, FileNotFoundError):
            return None

    def set(self, last_event_id):
        with open(self.filename, 'w') as f:
            f.write(str(last_event_id))
