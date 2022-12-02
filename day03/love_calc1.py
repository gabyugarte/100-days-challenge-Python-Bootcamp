# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1_to_lower = name1.lower()
name2_to_lower = name2.lower()

count_name1_t = name1_to_lower.count('t')
count_name2_t = name2_to_lower.count('t')
count_name1_r = name1_to_lower.count('r')
count_name2_r = name2_to_lower.count('r')
count_name1_u = name1_to_lower.count('u')
count_name2_u = name2_to_lower.count('u')
count_name1_e = name1_to_lower.count('e')
count_name2_e = name2_to_lower.count('e')

t_occurs = int(count_name1_t) + int(count_name2_t)
r_occurs = int(count_name1_r) + int(count_name2_r)
u_occurs = int(count_name1_u) + int(count_name2_u)
e_occurs = int(count_name1_e) + int(count_name2_e)

first_number = t_occurs + r_occurs + u_occurs + e_occurs

count_name1_l = name1_to_lower.count('l')
count_name2_l = name2_to_lower.count('l')
count_name1_o = name1_to_lower.count('o')
count_name2_o = name2_to_lower.count('o')
count_name1_v = name1_to_lower.count('v')
count_name2_v = name2_to_lower.count('v')
count_name1_e = name1_to_lower.count('e')
count_name2_e = name2_to_lower.count('e')

l_occurs = int(count_name1_l) + int(count_name2_l)
o_occurs = int(count_name1_o) + int(count_name2_o)
v_occurs = int(count_name1_v) + int(count_name2_v)
e_occurs = int(count_name1_e) + int(count_name2_e)

second_number = l_occurs + o_occurs + v_occurs + e_occurs

loveScores_int = int(str(first_number) + str (second_number))
# loveScores_int = int(loveScores)
# print(loveScores_int)
if (loveScores_int < 10) or (loveScores_int > 90):
    print(f"Your score is {loveScores_int}, you go together like coke and mentos.") 
elif (loveScores_int >= 40) and (loveScores_int <= 50):
    print(f"Your score is {loveScores_int}, you are alright together.")
else:
    print(f"Your score is {loveScores_int}.")