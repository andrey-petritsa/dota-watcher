class NotifyAboutDotaMatchCommand:
    def __init__(self):
        self.event_watcher = None
        self.chat = None
        self.last_event_id_provider = None

    def execute(self, player_id):
        events = self.event_watcher.get_events(player_id)
        new_events = self.__get_new_events(events)[:4]
        if not new_events:
            return

        for event in new_events:
            self.chat.send_event(event)

        self.last_event_id_provider.set(new_events[0]['id'])

    def __get_new_events(self, events):
        last_event_id = self.last_event_id_provider.get()
        if last_event_id is None:
            return events

        for i, event in enumerate(events):
            if event['id'] == last_event_id:
                return events[:i]

        return events

