import random

name = input("Please enter your name (or e to end):")

messages = ["Awesome", "Nice", "Great job!","Party Animal"]

while name != "e":
    pos = random.randint(0, len(messages) -1)
    print(messages[pos])
    name = input("Please enter your name (or e to end):")