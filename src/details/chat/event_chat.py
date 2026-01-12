from details.ui.event_presenter import EventPresenter


class EventChat:
    def __init__(self, chat):
        self.chat = chat

    def send_event(self, event):
        message = EventPresenter.present(event)
        self.chat.send_message(message)
