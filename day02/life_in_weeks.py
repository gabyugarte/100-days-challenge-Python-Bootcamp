# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

age_as_int = int(age)
days_remaining = 90 - age_as_int
days = days_remaining * 365
weeks = days_remaining * 52
months = days_remaining * 12

message = f"You have {days} days, {weeks} weeks, and {months} months left."
print (message)