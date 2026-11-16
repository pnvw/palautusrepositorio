import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from player import Player
from player_stats import PlayerStats


class ReaderStub:
    def __init__(self, players):
        self._players = players

    def get_players(self):
        return self._players


def build_players():
    return [
        Player({"name": "Ana", "nationality": "FIN", "assists": 20, "goals": 10, "team": "TBL"}),
        Player({"name": "Ben", "nationality": "USA", "assists": 15, "goals": 25, "team": "TBL"}),
        Player({"name": "Cia", "nationality": "FIN", "assists": 30, "goals": 5, "team": "BOS"}),
        Player({"name": "Dan", "nationality": "USA", "assists": 5, "goals": 15, "team": "TBL"}),
        Player({"name": "Eli", "nationality": "SWE", "assists": 12, "goals": 8, "team": "BOS"}),
    ]


def test_top_scorers_by_nationality_filters_and_sorts_by_points():
    stats = PlayerStats(ReaderStub(build_players()))

    players = stats.top_scorers_by_nationality("FIN")

    assert [player.name for player in players] == ["Cia", "Ana"]


def test_top_scorers_by_team_filters_and_sorts_by_points():
    stats = PlayerStats(ReaderStub(build_players()))

    players = stats.top_scorers_by_team("TBL")

    assert [player.name for player in players] == ["Ben", "Ana", "Dan"]


def test_top_scorers_by_team_returns_empty_list_when_no_match():
    stats = PlayerStats(ReaderStub(build_players()))

    players = stats.top_scorers_by_team("MTL")

    assert players == []
