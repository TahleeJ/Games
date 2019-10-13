import Random

#Create functions?
#Store information about move history (How many times did you/computer play r/p/s? longest win streak? What is the move history? What was
# played most often)
#Add custom program break
#Take edge cases into account i.e What if an input is not a string?
#Add two player and one player option

print("Endless Rock Paper Scissors")
move = ""
comp_wins = 0
player_wins = 0
ties = 0
round = 0

while(move is not -1):
    round += 1
    print("Round " + str(round) + "\n")
    set = ["r", "p", "s"]
    comp = set[random.randint(0, 2)]
    move = str(input("What's your move?")).lower()
    print("")

    if comp == "r":
        if move == "r" or move == "rock":
            ties += 1
            print("Both played ROCK")
        elif move == "p" or move == "paper":
            player_wins += 1
            print("You played PAPER\nComputer played ROCK")
        else:
            print("You played SCISSORS\nComputer played ROCK")
    elif comp == "p":
        if move == "r" or move == "rock":
            comp_wins += 1
            print("You played ROCK\n\Computer played PAPER")
        elif move == "p" or move == "paper":
            ties += 1
            print("Both played PAPER")
        else:
            player_wins += 1
            print("You played SCISSORS\n\Computer played PAPER")
    else:
        if move == "r" or move == "rock":
            player_wins += 1
            print("You played ROCK\nComputer played SCISSORS")
        elif move == "p" or move == "paper":
            comp_wins += 1
            print("You played PAPER\nComputer played SCISSORS")
        else:
            ties += 1
            print("Both played SCISSORS")

    print("You: " + str(player_wins) + "\tComputer: " + str(comp_wins) + "\tTies: " + str(ties) + "\n")
