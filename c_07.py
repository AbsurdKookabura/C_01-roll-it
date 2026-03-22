
#initialise list to hold game history
game_history = []

# get data (base component does this already, code below fore testing purposes)
user_score = 0
comp_score = 0

while True:
    rounds_played = input("round? ")
    if rounds_played == "":
        break

    user_points = int(input("user points "))
    comp_points = int(input("computer points?"))
    winner = input("who won? ")
    user_score = int(input("user score: "))
    comp_score = int(input("computer score: "))

    game_results = f"round {rounds_played}: user points: {user_points} | "
    f"computer points {comp_points}, {winner} wins "
    f"({user_score} | {comp_score})")

    game_history.append(game_results)

print("game history")

for item in game_history:
    print(item)