# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary)["key"]
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The Key {error_message} was not found")
# else:
#     content = file.read()
#     print(content)
# # finally:
# #     file.close()
# #     print("File was closed")
# finally:
#     raise TypeError("This is an error that I made up")

#ex2.

height = float(input("Height:"))
weight = int(input("Weight:"))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters")

#ex3.

fruits = ["Apple", "Pear", "Orange"]

#Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + " pie")

make_pie(4)
#ex.4.The code will crash and give you a KeyError. This is because some of the posts in the facebook_posts don't have any "Likes".

facebook_posts = [
    {'Likes': 21, 'Comments': 2}, 
    {'Likes': 13, 'Comments': 2, 'Shares': 1}, 
    {'Likes': 33, 'Comments': 8, 'Shares': 3}, 
    {'Comments': 4, 'Shares': 2}, 
    {'Comments': 1, 'Shares': 1}, 
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        pass



print(total_likes)