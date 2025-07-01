from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='make your bet', prompt='which turtle will win the race')
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
coordinate = [[100,-230], [50,-230], [0,-230], [-50,-230], [-100,-230], [-150,-230]]
all_turtle = []

for i in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(y=coordinate[i][0], x=coordinate[i][1])
    all_turtle.append(new_turtle)

is_race_on = False
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you're win 🏆, the {winning_color} turtle is the winner!")
            else:
                print(f"you're lost 😔, the {winning_color} turtle is the winner!")
            break  # Add this line to exit the for loop once we have a winner
        random_dis = random.randint(0,10)
        turtle.forward(random_dis)

screen.exitonclick()