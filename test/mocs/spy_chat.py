class SpyChat:
    def __init__(self):
        self.sent_events = []

    def send_event(self, event):
        self.sent_events.append(event)
