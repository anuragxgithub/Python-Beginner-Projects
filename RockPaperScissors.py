import random


def play():
    opponent = random.choice(["r", "p", "s"])
    player = input("Whats you choice ? 'r' for rock, 'p' for paper, 's' for scissor: ")

    if player == opponent:
        return "It\'s a tie!"
    if is_win(player, opponent):
        return "You won!"
    return "You lost!"
    

def is_win(player, opponent):
    # return true if player wins
    # r > s, p > r, s > p
    if (player == "p" and opponent == "r") or (player == "s" and opponent == "p") or (player == "r" and opponent == "s"):
        return True
    
print(play())