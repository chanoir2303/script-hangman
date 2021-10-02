import random

print("""
H A N G M A N
""")

word = ['python', 'java', 'kotlin', 'javascript']
pick_choice = random.choice(word)
tries = 0

# replace chars by '-'
if pick_choice == 'java':
    hidden_word = pick_choice.replace(pick_choice[:], '-' * len(pick_choice[:]))
else:
    hidden_word = pick_choice.replace(pick_choice[:], '-' * len(pick_choice[:]))

while tries <= 8:
    x = input(f'{hidden_word}\nInput a letter: ')
    if x in set(pick_choice):
        # replace char at give position
        hidden_word = hidden_word[:pick_choice.index(x)] + pick_choice[pick_choice.index(x)] + hidden_word[pick_choice.index(x) + 1:]
        tries += 1
    if hidden_word == pick_choice:
        print(hidden_word)
        break
    elif x not in set(pick_choice):
        print("That letter doesn't appear in the word")
        tries += 1
print("""
Thanks for playing!
We'll see how well you did in the next stage
    """)