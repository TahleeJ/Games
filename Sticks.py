# Add custom program break
# Format board
# Create other functions to stop having so much repeating code

p1_name = ""
p2_name = ""
p1_h1 = 1
p1_h2 = 1
p2_h1 = 1
p2_h2 = 1
p1_hand1 = True
p1_hand2 = True
p2_hand1 = True
p2_hand2 = True
p1_hands = 2
p2_hands = 2

p1_name = str(input("What's your name player 1? "))
p2_name = str(input("What's your name player 2? "))
print("\n\n")

def printBoard():
    print("%s\nHand 1: %s \t Hand 2: %s\n" % (p1_name, p1_h1, p1_h2)) # 26 spaces, 30 spaces for border
    print("%s\nHand 1: %s \t Hand 2: %s\n" % (p2_name, p2_h1, p2_h2))

def move(p_name):
    y_hand = 0
    o_hand = 0
    move = str(input("Hit or Split %s? " % (p_name)))
    if move.lower() == "s" or move.lower() == "split":
        split(p_name)
    elif move.lower() == "h" or move.lower() == "hit":
        y_hand = input("What hand would you like to use? ")
        o_hand = input("What hand would you like to hit? ")
        hit(p_name, y_hand, o_hand)
    else:
        recall(p_name, null)
    print("\n\n")

def recall(p_name, mv):
    print("\nYou cannot make that move. Try again.\n")
    if mv == "hit":
        hit(p_name, y_hand, o_hand)
    elif mv == "split":
        split(p_name)
    else:
        move(p_name)
    print("\n\n")

def split(p_name):
    global p1_h1
    global p1_h2
    global p2_h1
    global p2_h2

    num1 = int(input("How many on hand 1? "))
    num2 = int(input("How many on hand 2? "))
    if str(p_name) == p1_name:
        if (num1 + num2 > p1_h1 + p1_h2):
            recall(p1_name, "split")
        else:
            p1_h1 = num1
            p1_h2 = num2
    elif str(p_name) == p2_name:
        if (num1 + num2 > p2_h1 + p2_h2):
            recall(p2_name, "split")
        else:
            p2_h1 = num1
            p2_h2 = num2

# def player_hit(p_name, y_hand, o_hand, ):
#
#
#     if (int(y_hand) == 1 and p1_hand1 == True):
#         if int(o_hand) == 1 and p2_hand1 == True:
#             p2_h1 += p1_h1
#             if p2_h1 > 5:
#                 p2_h1 = p2_h1 - 5
#         elif int(o_hand) == 2 and p2_hand2 == True:
#             p2_h2 += p1_h1
#             if p2_h2 > 5:
#                 p2_h2 = p2_h2 - 5
#         else:
#             recall(p1_name, "hit")
#     elif int(y_hand) == 2 and p1_hand1 == True:
#         if int(o_hand) == 1 and p2_hand1 == True:
#             p2_h1 += p1_h2
#             if p2_h1 > 5:
#                 p2_h1 = p2_h1 - 5
#         elif int(o_hand) == 2 and p2_hand2 == True:
#             p2_h2 += p1_h2
#             if p2_h2 > 5:
#                 p2_h2 = p2_h2 - 5
#         else:
#             recall(p1_name, "hit")
#     else:
#         recall(p1_name, "hit")

def hit(p_name, y_hand, o_hand):
    global p1_hand1
    global p1_hand2
    global p2_hand1
    global p2_hand2
    global p1_h1
    global p1_h2
    global p2_h1
    global p2_h2
    global p1_hands
    global p2_hands

    if str(p_name) == p1_name:
        if (int(y_hand) == 1 and p1_hand1 == True):
            if int(o_hand) == 1 and p2_hand1 == True:
                p2_h1 += p1_h1
                if p2_h1 > 5:
                    p2_h1 = p2_h1 - 5
            elif int(o_hand) == 2 and p2_hand2 == True:
                p2_h2 += p1_h1
                if p2_h2 > 5:
                    p2_h2 = p2_h2 - 5
            else:
                recall(p1_name, "hit")
        elif int(y_hand) == 2 and p1_hand1 == True:
            if int(o_hand) == 1 and p2_hand1 == True:
                p2_h1 += p1_h2
                if p2_h1 > 5:
                    p2_h1 = p2_h1 - 5
            elif int(o_hand) == 2 and p2_hand2 == True:
                p2_h2 += p1_h2
                if p2_h2 > 5:
                    p2_h2 = p2_h2 - 5
            else:
                recall(p1_name, "hit")
        else:
            recall(p1_name, "hit")

    elif str(p_name) == p2_name:
        if int(y_hand) == 1 and p2_hand1 == True:
            if int(o_hand) == 1 and p1_hand1 == True:
                p1_h1 += p2_h1
                if p1_h1 > 5:
                    p1_h1 = p1_h1 - 5
            elif int(o_hand) == 2 and p1_hand2 == True:
                p1_h2 += p2_h1
                if p1_h2 > 5:
                    p1_h2 = p1_h2 - 5
            else:
                recall(p2_name, "hit")

        elif int(y_hand) == 2 and p2_hand2 == True:
            if int(o_hand) == 1 and p1_hand1 == True:
                p1_h1 += p2_h2
                if p1_h1 > 5:
                    p1_h1 = p1_h1 - 5
            elif int(o_hand) == 2 and p1_hand2 == True:
                p1_h2 += p2_h2
                if p1_h2 > 5:
                    p1_h2 = p1_h2 - 5
            else:
                recall(p2_name, "hit")

        else:
            recall(p2_name, "hit")

while p1_hands is not 0 and p2_hands is not 0:
    printBoard()
    print("\n\n")
    move(p1_name)
    if p2_h1 == 5:
        p2_hand1 = False
        p2_h1 = 0
        p2_hands = p2_hands - 1
        if p2_hands is not 0:
            print("\n%s lost one hand, hand 1 is no longer available" %(p2_name))

    elif p2_h2 == 5:
        p2_hand2 = False
        p2_h2 = 0
        p2_hands = p2_hands - 1
        if p2_hands is not 0:
            print("\n%s lost one hand, hand 2 is no longer available" %(p2_name))

    if p2_hands is not 0:
        print("\n\n")
        printBoard()
        print("\n\n")
        move(p2_name)
        if p1_h1 == 5:
            p1_hand1 = False
            p1_h1 = 0
            p1_hands = p1_hands - 1
            if p1_hands is not 0:
                print("\n%s lost one hand, hand 1 is no longer available" %(p1_name))

        elif p1_h2 == 5:
            p1_hand2 = False
            p1_h2 = 0
            p1_hands = p1_hands - 1
            if p1_hands is not 0:
                print("\n%s lost one hand, hand 2 is no longer available" %(p1_name))

    else:
        break

if p1_hands > 0:
    print("\n\n%s is the winner!" % p1_name)
else:
    print("\n\n%s is the winner!" % p2_name)
