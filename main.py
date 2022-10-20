from turtle import Screen
import pandas
from place_state import StateText
import time

data = pandas.read_csv("50_states.csv")
states_list = data.state

tv = Screen()
tv.tracer(0)
tv.setup(width=800, height=600)
tv.bgpic(picname="us_map.png")

tiny_states = ["West Virginia", "Vermont", "New Hampshire", "Massachusetts", "Rhode Island",
               "Connecticut", "New Jersey", "Delaware", "Maryland", "Mississippi", "South Carolina"]

game_on = True
while game_on:
    response = tv.textinput("50 US States", "Name a state: ").title()
    time.sleep(.2)
    tv.update()
    if response is None:
        game_on = False
    for state in states_list:
        writer = StateText()
        if state == response:
            if state in tiny_states:
                writer.draw_line(state)
            row = data[data.state == response]
            x = int(row.x)
            y = int(row.y)
            writer.set_text(state, x, y)
        else:
            pass

tv.exitonclick()
