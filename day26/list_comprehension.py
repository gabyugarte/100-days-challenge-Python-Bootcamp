#List Comprehension
#new_list = [new_item for item in list]

numbers = [1, 2, 3] 
new_num = [n + 1 for n in numbers]
print(new_num)

#We could also use in variables holding strings as list
name = "Gabriela"
letters_list = [l for l in name]
print(letters_list)

#Using range as list

numbers = range(1, 5)
range_list = [n * 2 for n in numbers]
print(range_list)

#Conditional list comprehension
#new_list = [new_item for item in list if test]

names = ["Alex", "Beth", "Caroline", "Dave", "Eleonore", "Freddie"]
new_names_list = [name.upper() for name in names if len(name) >= 5]
print(new_names_list)

# Create a list of numbers 0 to 99
my_list = [x for x in range(100)]

# Create a list of square numbers from 0^2 to 99^2
my_list_1 = [x*x for x in range(100)]

# Create a list of even numbers less than 100
my_list_2 = [x for x in range(100) if x % 2 == 0]

# Do the same thing by using a different version of range
my_list_3 = [x for x in range(0, 101, 2)]

# Create a list of words that have an 'E'
my_words = ['CAKE', 'DOG', 'APPLE']
words_with_e = [word for word in my_words if 'E' in word]

# Find all leap years between 1900 and 2000
# Multiples of 4 are leap years
# Except, Multiples of 100 are not leap years
# Except, Multiples of 400 are leap years
leap_years = [year for year in range(1900, 2001) if (year % 400 == 0) or
					(year % 100 != 0 and year % 4 == 0)]
print(my_list)
print(my_list_1)
print(my_list_2)
print(my_list_3)
print(words_with_e)
print(leap_years)
