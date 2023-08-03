#Opens a file and save it in a variable called file
# file = open("my_file.txt")
# #reads the file 
# contents = file.read()
# print(contents)
# file.close()

#Here is a different way to do this and forget about the close()
#Read a file
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)
    
# #Relative Path
# with open("../../../../../../Desktop/my_file.txt") as file:
#     contents = file.read()
#     print(contents)
    
#Absolute Path
with open("/Users/Gaby/Desktop/my_file.txt") as file:
    contents = file.read()
    print(contents)

#write a file: mode = "w" -> write, mode = "a" -> append, mode = "r" -> read
# with open("my_file.txt", mode="a") as file:
#     file.write("\nnew Text.")

# #Create a new file:
# #mode = "w" -> write, also creates a new file
# with open("new_file.txt", mode="w") as new_file:
#     new_file.write("hello world")
    