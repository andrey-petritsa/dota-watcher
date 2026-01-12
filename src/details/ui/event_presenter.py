from details.players import players


class EventPresenter:
    @classmethod
    def present(cls, event):
        player_id = str(event["player_id"])
        if player_id in players:
            player_name = players[player_id]
        else:
            player_name = "неизвестный игрок"
        duration_min = round(event["duration"] / 60)
        if event["is_win"]:
            result_text = f"Выигранный матч {player_name}!"
        else:
            result_text = f"Проигранный матч {player_name}!"

        return f"{result_text} Герой: {event['hero']}, Продолжительность: {duration_min} минут. KDA: {event['kda']}"
