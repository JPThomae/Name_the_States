from turtle import Turtle

STATE_COORDS = {
    "West Virginia": [[230, 100], [237, 0]], "Vermont": [[240, 185], [325, 130]],
    "New Hampshire": [[280, 200], [340, 130]], "Massachusetts": [[283, 250], [340, 98]],
    "Rhode Island": [[355, 43], [349, 90]], "Connecticut": [[327, 26], [339, 87]],
    "New Jersey": [[315, 46], [327, 12]], "Delaware": [[308, 31], [327, -3]],
    "Maryland": [[290, 30], [327, -18]], "Mississippi": [[120, -120], [175, -185]],
    "South Carolina": [[255, -75], [280, -90]]
}


class StateText(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.pensize(1.5)
        self.hideturtle()
        self.color("black")

    def set_text(self, text, x_coord, y_coord):
        self.goto(x_coord, y_coord)
        self.write(text)

    def draw_line(self, state):
        print(STATE_COORDS[state][0])
        print(STATE_COORDS[state][1])
        self.goto(STATE_COORDS[state][0])
        self.pendown()
        self.goto(STATE_COORDS[state][1])
        self.penup()
