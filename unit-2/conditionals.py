total = 10

if total % 2 == 0:
    print("even")
else:
    print("odd")

first_name = "Chizea"

if len(first_name) > 7:
    print("Nice size")
else:
    print("Not nice size")

#comparison operators
# == 
# >
# <
# >=
# <=
# !=

score = 60

if score >= 80:
    print("A")
elif score >= 60:
    print("B")
elif score >= 50:
    print("C")
else:
    print("F")

# A non empty string is 'Truthy
if "hello world":
    print("yes, its true")

# An empty string is Falsey
if "":
    print("its true")
else:
    print("it is false")

# Any number that is not zero is truthy
if 13:
    print("its true")

#0 is falsey
if 0:
    print("its true")
else:
    print("its false")

a= -10
b= -11

if a > 0 or b <0:
    print("Good!")

if a > 0 and b < 0:
    print("Excellent!")
else: 
    print("Not good")