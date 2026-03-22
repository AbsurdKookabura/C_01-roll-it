import random

def yes_no(question):



    while True:

        response = input(question).lower()

        # check the user says yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
           return "no"
        else:
            print("please enter yes / no")

def instructions():


    print("""
*** Instructions ****

Roll the dice and try to win!
    """)

    return ""


def int_check():

    error = "Please enter a number more than 13"

    while True:

        # ask user for a number....
        try:
            response = int(input("What is your game goal? "))

            if response > 13:
                return response

            else:
                print(error)

        except ValueError:
            print(error)



def initial_points(which_player):
    """Roll dice twice and return total / if double points apply"""

    double_user = "no"

    # Roll the dice for the user and note if they got a double
    roll_one = random.randint(1, 6)
    roll_two = random.randint(1, 6)

    if roll_one == roll_two:
        double_user = "yes"

    # find the total of both dice rolls
    total = roll_one + roll_two

    # show output
    print(f"{which_player} rolled a {roll_one} and {roll_two} - Total: {total}")

    return total, double_user

def make_statement(statement, decoration):
    """adds emoji / additional characters to the start and end of headings"""

    ends = decoration * 3
    print(f"{ends} {statement} {ends}")


# main starts here...


# at the start of the game, the computer / user score are both zero
comp_score = 0
user_score = 0
rounds_played = 0

game_history = []

# ask the user if they want instructions (check they say yes / no)
want_instructions = yes_no("Do you want to see the instructions ")

# Display the instructions if the user wants to see them...
if want_instructions == "yes":
    instructions()


game_goal = int_check()

# play multiple rounds until a winner has been found
while comp_score < game_goal and user_score < game_goal:

    rounds_played += 1

    # Roll the dice for the user and note if they got a double
    initial_user = initial_points("User")
    initial_comp = initial_points("Comp")

    # Retrieve user points (first item returned from function)
    user_points = initial_user[0]
    comp_points = initial_comp[0]

    double_user = initial_user[1]

    # Let the user know if they qualify for double points
    if double_user == "yes":
        print("Great news - if you win, you will earn double points")

    # assume user goes first...
    first = "User"
    second = "Comp"
    player_1_points = user_points
    player_2_points = comp_points

    # if user has fewer points, they start the game
    if user_points < comp_points:
        print("You start because your initial roll was less than the computer\n")

    # if the user and computer roll equal points, the users is player 1...
    elif user_points == comp_points:
        print("The initial rolls were the same, the user starts!")

    # if the computer has fewer points,switch the computer to 'player 1'
    else:
        player_1_points, player_2_points = player_2_points, player_1_points
        first, second = second, first

    # loop until we have winner
    while player_1_points < 13 and player_2_points < 13:
        print()
        input("press <enter> to continue this round\n")

        # first person rolls the die and score is updated
        player_1_roll = random.randint(1, 6)
        player_1_points += player_1_roll

        print(f"{first}: rolled a {player_1_roll} - has {player_1_points} points")

        # if the first person's score is over 13, end the round
        if player_1_points >= 13:
            break

        # second person rolls the die (and score is updated)
        player_2_roll = random.randint(1, 6)
        player_2_points += player_2_roll

        print(f"{second}: rolled a {player_2_roll} - has {player_2_points} points")

        print(f"{first}: {player_1_points}  | {second}: {player_2_points}")

    # end of round

    # associate player points with either the user or the computer
    user_points = player_1_points
    comp_points = player_2_points

    # switch the user and computer points if the computer went first
    if first == "Comp":
        user_points, comp_points = comp_points, user_points

    # work out who won...
    if user_points > comp_points:
        winner = "User"
        comp_points = 0
    else:
        winner = "Comp"
        user_points = 0

    round_feedback = f"the {winner} won."

    # double user points if eligible
    if winner == "User" and double_user == "yes":
        user_points = user_points * 2


    # update score!
    comp_score += comp_points
    user_score += user_points

    # show overall scores (add this to rounds loop)
    print("*** game update ***")    # replace with call to statement generator
    print(f"user score: {user_score} | computer score {comp_score}")

    history_item = f"Round {rounds_played}: user score: {user_score} | computer score {comp_score}"
    game_history.append(history_item)

# end of entire game, output final results

make_statement( "game over", "*")
print()
if user_score > comp_score:
    print("the user won")   # replace this with statement generator call
else:
    print("the computer won")

print()
make_statement("Game History", "🎲")
for item in game_history:
    print(item)