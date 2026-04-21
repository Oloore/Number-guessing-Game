import random
#from playsound import playsound  # pip install playsound
#The import random generate random number

Number = random.randint(1,500) # it specify the limit of the number generated

while True:
    user_guess = int(input("GUESS A NUMBER: "))
    
    if user_guess < Number:
        print("Too low! Try again.")
    elif user_guess > Number:
        print("Too high! Try again")
    else:
        print("you got the correct number!")
        break  # it stops the loop once the user guessed the number
print ("Welcome to the Show")
Name = input("Nice, your guessed correctly!! Enter your name:  ")

import time
user_input = int(input("Enter a number: "))

for i in range(1, user_input+ 1):
    print(i)
    #playsound('alert.mp3')  # Play before sleep
    time.sleep(1)
    #playsound('alert.mp3')  # Play after sleep

# Reverse the string inside the name
reve_name = Name[::-1]
print("your reversed name is",reve_name)

def power (x,y):
    num1 = x
    num2 = y
    return x ** y

def Square(x):
    return x ** 2
def Cube(x):
    return x ** 3

def Binary(x):
    bina = []
    while x > 0:
        bina.append(x % 2)
        x //= 2
    bina.reverse() # reverses the number
    return bina
    

choice = int(input("1 for power, 2 for Square, 3 for Cube, 4 for binary: "))
if choice == 1:
    num1 = int(input("Enter base number: "))
    num2 = int(input("Enter a number: "))
    answer = power(num_1, num_2)
    print (answer)
    
elif choice == 2:
    num = int(input("Enter a number: "))
    answer = Square(num)
    print(answer)
    
elif choice == 3:
    num = int(input("Enter a number: "))
    answer = Cube(num)
    print(answer)
    
elif choice == 4:
    num = int(input("Enter a number: "))
    answer = Binary(num)
    print(answer)
    
else:
    print("choose from choice")

import time
user_input = int(input("Enter a number: "))

for i in range(1, user_input+ 1):
    print(i)
    time.sleep(1)
    
    
print("bye for now")
    