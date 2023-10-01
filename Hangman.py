#We will make all letters in words Uppercase because there will be issue for uppercase 
#and lowercase characteres.
import random
import string
from hangman_words import words

def get_word():
    word_choosen = random.choice(words)

    while "-" in word_choosen or " " in word_choosen:
        word_choosen = random.choice(words)

    return word_choosen.upper()

def hangman():
    word_choosen = get_word()
    word_letters = set(word_choosen)
    alphabet = set(string.ascii_uppercase)  #string.ascii_uppercase ontains all the uppercase letters of the English alphabet
    used_letters = set()            #note set in python are unordered collection
    
    lives = 8

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        #letters used
        #.join() converts the iterables into a string eg ' '.join(['a', 'b', 'cd']) -> "a b cd"
        print("You have", lives, "lives left and you have used these letters: ", ' '.join(used_letters))
        
        #also we will tell the player what the current word is using dashes eg (W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word_choosen]   #it creates a new list based on the letters in word_choosen. It adds letter to the list if it is present in the used_letter else add '-'. NOTE: for loop will execute first
        print("Current word: ", ' '.join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:  #makes sure that the entered char is b/w A-Z and not already gussed letter
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)    #remove letter from the set of word_letters if user's letter match.
            else:
                lives = lives-1
                print("Letter is not in word.")
                
        elif user_letter in used_letters:
            print("You already used this character. Please try again.")
        
        else:
            print("Enter valid character!")

    if lives == 0:
        print("You died, sorry. The word was", word_choosen)
    else:
        print(f"You guessed the word {word_choosen} !!")
hangman()