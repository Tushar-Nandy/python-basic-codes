import turtle as tl
import pandas as pd

guessed_state=[]
IMAGE="blank_states_img.gif"
screen=tl.Screen()
screen.title("US Map Game")
screen.addshape(IMAGE)
tl.shape(IMAGE)

def capitalize_word(word):
    words=word.split()
    capitalized_word=[w.capitalize() for w in words]
    return " ".join(capitalized_word)

while len(guessed_state) < 50:

    in_word=screen.textinput(title="Guess the State",prompt="What's the name of the State?")
    answer=capitalize_word(in_word)


    state_data= pd.read_csv("50_states.csv")
    # print(state_data)
    # print(answer)
    all_states=state_data.state.to_list()

    if answer=='Exit':
        missed_state=[state for state in all_states if state not in guessed_state]
        # for states in all_states:
        #     if states not in guessed_state:
        #         missed_state.append(states)
        new_data=pd.DataFrame(missed_state)
        new_data.to_csv("states_to_learn.csv")
        break
    elif answer in all_states:
        guessed_state.append(answer)
        turtle=tl.Turtle()
        turtle.hideturtle()
        turtle.penup()
        ans_state=state_data[state_data['state']==answer]
        print(ans_state)
        turtle.goto(ans_state.x.item(),ans_state.y.item())
        turtle.write(answer)
    else:
        print(answer)
        pass
    # def get_mouse_click_coor(x,y):
    #     print(x,y)

    # tl.onscreenclick(get_mouse_click_coor)

  
#states-to_learn.csv


