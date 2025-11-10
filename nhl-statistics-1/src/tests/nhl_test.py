import unittest

from statistics_service import StatisticsService
from player_reader import PlayerReader
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
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_firstPlayerName(self):
        self.assertEqual(self.stats._players[0].name, "Semenko")

    def test_firstPlayerTeam(self):
        self.assertEqual(self.stats._players[0].team, "EDM")

    def test_firstPlayerGoals(self):
        self.assertEqual(self.stats._players[0].goals, 4)

    def test_firstPlayerAssists(self):
        self.assertEqual(self.stats._players[0].assists, 12)

    def test_search(self):
        player = self.stats.search("Kurri")
        #self.assertIsNotNone(player)
        self.assertEqual(player.name, "Kurri")

    def test_search_olematon(self):
        self.assertIsNone(self.stats.search("asdjkasdjhf"))

    def test_pisteet(self):
        player = self.stats.search("Kurri")
        self.assertEqual(player.points, 90)

    #def test_player_str_method(self):
      #  player = Player("Test", "AAA", 5, 7)
     #   expected = "Test AAA 5 + 7 = 12"
     #   self.assertEqual(str(player), expected)

    def test_players_of_team(self):
        joukkue = self.stats.team("EDM")
        names = [p.name for p in joukkue]
        self.assertCountEqual(names, ["Semenko", "Kurri", "Gretzky"])

    def test_top_returns_sorted_players(self):
        top_players = self.stats.top(2)
        self.assertTrue(top_players[0].points >= top_players[1].points)

    def sort_by_points(self):
        top_players = self.stats.top(2)
        self.assertEqual(top_players[0].name, "Gretzky")