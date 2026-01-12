from core.notify_about_dota_match_command import NotifyAboutDotaMatchCommand
from mocs.in_memory_last_event_id_provider import InMemoryLastEventIdProvider
from mocs.spy_chat import SpyChat
from mocs.spy_event_watcher import SpyEventWatcher


class TestNotifyAboutDotaMatchCommand:
    def test_execute(self):
        cmd = NotifyAboutDotaMatchCommand()
        cmd.chat = SpyChat()
        cmd.event_watcher = SpyEventWatcher()
        cmd.last_event_id_provider = InMemoryLastEventIdProvider()

        cmd.last_event_id_provider.set('1')
        cmd.event_watcher.events = [
            {'id':'3', 'player_id':'100200', 'date':1768175700, 'duration':1502, 'hero':'Jakiro', 'is_win':False, 'kda':'1/5/5'},
            {'id':'2', 'player_id':'100200', 'date':1768175701, 'duration':1600, 'hero':'Pudge', 'is_win':True, 'kda':'10/2/15'},
            {'id':'1', 'player_id':'100200', 'date':1768175702, 'duration':1400, 'hero':'Invoker', 'is_win':False, 'kda':'5/6/7'}
        ]

        cmd.execute(player_id=100200)

        assert len(cmd.chat.sent_events) == 2
