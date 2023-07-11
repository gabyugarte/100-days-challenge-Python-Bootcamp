from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("lime green")

#draw a square.
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)

# Best way:

# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)
    
#draw a dashed line

for _ in range(15):
    timmy_the_turtle.forward(10)
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(10)
    timmy_the_turtle.pendown()

    
# more colors: https://cs111.wellesley.edu/reference/colors
# more colors: https://trinket.io/docs/colors
# turtle documentation:  https://docs.python.org/3/library/turtle.html


screen = Screen()
screen.exitonclick()
