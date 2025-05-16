import random

# This part is to ensure the user is engaged
input("Press Any key to start the game")
#Random generator(1-50)
number = random.randint(1, 50)


while True:
   guess = int(input("Guess a number between 1 and 50: "))
   #Ensure that only numbers are allowed to be entered
   if not guess_input.isdigit():
            print("Invalid input. Please enter a number.")
            continue
#convert the guess to  an integer
        guess = int(guess_input)
   if guess == number:
       print("You guessed it right!")
       break
      #Loop while giving hints until the correct guess
   elif guess < number:
       print("Too low, try again!")
   else:
       print("Too high, try again!")
print(f"The number was {number}")
