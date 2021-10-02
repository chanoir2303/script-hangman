import random

print('H A N G M A N')
start = input('Type "play" to play the game, "exit" to quit: ')
if start == 'play':
    puzzle_options = ['python', 'java', 'kotlin', 'javascript']
    puzzle_selection = random.choice(puzzle_options)
    tries = 8
    guesses = set()

    while True:
        print()
        for letter in puzzle_selection:
            if letter in guesses:
                print(letter, end='')
            else:
                print('-', end='')
        print()

        if set(puzzle_selection).issubset(guesses):
            print("You guessed the word!\nYou survived!")
            break

        guess = input("Input a letter: ")
        if len(guess) != 1:
            print("You should input a single letter")
            continue
        elif guess not in set('qwertyuiopasdfghjklzxcvbnm'):
            print("Please enter a lowercase English letter")
            continue
        elif guess in guesses:
            print("You've already guessed this letter")
            continue
        elif guess not in puzzle_selection:
            print("That letter doesn't appear in the word")
            tries -= 1
            if tries == 0:
                print("You lost!")
                break
        guesses.add(guess)
elif start == 'exit':
    pass
else:
    print('Type "play" to play the game, "exit" to quit: ')