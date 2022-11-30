print("Wellcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
total_people = int(input("How many people to split the bill? "))

tip_percentage = bill * percentage /100
total_inc_tip = bill + tip_percentage
total_per_person = total_inc_tip / total_people

print(f"each person should pay: ${total_per_person:.2f}")