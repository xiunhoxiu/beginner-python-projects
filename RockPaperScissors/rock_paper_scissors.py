import random


def play():

    choices = ["r", "p", "s"]
    computer = random.choice(choices)
    user = None

    while user not in choices:
        user = input("""
        Let's play! \n
        'r' for rock, 
        'p' for paper,
        's' for scissors? \n 
        what is your choice?: """).lower()

    if user == computer:
        print(f'\nIt\'s a tie.')
        return encore()

    if is_win(user, computer):
        print(f'\nCongrats, you won! I picked {translate(computer)}.')
        return encore()

    print(f'\nYou lost against my choice {translate(computer)}!')
    return encore()


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
        output += mapping.get(items, "invalid!")
    return output


def encore():
    play_again = input("Play again [y/n]? ").lower()

    if play_again != "y":
        return 'Bye!'
    else:
        play()


print(play())
