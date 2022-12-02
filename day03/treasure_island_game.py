print('''
                  ,-'`\               ,    [_________________]
                ,'   ,-`\            / \  /|                 \
               (    |` ,`-,         _|_|_,-,                 |
                \  (`    `,     _,.,'  / / \                 |
                 \ )`'   ',' ,-'   \,_/ (   )               /
                  `\_   -|_,')    ,/     `-'      |         |
                 ,-[__>-'     ._,'        /       \         |
               ,'/           ,/          |         \        |
            _,' /         ,-'            |        / \       |
          ,'/  /           |             |        |  |      |
         (   ,/|          /              |        |  |      |
      ,-'\_,/ /          '|              /        /  |      |
    ,/|,-'    |--,.'`-,--'               (       /   |      |
    '-/'      |         /                 \     / \  |      |
               \       \                   \      \  |      |
              / `.     _\                   \      \ |      |
             /    \-    `\                   \      \|      |
            /     /\      )                   \      |      |
           /     / /     /                     \     |      |**************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
# Arte código Ascii
# https://ascii.co.uk/art
#Write your code below this line 👇

direction = input(
    "You\'re at crossroad, Where would you like to go?: 'L' for left or 'R' for right?").upper()

if direction == 'L':
    action = input("You've come to a lake. There is an island in the middle of the lake. Do you want to swim across? (Type -> swim) or wait for a boat (Type -> wait)?").lower()
    if action == 'wait':
        door_option = input(
            "You arrive at the island unharmed. There is a house with 3 doors. Which door would you choose: type -> red, yellow or blue?").lower()
        if door_option == "yellow":
            print("Congrats, you won")
        elif door_option == "red":
            print("Burned by fire")
        elif door_option == "blue":
            print("Eaten by beasts. Game over!")
        else:
            print("Game Over!")
    else:
        print("Attacked by trout. Game over")

else:
    print("Fall into a hole. Game Over")
