class PlayerStats:
    def __init__(self,reader):
        self.reader = reader
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        nationality_players = []

        for player in self.players:
            if player.nationality == nationality:
                nationality_players.append(player)

        nationality_players.sort(
            key=lambda player: player.goals + player.assists,
            reverse=True
        )

        return nationality_players