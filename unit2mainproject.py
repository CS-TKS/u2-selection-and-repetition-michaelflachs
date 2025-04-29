
#input section talking about

import time
print("Welcome to this Minigame!👋")
print("Your objective will be to cool down the planet by eliminating objects which you think harm the planet 🌍")
print("Based off your understanding, if you think you are confident type yes, if you are not type no")

#processing section
client = input("So what will it be? (Yes!/No!)")

#game section if yes confident, there will be more objects
if client == "Yes!":
    difficulty = "hard"
    objects = ["Trash bag", "Car", "Plant", "Plane", "Factory", "Tree", "Animal Cow", "Forest"]
    round = 5
elif client == "No!":
    difficulty = "easy"
    objects = ["Trash", "Ship", "Bus", "Plant", "Humans", "Solar Panel"]
    round = 3
else:
    print("Invalid result! The game will now stop")
    exit()

usefulobject = ["Plant", "Solar Panel", "Tree", "Forest"]

#game beginnign to start



score = 0

for startgame in range(rounds):
    objectsgame = objects[startgame]
    print("Object {startgame + 1}: {usefulobject}")
    cdecision = input("Do you wish to select this / and eliminate it? (yes/no): ")


    if cdecision == "yes":
        if objectsgame in usefulobject:
            print("Oh no! You selected the wrong object, this object helps the climate")
            score -= 1
        else:
            print("Good job! This object harms the climate")
            score += 1
    elif cdecision == "no":
        if objectsgame in usefulobject:
            print("Nice! Good job you helped the climate!")
            score +=1
    else:
            print("Oops! You selected the wrong object which helps the climate")
            score -=1

    print("Thanks for playing! Hopefully you have learnt something new today :)")














