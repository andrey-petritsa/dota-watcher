class SpyEventWatcher:
    def __init__(self):
        self.events = []

    def get_events(self, player_id):
        return self.events