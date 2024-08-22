from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 400)

while True:
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    y_positions = [-125, -75, -25, 25, 75, 125]
    all_turtles = []

    is_race_on = False
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
    while user_bet not in colors:
        user_bet = screen.textinput(title="Invalid bet",
                                    prompt="Please select one of the "
                                           "following colors: red, orange, yellow, green, blue, purple.")

    for turtle_index in range(0, 6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.penup()
        new_turtle.goto(x=-225, y=y_positions[turtle_index])
        new_turtle.color(colors[turtle_index])
        all_turtles.append(new_turtle)

    if user_bet:
        is_race_on = True

    message_turtle = Turtle(visible=False)
    message_turtle.penup()
    message_turtle.goto(0, 0)

    while is_race_on:
        for turtle in all_turtles:
            if turtle.xcor() > 230:
                is_race_on = False
                winning_turtle = turtle.pencolor()
                if winning_turtle == user_bet:
                    message_turtle.write("You're the winner!", align='center', font=('Arial', 24, 'normal'))
                else:
                    message_turtle.write("You lose, the winner is: " + winning_turtle, align='center',
                                         font=('Arial', 24, 'normal'))

            new_distance = random.randint(0, 10)
            turtle.forward(new_distance)

    play_again = screen.textinput(title="Play again?", prompt="Do you want to play again? (yes/no): ")
    if play_again != "yes":
        break
    else:
        screen.clearscreen()

screen.exitonclick()
