import random
number=random.randint(1,10)
guess=0
guess_history=[]
print("choose a number 1-10")

while guess!=number:
    guess= int(input("enter a guess:"))

    if guess < number:
        print("Too low")
        guess_history.append(guess)
        print("your guesses so far: ", guess_history)

    elif guess > number:
        print("too high")
        guess_history.append(guess)
        print("your guesses so far: ", guess_history)

    else:
        print(f"correct the number was {number}")
        print("Here are your incorrect guesses:", guess_history)
   
