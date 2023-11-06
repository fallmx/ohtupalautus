import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(
            PlayerReaderStub()
        )
    
    def test_search_found(self):
        self.assertEqual(str(self.stats.search("Kurri")), "Kurri EDM 37 + 53 = 90")

    def test_search_not_found(self):
        self.assertEqual(self.stats.search("Jorma"), None)

    def test_filter_team(self):
        self.assertEqual(str(list(map(lambda player: str(player), self.stats.team("EDM")))), "['Semenko EDM 4 + 12 = 16', 'Kurri EDM 37 + 53 = 90', 'Gretzky EDM 35 + 89 = 124']")

    def test_sort(self):
        self.assertEqual(self.stats.top(1)[0].name, "Gretzky")
