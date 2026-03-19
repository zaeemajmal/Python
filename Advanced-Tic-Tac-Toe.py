import turtle

# setup screen
screen = turtle.Screen()
screen.bgcolor("orange")
screen.setup(400,400)

print("-----Welcome to Tic-Tac-Toe-----")

The_Board = {
"A1":"", "A2":"", "A3":"",
"B1":"", "B2":"", "B3":"",
"C1":"", "C2":"", "C3":""
}

# draw grid
Board = turtle.Turtle()
Board.speed(0)
Board.penup()
Board.hideturtle()
Board.pensize(5)

for x in [-50,50]:
    Board.goto(x,150)
    Board.pendown()
    Board.goto(x,-150)
    Board.penup()

for y in [50,-50]:
    Board.goto(-150,y)
    Board.pendown()
    Board.goto(150,y)
    Board.penup()

positions = {
"A1":(-100,100),"A2":(0,100),"A3":(100,100),
"B1":(-100,0),"B2":(0,0),"B3":(100,0),
"C1":(-100,-100),"C2":(0,-100),"C3":(100,-100)
}

# X drawer
X_draw = turtle.Turtle()
X_draw.hideturtle()
X_draw.pensize(5)

def draw_X(x,y):
    X_draw.penup()
    X_draw.goto(x-20,y-20)
    X_draw.pendown()
    X_draw.goto(x+20,y+20)

    X_draw.penup()
    X_draw.goto(x-20,y+20)
    X_draw.pendown()
    X_draw.goto(x+20,y-20)

# O turtle
O_turtle = turtle.Turtle()
O_turtle.penup()
O_turtle.hideturtle()
O_turtle.shape("circle")
O_turtle.shapesize(2)

# ✅ MESSAGE TURTLE (FIXED)
Msg = turtle.Turtle()
Msg.hideturtle()
Msg.penup()

def show_message(text):
    Msg.clear()
    Msg.goto(0,160)   # 👈 always visible top
    Msg.write(text, align="center", font=("Arial",16,"bold"))

# win line
WinLine = turtle.Turtle()
WinLine.hideturtle()
WinLine.pensize(10)
WinLine.color("red")

player = "X"

winning_combos = [
("A1","A2","A3"),
("B1","B2","B3"),
("C1","C2","C3"),
("A1","B1","C1"),
("A2","B2","C2"),
("A3","B3","C3"),
("A1","B2","C3"),
("A3","B2","C1")
]

def draw_win_line(combo):
    start = positions[combo[0]]
    end = positions[combo[2]]

    WinLine.penup()
    WinLine.goto(start)
    WinLine.pendown()
    WinLine.goto(end)

def check_win():
    for combo in winning_combos:

        if all(The_Board[pos] == "X" for pos in combo):
            draw_win_line(combo)
            return "X"

        if all(The_Board[pos] == "O" for pos in combo):
            draw_win_line(combo)
            return "O"

    return None

# GAME LOOP
while "" in The_Board.values():

    move = screen.textinput("Move", player + " enter A1-C3")

    if move is None:
        continue

    move = move.upper()

    # ❌ invalid input
    if move not in The_Board:
        show_message("Invalid move! Use A1-C3")
        continue

    # ❌ already filled
    if The_Board[move] != "":
        show_message("Place already filled!")
        continue

    # ✅ valid move
    show_message("")  # clear message
    The_Board[move] = player

    x,y = positions[move]

    if player == "X":
        draw_X(x,y)
    else:
        O_turtle.goto(x,y)
        O_turtle.stamp()

    winner = check_win()

    if winner:
        show_message(winner + " WINS!")
        print(winner, "wins!")
        break

    player = "O" if player=="X" else "X"

# draw
if "" not in The_Board.values() and not check_win():
    show_message("DRAW!")
    print("Draw!")

turtle.done()