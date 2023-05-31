# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# print(student_heights)
# 🚨 Don't change the code above 👆

sum_heights = 0
#Write your code below this row 👇
for height in student_heights:
    sum_heights += height
# print(sum_heights)
# for counter in student_heights:
num_of_students = 0

for student in student_heights:
    num_of_students += 1
# print(num_of_students)

average = round(sum_heights / num_of_students)
print(average)
