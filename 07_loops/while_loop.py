import random
# i = 0
# while i<10:
#     print("Hello, World!")
#     i += 1
# else:
#     print("The loop is done")


guess = int(input("Enter a number: "))

jackport = random.randint(1, 100)

while guess != jackport:
    if guess < jackport:
        print("Too low")
    else:
        print("Too high")
    guess = int(input("Enter a number: "))
else:
    print("You guessed it!")
