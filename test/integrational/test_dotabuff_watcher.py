from details.dotabuff.dotabuff_watcher import DotabuffWatcher


class TestDotabuffWatcher:
    def test_get_events(self):
        watcher = DotabuffWatcher()
        events = watcher.get_events(player_id=250798893)
        assert len(events) != 0
        required_fields = ['is_win', 'hero', 'duration', 'kda', 'date', 'player_id', 'id']
        for event in events:
            assert list(event.keys()) == required_fields