import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def setUp(self):

        self.stats = StatisticsService(

            PlayerReaderStub()

        )

    def test_search_finds_player(self):
        player = self.stats.search("Gretzky")

        self.assertEqual(player.name, "Gretzky")

    def test_search_does_not_find_player(self):
        player = self.stats.search("Messi")

        self.assertIsNone(player)

    def test_search_finds_partial_name(self):
        player = self.stats.search("Gret")

        self.assertEqual(player.name, "Gretzky")

    def test_team_returns_players(self):
        players = self.stats.team("EDM")

        self.assertEqual(len(players), 3)

    def test_team_returns_empty_list(self):
        players = self.stats.team("NYR")

        self.assertEqual(players, [])

    def test_top_returns_players_in_order(self):
        players = self.stats.top(2)

        self.assertEqual(
            [player.name for player in players],
            ["Gretzky", "Lemieux"]
        )


    def test_top_by_goals(self):
        players = self.stats.top(2, SortBy.GOALS)

        self.assertEqual(
            [player.name for player in players],
            ["Lemieux", "Yzerman"]
        )

    def test_top_by_assists(self):
        players = self.stats.top(2, SortBy.ASSISTS)

        self.assertEqual(
            [player.name for player in players],
            ["Gretzky", "Yzerman"]
        )

    def test_top_by_points(self):
        players = self.stats.top(2, SortBy.POINTS)

        self.assertEqual(
            [player.name for player in players],
            ["Gretzky", "Lemieux"]
        )