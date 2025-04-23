
#input section talking about

import time
print("Welcome to this Minigame!👋")
print("Your objective will be to cool down the planet by eliminating objects which you think harm the planet 🌍")
print("Based off your understanding, if you think you are confident type yes, if you are not type no")

#processing section
client = input("So what will it be? (yes/no)")

#game section if yes confident there will be more objects
if client == "yes":
    difficulty = "hard"
    objects = ["Trash bag", "Car", "Plant", "Plane", "Factory", "Tree", "Animal Cow", "Forest"]
    round = 5
elif client == "no":
    difficulty = "easy"
    objects = ["Trash", "Ship", "Bus", "Plant", "Humans", "Solar Panel"]
    round = 3

usefulobject = ["Plant", "Solar Panel", "Tree", "Forest"]

#starting the game / code and etc
score = 0

for startinggame in score(round):
    objectgame = object[startinggame]
    print("object {turn +1}:
