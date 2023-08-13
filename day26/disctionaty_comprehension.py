#dictionary comprehension
#keyword:
#The basic -> new_dict = {new_key:new_value for item in list}
#complex -> new_dict = {new_key:new_value for (key,value) in dict.items() if test}

import random
names = ["Alex", "Beth", "Caroline", "Dave", "Eleonore", "Freddie"]
students_scores = {student:random.randint(1, 100) for student in names}
print(students_scores)

passed_students = {key:value for (key,value) in students_scores.items() if value >= 60}
print(passed_students)

#Another example:
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word:len(word) for word in sentence.split()}
print(result)

#convert celsius to fahrenheit using dict comprehension

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
weather_f = {day_week:(grades * 9/5) + 32 for (day_week,grades) in weather_c.items()}
print(weather_f)

#Using pandas library
import pandas
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

#loop through rows of a dataframe

for(index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)


