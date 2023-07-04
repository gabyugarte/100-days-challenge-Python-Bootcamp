class User:
    #constructor of the User class
    #the atributes are the things the objects has
    #Methods are the things the objects does
    def __init__(self, username, user_id):   
        self.username = username
        self.id = user_id
        self.followers = 0
        self.following = 0
        
    #define a method.
    def follow(self, user):
        user.followers += 1
        self.following += 1
        
        

user_1 = User('gaby', '001')
user_2 = User('Jhon', '002')

user_1.follow(user_2)

print(user_1.username, user_1.id, user_1.followers)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
