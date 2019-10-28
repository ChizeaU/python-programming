# The For loop

name = "Chizea"
# print the odd numbers between 1 and 10 
for num in range(1,11):
    if num % 2 == 1:
        print(num)
        
#print the sum of the even numbers
total= 0 
for no in range(1,11):
    if no % 2 == 0:
        total = total + no
    
print(total)

full_name = "Chizea Ubosi"

for n in full_name:
    if n == "a" or n=="e" or n=="i" or n=="o" or n=="u":
        print(n)
