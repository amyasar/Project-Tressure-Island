print("Welcome to the Tressure Island")
print("Your mission is to find the tressure")

choice1 = input('You are at a road. Where do you want to go? Type"Left" or "Right".\n').lower()
if choice1 == "left":
# Continue Game
    choice2 = input("Now choose Wisely! You\'re going to \"Swim\" or \"Wait\". \n").lower()
    if choice2 == "wait":
        # Game Continue
        choice3 = input('Please choose one door between \"Red\" , \"Yellow\" and \"Blue\".\n').lower()
        if choice3 == "red" and "blue":
            print("Game Over")
        elif choice3 == "yellow":
            print("You Won")
        else:
            print("You Lost")
    else: 
        print("You gotta wait. Agey gele baaghe khai")




else:
    print("You chose Right! But the treasure was on the left side. Game Over")