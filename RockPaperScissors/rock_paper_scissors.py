import random


def play():
    user = input("""
    Let's play! \n
    'r' for rock, 
    'p' for paper,
    's' for scissors?: \n 
    what is your choice?: """)
    computer = random.choice(["r", "p", "s"])

    if user == computer:
        return 'It\'s a tie.'

    if is_win(user, computer):
        return f'You won! I chose {translate(computer)}.'

    return f'You lost against my choice {translate(computer)}!'


def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
            or (player == 'p' and opponent == 'r'):
        return True


def translate(item):
    mapping = {
        "r": "rock",
        "s": "scissors",
        "p": "paper"
    }
    output = ""
    for items in item:
        output += mapping.get(items, "!")
    return output


print(play())
