import random


input("Press Enter to start the game")
number = random.randint(1, 50)


while True:
   guess = int(input("Guess a number between 1 and 50: "))
    if not guess_input.isdigit():
            print("Invalid input. Please enter a number.")
            continue

        guess = int(guess_input)
   if guess == number:
       print("You guessed it right!")
       break
   elif guess < number:
       print("Too low, try again!")
   else:
       print("Too high, try again!")
print(f"The number was {number}")
