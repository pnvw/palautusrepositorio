from player_reader import PlayerReader
from player_stats import PlayerStats
from rich.console import Console
from rich.table import Table

def main():
    nationality = input("Nationality: ")
    season = input("Season: ")

    url = f"https://studies.cs.helsinki.fi/nhlstats/2024-25/players"

    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    players = stats.top_scorers_by_nationality(nationality)

    console = Console()

    table = Table(title=f"Players from {nationality} ({season})")
    
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

    console.print(table)

if __name__ == "__main__":
    main()