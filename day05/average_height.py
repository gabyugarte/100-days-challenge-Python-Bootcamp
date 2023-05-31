# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

sum_heights = 0
#Write your code below this row 👇
sum_heights = sum(height for height in student_heights)
len_students = len(student_heights)
average = sum_heights / len_students

print(f'{average:.0f}')


