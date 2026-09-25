
import random


# Store all the details of each player
class Player:
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.losses = 0
        self.draws = 0
        self.points = 0


# Ask the user for a valid number
def ask_number(message, minimum, maximum):
    while True:
        try:
            number = int(input(message))

            if minimum <= number <= maximum:
                return number
            else:
                print("Please enter a number within the given range.")

        except ValueError:
            print("That's not a valid number. Try again.")


# Get the names of all the players
def get_players(total_players):
    players = []
    names = set()

    for i in range(total_players):
        while True:
            name = input(f"Enter Player {i + 1}'s name: ").strip()

            if name == "":
                print("Please enter a name.")

            elif name.lower() in names:
                print("This name is already taken. Try another one.")

            else:
                names.add(name.lower())
                players.append(Player(name))
                break

    return players


# Check who won the round
def check_winner(player_choice, computer_choice):

    if player_choice == computer_choice:
        return "draw"

    elif (
        (player_choice == "rock" and computer_choice == "scissors")
        or (player_choice == "paper" and computer_choice == "rock")
        or (player_choice == "scissors" and computer_choice == "paper")
    ):
        return "win"

    else:
        return "loss"


# Play one round
def play_round(player, round_number):

    choices = ["rock", "paper", "scissors"]

    print(f"\n--- Round {round_number} | Player: {player.name} ---")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    while True:
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice in ["1", "2", "3"]:
            player_choice = choices[int(choice) - 1]
            break
        else:
            print("Oops! Choose 1, 2, or 3.")

    # Let the computer pick a choice
    computer_choice = random.choice(choices)

    print(f"\nYou chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")

    # Find out who won
    result = check_winner(player_choice, computer_choice)

    if result == "win":
        print(f"Great job, {player.name}! You won this round.")
        player.wins += 1
        player.points += 3

    elif result == "loss":
        print("The computer won this round. Better luck next time!")
        player.losses += 1

    else:
        print("It's a draw! Nobody gets the win.")
        player.draws += 1
        player.points += 1

    print(f"Your total points: {player.points}")


# Show everyone's scores at the end
def show_leaderboard(players):

    # Put the highest-scoring players at the top
    players.sort(
        key=lambda player: (player.points, player.wins, -player.losses),
        reverse=True
    )

    print("\n" + "=" * 65)
    print("              CHAMPIONSHIP LEADERBOARD")
    print("=" * 65)

    print(
        f"{'Rank':<8}{'Player':<18}{'Wins':<8}"
        f"{'Losses':<9}{'Draws':<8}{'Points':<8}"
    )

    print("-" * 65)

    for rank, player in enumerate(players, start=1):
        print(
            f"{rank:<8}{player.name:<18}{player.wins:<8}"
            f"{player.losses:<9}{player.draws:<8}{player.points:<8}"
        )

    print("=" * 65)

    return players


# Announce the champion
def announce_champion(players):

    if not players:
        print("No players joined the championship.")
        return

    highest_score = players[0].points

    champions = []

    for player in players:
        if player.points == highest_score:
            champions.append(player.name)

    if len(champions) == 1:
        print(f"\nCongratulations, {champions[0]}!")
        print("You are the champion of the championship!")
        print(f"Final score: {highest_score} points")

    else:
        print("\nIt's a tie! We have joint champions:")
        print(", ".join(champions))
        print(f"Final score: {highest_score} points")


# Run the whole championship
def main():

    print("=" * 50)
    print("       ROCK PAPER SCISSORS CHAMPIONSHIP")
    print("=" * 50)

    print("\nWelcome to the championship!")
    print("Let's see who wins today.")

    print("\nGame Rules:")
    print("Rock beats Scissors")
    print("Paper beats Rock")
    print("Scissors beats Paper")
    print("Win = 3 points | Draw = 1 point | Loss = 0 points")

    total_players = ask_number(
        "\nHow many players are joining? (2-20): ", 2, 20
    )

    total_rounds = ask_number(
        "How many rounds should each player play? (1-50): ", 1, 50
    )

    players = get_players(total_players)

    print("\nEveryone is ready!")
    print("Let the championship begin!")

    # Give every player the same number of rounds
    for player in players:

        print(f"\nIt's {player.name}'s turn!")

        for round_number in range(1, total_rounds + 1):
            play_round(player, round_number)

    # Show the final scores and announce the champion
    leaderboard = show_leaderboard(players)
    announce_champion(leaderboard)

    print("\nThanks for playing! See you next time.")


# Start the game
if __name__ == "__main__":
    main()
    