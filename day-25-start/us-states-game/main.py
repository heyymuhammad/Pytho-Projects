import turtle, pandas

screen = turtle.Screen()
screen.title("U.S States Game")
map_image = "map.gif"
screen.addshape(map_image)
turtle.shape(map_image)

## method to find x and y on map
# def get_mouse_click_coor(x,y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

data = pandas.read_csv("50_states.csv")

all_states = data.state.to_list()
guessed_answer = []
remaining_answer = []
while len(guessed_answer) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_answer)}/50 States Correct", 
                                    prompt="What's another states name?").title()
    if answer_state == "Exit":
        missing_states = [item for item in all_states if item not in guessed_answer]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_know.csv")
    if answer_state in all_states:
        guessed_answer.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state = data[data.state == answer_state]
        t.goto(int(state.x), int(state.y))
        t.write(answer_state, font=["Serif",8])
        
        
