import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S STATES GAME")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

#code to get the coordinates for each state:
# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
#All of the results are saved in the 50_states.csv file

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What`s another state name?").title()
    
    if answer_state == "Exit":
        #List comprehension
        missing_states = [state for state in all_states if state not in guessed_states]
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        #if they got right create a new turtle
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        #create a turtle to write the name of the state at the coordinates in the map
        t.write(answer_state)
        



screen.exitonclick()