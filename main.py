import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()     #capturing all states in list
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title = f'{len(guessed_states)}/50 Guess the state', prompt = "What's another state's name?").title()
    if answer_state == "Exit":
        # missed_states = []
        # for i in all_states:
        #     if i not in guessed_states:
        #         missed_states.append(i)
        missed_states = [i for i in all_states if i not in guessed_states] # above 4 lines were compressed into 1 line using list compreensions.
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:  # check if answer_state/input is one of 50_US.csv
        guessed_states.append(answer_state)
        tim = turtle.Turtle()    # Create a turtle to write the name of state at the state's x,y coordinates
        tim.hideturtle()
        tim.penup()
        state_data = data[data.state == answer_state]
        tim.goto(int(state_data.x), int(state_data.y))
        tim.write(answer_state)


# states_to_learn.csv



