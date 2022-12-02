# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma\. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# len_names = len(names)
# random_name = random.randint(0, len_names -1)
# pay_bill = names[random_name]
pay_bill = random.choice(names)
print(f"{pay_bill} is going to buy the meal today!")