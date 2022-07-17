from turtle import Turtle, Screen
import pandas
screen = Screen()
turtle = Turtle()

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()

game_on = True
user_answers = []

def get_coors(state_name):
    curr_row = data[data.state == state_name]
    print(curr_row)
    x = int(curr_row["x"])
    y = int(curr_row["y"])
    final = (x, y)
    return final


while game_on:
    score = len(user_answers)
    answer_state = screen.textinput(title=f"{score}/50 States correct", prompt="Enter states here:").title()
    if answer_state in states:
        user_answers.append(answer_state)
        new_turtle = Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()
        new_turtle.goto(get_coors(answer_state))
        new_turtle.write(answer_state, ('Arial', 8, 'normal'))
    if len(user_answers) == 50:
        user_answers = []
        game_on = False





screen.exitonclick()
