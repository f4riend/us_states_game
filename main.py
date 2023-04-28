from state import State
import turtle
import pandas


canvas = turtle.Screen()
canvas.title("US STATES GAME")

usMap = "blank_states_img.gif"
canvas.addshape(usMap)
turtle.shape(usMap)


data = pandas.read_csv("50_states.csv")


allStates = data.state.to_list()
guessed = []


while len(guessed) < 50:
    user = canvas.textinput(title=f"{len(guessed)}/50 States Correct",prompt="What's another state name ?").title().strip()
    if user == "Exit":
        missings = [state for state in allStates if state not in guessed]
        learned = pandas.DataFrame(missings)
        learned.to_csv("states_to_learn.csv")
        break
    
    if user in allStates:
        guessed.append(user)
        stateData = data[data.state ==  user]
        state = State(state=user.title(),position=(int(stateData.x),int(stateData.y)))