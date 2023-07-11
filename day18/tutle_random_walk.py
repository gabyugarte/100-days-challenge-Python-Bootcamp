import turtle as t
import random

timy = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    #save the rgb color into a TUPLE, inmutable
    r_color = (r, g, b)
    return r_color

# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
timy.pensize(15)
timy.speed("fastest")

for _ in range(200):
    timy.color(random_color())    
    timy.forward(30)
    timy.setheading(random.choice(directions))
    