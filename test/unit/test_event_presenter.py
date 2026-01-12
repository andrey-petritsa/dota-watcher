from details.ui.event_presenter import EventPresenter

class TestEventPresenter:
    def test_present_for_yana_loss(self):
        event = {
            'player_id': '1',
            'date': 1768175700,
            'duration': 1502,
            'hero': 'Jakiro',
            'is_win': False,
            'kda': '1/5/5'
        }
        expected = "Проигранный матч яна! Герой: Jakiro, Продолжительность: 25 минут. KDA: 1/5/5"
        actual = EventPresenter.present(event)
        assert actual == expected

    def test_present_for_yana_win(self):
        event = {
            'player_id': '1',
            'date': 1768175700,
            'duration': 1800,
            'hero': 'Invoker',
            'is_win': True,
            'kda': '10/2/15'
        }
        expected = "Выигранный матч яна! Герой: Invoker, Продолжительность: 30 минут. KDA: 10/2/15"
        actual = EventPresenter.present(event)
        assert actual == expected

    def test_present_unknown_player(self):
        event = {
            'player_id': '999',
            'date': 1768175700,
            'duration': 1200,
            'hero': 'Pudge',
            'is_win': False,
            'kda': '2/10/3'
        }
        expected = "Проигранный матч неизвестный игрок! Герой: Pudge, Продолжительность: 20 минут. KDA: 2/10/3"
        actual = EventPresenter.present(event)
        assert actual == expected
