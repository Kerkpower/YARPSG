import random

TOOLS = ("rock", "paper", "scissors")


def get_input() -> str:
    move = input("Choose your move: ").lower()

    while not check_input(move):
        print("The specified move is not correct, try again.")
        move = input("Choose your move: ").lower()

    return move


def check_input(move: str) -> bool:
    return move in TOOLS


def random_opponent_tool() -> str:
    return random.choice(TOOLS)


def check_winner(user_move: str, opponent_move: str) -> str:
    if user_move == opponent_move:
        return "Tie"

    match user_move:
        case "rock":
            if opponent_move == "paper":
                return "Loss"

        case "paper":
            if opponent_move == "scissors":
                return "Loss"

        case "scissors":
            if opponent_move == "rock":
                return "Loss"

    return "Win"


def main():
    print("----Rock Paper Scissors----")

    user_move = get_input()
    random_move = random_opponent_tool()

    print(check_winner(user_move, random_move))


if __name__ == "__main__":
    main()
