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

