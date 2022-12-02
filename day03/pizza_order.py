# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

final_price = 0


if size == 'S':
    final_price += 15
elif size == 'M':
    final_price += 20
else:
    final_price += 25

if add_pepperoni == 'Y':
    if size == 'S':
        final_price += 2
    else:
        final_price += 3
if extra_cheese == 'Y':
    final_price += 1

print(f"Your final bill is: ${final_price}.")
    