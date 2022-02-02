import random


def guess(n):
    random_number = random.randint(1, n)
    guessing = 0
    while guessing != random_number:
        guessing = int(input(f'Guess a number between 1 and {n}: '))
        if guessing < random_number:
            print('Your guess is too low. Try a higher number.')
        elif guessing > random_number:
            print('Your guess is too high. Try a lower number.')

    print(f'Yay! Congrats! You have guess the secret number {random_number}.')


def computer_guess(n):
    low = 1
    high = n
    feedback = ''
    while feedback != 'c':
        if low != high:
            guessing = random.randint(low, high)
        else:
            guessing = low
        guessing = random.randint(low, high)
        feedback = input(f'My turn to guess. Is {guessing} too high (H), too low (L), or correct (C)?: ').lower()
        if feedback == 'h':
            high = guessing - 1
        elif feedback == 'l':
            low = guessing + 1
    print(f'Yay! The computer guessed your secret number, {guessing}!')


guess(1000)
computer_guess(1000)

