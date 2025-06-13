import random

ten_or_hundred = random.choice([10,100])
number = round(random.random()*ten_or_hundred)

print(number)

for i in range(5):

    guess=int(input("Guess any Number between 1 to 100:"))

    if guess == number:
        print("You have Guessed The Number")
        print("The Number Was ",number)
        break

    else:
        if guess>number:
            print("You have entered a larger number")
        elif guess<number:
            print("You have guesse a smaller number")
