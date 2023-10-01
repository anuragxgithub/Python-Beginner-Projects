import random

randomNumber = random.randrange(10,50)

def guess(num, attempt):    # Here we are guessing secret number of computer
    if num == randomNumber:
        print(f"Congrats you guessed it in {attempt} attempts.")
        return True
    elif num > randomNumber:
        print("Enter something less")
        return False
    else:
        print("Enter something big")
        return False


def coumputer_guess(x):    # Here computer will guess our secret number.
    #before starting know one thing it will give error if randrange(2,2) same number comes. Cover this edge case.
    high = x
    low = 1
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randrange(low,high)
        else:
            low = guess    # could also be high as low = high
        feedback = input(f"Is {guess} it too high 'h' too low 'l' or correct 'c' : ")
        if feedback == 'h':
            high = guess-1
        elif feedback == 'l':
            low = guess+1

     
    print(f"Yay! Computer guessed you number, {guess}, correctly.")




# num = int(input("Guess the number: "))
# attempt = 1
# while guess(num,attempt) == False:
#     attempt += 1; 
#     num = int(input())


coumputer_guess(100)