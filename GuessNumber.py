import random

random_number = random.randrange(10, 50)

def guess(user_input, attempt):    # Function for guessing the secret number
    if user_input == random_number:
        print(f"Congrats! You guessed it in {attempt} attempts.")
        return True
    elif user_input > random_number:
        print("Enter something less.")
        return False
    else:
        print("Enter something bigger.")
        return False

def computer_guess(user_range):    # Function for the computer to guess the secret number
    # Before starting, consider the case where randrange(2, 2) results in the same number; handle this edge case.
    high = user_range
    low = 1
    feedback = ''

    while feedback != 'c':
        if low != high:
            guess = random.randrange(low, high)
        else:
            low = guess    # Could also be high as low = high
        feedback = input(f"Is {guess} too high 'h', too low 'l', or correct 'c': ")
        
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f"Yay! The computer guessed your number, {guess}, correctly.")

# Uncomment the following lines to let the user guess the number
# user_input = int(input("Guess the number: "))
# attempt = 1
# while not guess(user_input, attempt):
#     attempt += 1
#     user_input = int(input())

# Uncomment the following line to let the computer guess the user's number within a specified range
computer_guess(100)
