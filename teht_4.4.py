import random
print("Let us play a guessing game!")
val = random.randint(1, 100)
count = 1
guess = int(input("\n\t\tEnter a number between 1 and 100: "))
while(guess != val):
    if guess > val:
        print("Too high. Try again:", guess)
    elif guess < val:
        print("Too low. Try again:", guess)
    guess = int(input("\n\t\tEnter a number between 1 and 100: "))
    count += 1
print("\nCongratulations! You got it in ", count, " guesses.")
input("Press enter to quit.")