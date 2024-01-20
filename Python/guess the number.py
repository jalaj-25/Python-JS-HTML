import random
secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 10
print("Welcom in the game of guessing the number!!")
while attempts <= max_attempts:
    guess = int(input("Enter your guess: "))
    attempts += 1
    if guess == secret_number:
        print("Congratulation you have guessed the number", secret_number ,"is right in", attempts, "attempts!!")
        break
    elif guess < secret_number:
        print("Too low. Try again")
    else:
        print("Too high. Try again")
else:
    print("Sorry you have reached max attempts. The secret number is ",secret_number)
