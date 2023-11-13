

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        players = self.reader.get_players()

        filtered = list(filter(lambda p : p.nationality == nationality, players))
        filtered.sort(key=lambda p : p.points, reverse=True)

        return filtered
    