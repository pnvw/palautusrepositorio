from rich.console import Console
from rich.table import Table

from player_reader import PlayerReader
from player_stats import PlayerStats


def create_table(players, filter_value, season):
    table = Table(title=f"Players from {filter_value} ({season})")

    table.add_column("Name")
    table.add_column("Team")
    table.add_column("Goals", justify="right")
    table.add_column("Assists", justify="right")
    table.add_column("Points", justify="right")

    for player in players:
        table.add_row(
            player.name,
            player.team,
            str(player.goals),
            str(player.assists),
            str(player.goals + player.assists)
        )

    return table


def get_players_for_filter(stats, filter_type):
    if filter_type == "team":
        team = input("Team: ")
        return stats.top_scorers_by_team(team), team

    nationality = input("Nationality: ")
    return stats.top_scorers_by_nationality(nationality), nationality


def main():
    filter_type = input("Filter by (nationality/team): ").strip().lower()
    season = input("Season: ")

    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players, filter_value = get_players_for_filter(stats, filter_type)

    console = Console()
    table = create_table(players, filter_value, season)
    console.print(table)


if __name__ == "__main__":
    main()
