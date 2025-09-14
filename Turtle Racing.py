import turtle
import time
import random

width, height = 500, 500
COLORS = ['red', 'blue', 'green', 'orange', 'purple', 'yellow', 'black', 'brown', 'pink', 'cyan']

def get_number_of_racers():
    while True:
        racers = input('Enter the number of racers (2-10): ')
        if racers.isdigit():
            racers = int(racers)
        else:
            print('Input is not numeric... Try again!')
            continue
        if 2 <= racers <= 10:
            return racers
        else:
            print('Number is not in range 2-10. Try again!')

def init_turtle():
    screen = turtle.Screen()
    screen.setup(width, height)
    screen.title('Turtle Racing!')

def create_turtles(colors):
    turtles = []
    spacing_x = width // (len(colors) + 1)
    start_y = -height // 2 + 20
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.penup()
        racer.setheading(90)
        racer.setpos(-width // 2 + (i + 1) * spacing_x, start_y)
        racer.pendown()
        turtles.append(racer)
    return turtles

def race(colors):
    turtles = create_turtles(colors)
    while True:
        for i, racer in enumerate(turtles):
            distance = random.randint(1, 20)
            racer.forward(distance)
            x, y = racer.pos()
            if y >= height // 2 - 10:
                return colors[i]

racers = get_number_of_racers()
init_turtle()
random.shuffle(COLORS)
colors = COLORS[:racers]
winner = race(colors)
print(f"The winner is: {winner}")
turtle.done()
