import turtle
import random
print("Welcome to snakes and ladders\nInstruction to remember:-\n Look at the console to see how what number you rolled\nEnjoy the game! ")

n  = int(input("Enter number of players:- "))
if n > 4 : 
    print("Max Limit 4")
    n = 4
elif n == 1:
    print("Minimum number 2")
    n = 2    
else:
    pass
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
turtle.hideturtle()
pen = turtle.Turtle()
pen.speed(100)
pen.penup()

def get_pos(n, start_x, start_y, square_size):
    row = (n - 1) // 10
    col = (n - 1) % 10

    if row % 2 == 1:
        col = 9 - col

    x = start_x + col * square_size + 25
    y = start_y + row * square_size + 25

    return x, y


def draw_ladder(x1, y1, x2, y2):
    pen.color("green")
    pen.width(3)

    offset = 20
    pen.penup()
    pen.goto(x1, y1)
    pen.pendown()
    pen.goto(x2, y2)

    pen.penup()
    pen.goto(x1 + offset, y1)
    pen.pendown()
    pen.goto(x2 + offset, y2)

    steps = 6
    for i in range(steps + 1):
        t = i / steps
        x = x1 + t * (x2 - x1)
        y = y1 + t * (y2 - y1)

        pen.penup()
        pen.goto(x, y)
        pen.pendown()
        pen.goto(x + offset, y)

    pen.penup()
    pen.color("black")
    pen.width(1)


def draw_snake(x1, y1, x2, y2):
    pen.penup()
    pen.goto(x1, y1)
    pen.pendown()

    pen.color("red")
    pen.width(4)

    steps = 20
    dx = (x2 - x1) / steps
    dy = (y2 - y1) / steps

    for i in range(steps):
        pen.goto(x1 + dx * i, y1 + dy * i)

        if i % 2 == 0:
            pen.left(30)
        else:
            pen.right(30)

    pen.goto(x2, y2)

    pen.penup()
    pen.goto(x1, y1)
    pen.dot(12, "black")

    pen.penup()
    pen.color("black")
    pen.width(1)

square_size = 50
start_x = -200
start_y = -200
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

    x1, y1 = get_pos(19, start_x, start_y, square_size)
    x2, y2 = get_pos(38, start_x, start_y, square_size)
    draw_ladder(x1, y1, x2, y2)
    
    x1, y1 = get_pos(31, start_x, start_y, square_size)
    x2, y2 = get_pos(52, start_x, start_y, square_size)
    draw_ladder(x1, y1, x2, y2)

    x1, y1 = get_pos(35, start_x, start_y, square_size)
    x2, y2 = get_pos(65, start_x, start_y, square_size)
    draw_ladder(x1, y1, x2, y2)

    x1, y1 = get_pos(80, start_x, start_y, square_size)
    x2, y2 = get_pos(97, start_x, start_y, square_size)
    draw_ladder(x1, y1, x2, y2)

    x1, y1 = get_pos(50, start_x, start_y, square_size)
    x2, y2 = get_pos(70, start_x, start_y, square_size)
    draw_ladder(x1, y1, x2, y2)

    x1, y1 = get_pos(3, start_x, start_y, square_size)
    x2, y2 = get_pos(25, start_x, start_y, square_size)
    draw_ladder(x1, y1, x2, y2)

    x1, y1 = get_pos(42, start_x, start_y, square_size)
    x2, y2 = get_pos(61, start_x, start_y, square_size)
    draw_ladder(x1, y1, x2, y2)

    x1, y1 = get_pos(99, start_x, start_y, square_size)
    x2, y2 = get_pos(87, start_x, start_y, square_size)
    draw_snake(x1, y1, x2, y2)

    x1, y1 = get_pos(67, start_x, start_y, square_size)
    x2, y2 = get_pos(13, start_x, start_y, square_size)
    draw_snake(x1, y1, x2, y2)

    x1, y1 = get_pos(63, start_x, start_y, square_size)
    x2, y2 = get_pos(37, start_x, start_y, square_size)
    draw_snake(x1, y1, x2, y2)

    x1, y1 = get_pos(30, start_x, start_y, square_size)
    x2, y2 = get_pos(7, start_x, start_y, square_size)
    draw_snake(x1, y1, x2, y2)

    x1, y1 = get_pos(90, start_x, start_y, square_size)
    x2, y2 = get_pos(47, start_x, start_y, square_size)
    draw_snake(x1, y1, x2, y2)
draw_board()

for name in Players:
    t = turtle.Turtle()
    t.shape("circle")
    t.color(Players[name]["Colour"])
    t.penup()
    Players[name]["T"] = t


def update_positions():
    i = 0
    for name in Players:
        pos = Players[name]["Pos"]
        if pos == 0:
            pos = 1

        x, y = get_pos(pos, start_x, start_y, square_size)

        dx = -10 if i % 2 == 0 else 10
        dy = 0 if i < 2 else 10

        Players[name]["T"].goto(x + dx, y + dy)
        i += 1


turn = 1
player_names = list(Players.keys())
update_positions()
while True:
    current = player_names[turn - 1]
    choice = turtle.textinput("Dice Roll", f"{current} roll dice? (Y/N/Q): ")

    if choice is None:
       continue

    choice = choice.upper()

    if choice == "Q":
        print("Game Ended")
        exit()

    if choice == "N":
        continue

    if choice == "Y":
        dice = random.randint(1, 6)
        print(current, "rolled:", dice)

        Players[current]["Pos"] += dice

        if Players[current]["Pos"] > 100:
            Players[current]["Pos"] -= dice 

        ladders = {19:38, 31:52, 50:70, 60:82, 80:97}
        snakes = {99:87, 67:13, 63:37, 30:7, 90:47}

        pos = Players[current]["Pos"]

        if pos in ladders:
            print("Ladder!")
            Players[current]["Pos"] = ladders[pos]

        elif pos in snakes:
            print("Snake!")
            Players[current]["Pos"] = snakes[pos]

        update_positions()

        if Players[current]["Pos"] == 100:
            print(current, "WINS")
            break

        turn += 1
        if turn > n:
            turn = 1

    else:
        print("Invalid input! Enter Y, N or Q")        
turtle.done()