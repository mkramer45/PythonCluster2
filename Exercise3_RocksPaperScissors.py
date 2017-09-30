#Create Infinite Loop

while True:
    print("Selection: Rock | Paper | Scissor")

# Ask User for Selection
    PlayerOne = input("Player1 Input: ")
    PlayerTwo = input("Player2 Input: ")

# Compare input from the two users and determine the winner based on RPS rules
    if PlayerOne == PlayerTwo:
        print("It's a tie! ")
    elif ((PlayerOne == "Rock" and PlayerTwo == "Scissors") or (PlayerOne == "Scissors" and PlayerTwo == "Paper") or (PlayerOne == "Scissors" and PlayerTwo == "Paper")):
        print("Player One Wins! ")
    else:
        print("Player Two Wins! ")

# R-P-S APP