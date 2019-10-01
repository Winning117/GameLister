def list_games(number_of_players):
    """
    Lists all of the games that you can play with the current number of players you have
    """
    with open("games.txt") as f:
        content = f.readlines()
        for line in content:
            if not line.startswith("#"):
                game_name = line.split(",")[0]
                minimum_number_of_players = int(line.split(",")[1])
                maximum_number_of_players = int(line.split(",")[2])
                if number_of_players >= minimum_number_of_players and number_of_players <= maximum_number_of_players:
                    print(f"{game_name} - {minimum_number_of_players} to {maximum_number_of_players} players")


def main():
    number_of_players = input("How many players are there? ")
    print()
    list_games(int(number_of_players))


if __name__ == "__main__":
    main()
