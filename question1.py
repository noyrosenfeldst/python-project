import random

TREASURE_FILE = "treasure_hunt.txt"
LEADERBOARD_FILE = "leaderboard.txt"

TREASURE = "TREASURE"

MIN_REPEAT = 1
MAX_REPEAT = 20

FORWARD = "1"
BACKWARD = "2"

MAX_SCORES = 10


def create_treasure_file():
    """Create the treasure hunt file."""
    try:
        with open(TREASURE_FILE, "w") as file:

            # Digits from 0 to 9
            for digit in range(10):
                amount = random.randint(MIN_REPEAT, MAX_REPEAT)
                file.write(str(digit) * amount)

            # Treasure word
            file.write(TREASURE)

            # Digits from 9 to 0
            for digit in range(9, -1, -1):
                amount = random.randint(MIN_REPEAT, MAX_REPEAT)
                file.write(str(digit) * amount)

    except PermissionError:
        print("Could not create the file.")


def read_treasure_file():
    """Read and return the treasure file content."""
    try:
        with open(TREASURE_FILE, "r") as file:
            return file.read()

    except FileNotFoundError:
        print("Treasure file was not found.")

    except PermissionError:
        print("Could not read the treasure file.")

    return ""


def get_amount():
    """Ask the user for how many characters to move."""
    try:
        amount = int(input("How many characters?\n"))

        if amount < 0:
            print("Please enter a positive number.")
            return 0

        return amount

    except ValueError:
        print("Invalid number.")
        return 0


def move_position(position, direction, amount, text_length):
    """Move the player position."""
    if direction == FORWARD:
        position += amount

    elif direction == BACKWARD:
        position -= amount

    # Keep inside file limits
    if position < 0:
        position = 0

    if position >= text_length:
        position = text_length - 1

    return position


def play_game():
    """Run the treasure hunt game."""
    text = read_treasure_file()

    if text == "":
        return 0

    position = 0
    moves = 0

    while text[position] not in TREASURE:

        print(f'You are on "{text[position]}"')

        direction = input(
            "Where do you want to move? [1- forward 2- backwards]\n"
        )

        # Validate direction immediately
        if direction != FORWARD and direction != BACKWARD:
            print("Invalid direction.")
            continue

        amount = get_amount()

        position = move_position(
            position,
            direction,
            amount,
            len(text)
        )

        moves += 1

        print(f'You hit "{text[position]}"')

    print("\nYou found the TREASURE!")
    print(f"It took you {moves} moves.")

    return moves


def read_leaderboard():
    """Read leaderboard scores from file."""
    scores = []

    try:
        with open(LEADERBOARD_FILE, "r") as file:

            for line in file:
                parts = line.strip().split(" ", 1)

                if len(parts) == 2:
                    score = int(parts[0])
                    name = parts[1]

                    scores.append((score, name))

    except FileNotFoundError:
        pass

    except PermissionError:
        print("Could not read leaderboard.")

    return scores


def save_leaderboard(scores):
    """Save leaderboard scores to file."""
    try:
        with open(LEADERBOARD_FILE, "w") as file:

            for score, name in scores:
                file.write(f"{score} {name}\n")

    except PermissionError:
        print("Could not save leaderboard.")


def update_leaderboard(score):
    """Update leaderboard if the score is good enough."""
    scores = read_leaderboard()

    if len(scores) < MAX_SCORES or score < scores[-1][0]:

        name = input("You entered the leaderboard! Enter your name:\n")

        scores.append((score, name))

        scores.sort()

        scores = scores[:MAX_SCORES]

        save_leaderboard(scores)

        print("Leaderboard updated.")

    else:
        print("You did not enter the leaderboard.")


def print_leaderboard():
    """Print the leaderboard."""
    scores = read_leaderboard()

    print("\nLeaderboard:")

    if len(scores) == 0:
        print("No scores yet.")
        return

    for index, (score, name) in enumerate(scores, start=1):
        print(f"{index}. {name} - {score} moves")


def main():
    create_treasure_file()
    score = play_game()
    if score > 0:
        update_leaderboard(score)
    print_leaderboard()


main()