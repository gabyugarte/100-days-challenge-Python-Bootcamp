#Write your code below this row 👇
counter = 0
for number in range(2, 101, 2):
    counter += number
print(counter)

# ex.2 

counter2 = 0
for number in range(1, 101):
    if number % 2 == 0:
        counter2 += number
print(counter2)