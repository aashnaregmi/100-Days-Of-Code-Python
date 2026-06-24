import random
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
totallen=len(chosen_word)
placeholder = ["_"] * totallen

lifeline = 6





while  lifeline>=0 and "_" in placeholder:
    placeholderstr="".join(placeholder)
    print(f"Guess word :{placeholderstr}")
    guess = input("Guess a letter : ").lower()
    if guess in placeholder:
        print(f"You already guessed :{guess}.\nGuess another word ")
    elif guess in chosen_word:
       for i in range(0,totallen):
           if chosen_word[i]==guess:
               placeholder[i]=guess

    else:
        print(f"\'{guess}\' is not there ")
        print(f"{stages[lifeline]}")
        lifeline-=1
        print(f"lifeline:{lifeline}/6")


if "_" not in placeholder:
        print("You won")
else:
        
        print("You loose")
        print(f"The correct word in {chosen_word}")









