from turtle import Turtle


class State(Turtle):

    def __init__(self,state,position):
        super().__init__()
        self.state = state
        self.position = position
        self.create()

    def create(self):
        self.penup()
        self.hideturtle()
        self.goto(self.position)
        self.write(self.state,align="center",font=("Arial",10,"normal"))