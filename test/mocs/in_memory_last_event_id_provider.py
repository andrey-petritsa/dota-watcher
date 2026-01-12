class InMemoryLastEventIdProvider:
    def __init__(self):
        self.last_event_id = None

    def get(self):
        return self.last_event_id

    def set(self, last_event_id):
        self.last_event_id = last_event_id