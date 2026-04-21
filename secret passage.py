while True:
    door = input("Which door do you want to enter? (1-10): ")
    
    if door == "3":
        print("You found the exit! Congratulations!")
        break
    elif door == "secret":
        print("You discovered the secret passage! You win!")
        break
    elif door == "skip":
        print("You skipped this door. Try again!")
        continue
    elif door.isdigit() and 1 <= int(door) <= 10:
        print("You entered a dead end. Go back to the beginning.")
    else:
        print("Invalid input. Please enter a number between 1 and 10, or type 'skip' or 'secret'.")
