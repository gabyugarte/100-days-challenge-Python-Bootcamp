from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
# all turtle size are 20 x 20, we stretch them by 5 and 1 to hace 100 x 20
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(position)


    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
    
    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
        
        