import turtle
import random

print("----Welcome to Snakes and ladders----\nKeypoint to remember look at the TERMINAL to see the number rolled\nEnjoy the game!")

n  = int(input("Enter number of players:- "))
if n > 4:
    n = 4
elif n == 1:
    n = 2    

Players = {}
for i in range(n):
    Player = "Player " + str(i+1)
    Players[Player] = {"Pos":1,"Colour":""}

Players["Player 1"]["Colour"] = "red"
Players["Player 2"]["Colour"] = "blue"
if n >= 3:
    Players["Player 3"]["Colour"] = "yellow"
if n == 4:
    Players["Player 4"]["Colour"] = "green"

screen = turtle.Screen()
screen.setup(1000, 800)
screen.bgcolor("lightblue")

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.penup()

square_size = 50
start_x = -200
start_y = -200

def get_pos(n, start_x, start_y, square_size):
    row = (n - 1) // 10
    col = (n - 1) % 10
    if row % 2 == 1:
        col = 9 - col
    x = start_x + col * square_size + 25
    y = start_y + row * square_size + 25
    return x, y

def draw_board():
    number = 1
    for row in range(10):
        x = start_x if row % 2 == 0 else start_x + (9 * square_size)
        y = start_y + (row * square_size)
        for col in range(10):
            pen.goto(x, y)
            pen.pendown()
            for _ in range(4):
                pen.forward(square_size)
                pen.left(90)
            pen.penup()
            pen.goto(x + 10, y + 10)
            pen.write(number, font=("Arial", 8, "normal"))
            number += 1
            if row % 2 == 0:
                x += square_size
            else:
                x -= square_size

def draw_ladder(a, b):
    x1,y1 = get_pos(a, start_x, start_y, square_size)
    x2,y2 = get_pos(b, start_x, start_y, square_size)
    pen.color("green")
    pen.width(3)
    offset = 20
    pen.goto(x1,y1); pen.pendown(); pen.goto(x2,y2)
    pen.penup(); pen.goto(x1+offset,y1); pen.pendown(); pen.goto(x2+offset,y2)
    for i in range(7):
        t = i/6
        x = x1 + t*(x2-x1)
        y = y1 + t*(y2-y1)
        pen.penup(); pen.goto(x,y); pen.pendown(); pen.goto(x+offset,y)
    pen.penup(); pen.color("black"); pen.width(1)

def draw_snake(a, b):
    x1,y1 = get_pos(a, start_x, start_y, square_size)
    x2,y2 = get_pos(b, start_x, start_y, square_size)
    pen.color("darkgreen")
    pen.width(6)
    steps = 40
    dx = (x2-x1)/steps
    dy = (y2-y1)/steps
    pen.goto(x1,y1); pen.pendown()
    for i in range(steps):
        x = x1 + dx*i
        y = y1 + dy*i + 10*((-1)**i)
        pen.goto(x,y)
    pen.goto(x2,y2)
    pen.penup()
    pen.goto(x1,y1)
    pen.dot(18,"darkgreen")
    pen.goto(x1-5,y1+5); pen.dot(4,"white")
    pen.goto(x1+5,y1+5); pen.dot(4,"white")
    pen.goto(x1-5,y1+5); pen.dot(2,"black")
    pen.goto(x1+5,y1+5); pen.dot(2,"black")
    pen.goto(x1,y1-2); pen.pendown()
    pen.goto(x1-6,y1-10); pen.goto(x1+6,y1-10); pen.goto(x1,y1-2)
    pen.penup(); pen.color("black"); pen.width(1)

ladders = {19:38,31:52,50:70,60:82,80:97}
snakes = {99:87,67:13,63:37,30:7,90:47}

draw_board()
for a,b in ladders.items():
    draw_ladder(a,b)
for a,b in snakes.items():
    draw_snake(a,b)

for name in Players:
    t = turtle.Turtle()
    t.shape("circle")
    t.color(Players[name]["Colour"])
    t.penup()
    Players[name]["T"] = t

def move_step(t, pos):
    x,y = get_pos(pos, start_x, start_y, square_size)
    t.goto(x,y)
    turtle.delay(40)

def move_forward(name, steps):
    for _ in range(steps):
        Players[name]["Pos"] += 1
        move_step(Players[name]["T"], Players[name]["Pos"])

def move_backward(name, steps):
    for _ in range(steps):
        Players[name]["Pos"] -= 1
        move_step(Players[name]["T"], Players[name]["Pos"])

def move_to(name, target):
    while Players[name]["Pos"] != target:
        if Players[name]["Pos"] < target:
            Players[name]["Pos"] += 1
        else:
            Players[name]["Pos"] -= 1
        move_step(Players[name]["T"], Players[name]["Pos"])

def update_positions():
    i = 0
    for name in Players:
        pos = Players[name]["Pos"]
        x, y = get_pos(pos, start_x, start_y, square_size)
        dx = -10 if i % 2 == 0 else 10
        dy = 0 if i < 2 else 10
        Players[name]["T"].goto(x + dx, y + dy)
        i += 1

update_positions()

turn = 1
player_names = list(Players.keys())

while True:
    current = player_names[turn - 1]

    choice = turtle.textinput("Dice Roll", f"{current} roll dice? (Y/N/Q): ")
    if choice is None:
        continue
    choice = choice.upper()

    if choice == "Q":
        break
    if choice == "N":
        continue

    dice = random.randint(1,6)
    print(current,"rolled:",dice)

    move_forward(current, dice)

    if Players[current]["Pos"] > 100:
        extra = Players[current]["Pos"] - 100
        move_backward(current, extra)

    pos = Players[current]["Pos"]

    if pos in ladders:
        print("Ladder!")
        move_to(current, ladders[pos])

    elif pos in snakes:
        print("Snake!")
        move_to(current, snakes[pos])

    if Players[current]["Pos"] == 100:
        print(current,"WINS")
        break

    turn += 1
    if turn > n:
        turn = 1

turtle.done()