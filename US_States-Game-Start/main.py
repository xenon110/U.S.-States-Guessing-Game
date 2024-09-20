import turtle
import pandas as pd
# Set up the screen
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
guessed = []
count = 0

def display_state(name, x, y):
    state_turtle = turtle.Turtle()
    state_turtle.hideturtle()
    state_turtle.penup()
    state_turtle.goto(x, y)
    state_turtle.write(name, align="center")

def close_game():
    screen.bye()

screen.listen()
screen.onkey(close_game, "Escape")

while len(guessed) < 50:
    guess = screen.textinput(f"{count}/50 States Correct", "Guess a state").title()
    if guess in data["state"].values and guess not in guessed:
        guessed.append(guess)
        state_data = data[data["state"] == guess]
        display_state(guess, int(state_data.x), int(state_data.y))
        count += 1
        screen.title(f"{count}/50 States Correct")
turtle.mainloop()

