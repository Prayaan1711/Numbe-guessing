
import random
playing = True
name = input("Enter your name: ")

print("Hello! "+name+" Welcome to number guessing game. I will be thinking of a number between 1 to 50 and you have 6 tries to guess")

num = random.randint(0,50)

if num%2 == 0:
    print("Hint: It is an even number.")
else:
    print("Hint: It is an odd number.")

count = 0
while playing:
    guess = int(input("Enter your guess: "))
    count=count+1
    if guess == num:
        print("You win")
        break
    else:
        if guess>=num:
            print("Guess is too high")
        else:
            print("Guess is too low")
    
    if count == 6:
        print("You are out of guesses...")
        print("The number was ",num)
        print("Game over")
        break
