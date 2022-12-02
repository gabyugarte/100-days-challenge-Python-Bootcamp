# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
position_list = list(position)
# print(position_list)

first_digit = position_list[0]
second_digit = position_list[1]

if (first_digit == '1') and (second_digit == '1'):
    map[0][0] = 'X'
elif (first_digit == '1') and (second_digit == '2'):
    map[1][0] = 'X'
elif (first_digit == '1') and (second_digit == '3'):
    map[2][0] = 'X'
elif (first_digit == '2') and (second_digit == '1'):
    map[0][1] = 'X'
elif (first_digit == '2') and (second_digit == '2'):
    map[1][1] = 'X'
elif (first_digit == '2') and (second_digit == '3'):
    map[2][1] = 'X'
elif (first_digit == '3') and (second_digit == '1'):
    map[0][2] = 'X'
elif (first_digit == '3') and (second_digit == '2'):
    map[1][2] = 'X'
elif (first_digit == '3') and (second_digit == '3'):
    map[2][2] = 'X'



#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

