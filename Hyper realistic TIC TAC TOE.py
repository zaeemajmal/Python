import turtle

screen = turtle.Screen()
screen.bgcolor("orange")
screen.setup(300,300)

print("-----Welcome to Tic-Tac-Toe-----")

The_Board = {
"A1":"", "A2":"", "A3":"",
"B1":"", "B2":"", "B3":"",
"C1":"", "C2":"", "C3":""
}

Board = turtle.Turtle()
Board.speed(0)
Board.penup()
Board.hideturtle()
Board.pensize(5)

# draw grid
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

# turtle for drawing X
X_draw = turtle.Turtle()
X_draw.hideturtle()
X_draw.pensize(5)

# turtle for O
O_turtle = turtle.Turtle()
O_turtle.penup()
O_turtle.hideturtle()
O_turtle.shape("circle")
O_turtle.shapesize(2)

# turtle for win line
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

def draw_X(x,y):

    X_draw.penup()
    X_draw.goto(x-20,y-20)
    X_draw.pendown()
    X_draw.goto(x+20,y+20)

    X_draw.penup()
    X_draw.goto(x-20,y+20)
    X_draw.pendown()
    X_draw.goto(x+20,y-20)


def draw_win_line(combo):

    start = positions[combo[0]]
    end = positions[combo[2]]

    WinLine.penup()
    WinLine.goto(start)
    WinLine.pendown()
    WinLine.goto(end)


def check_win():

    for combo in winning_combos:

        if all(The_Board[pos]=="X" for pos in combo):
            draw_win_line(combo)
            return "X"

        if all(The_Board[pos]=="O" for pos in combo):
            draw_win_line(combo)
            return "O"

    return None


def get_square(x,y):

    if y > 50:
        row = "A"
    elif y > -50:
        row = "B"
    else:
        row = "C"

    if x < -50:
        col = "1"
    elif x < 50:
        col = "2"
    else:
        col = "3"

    return row+col


def click(x,y):

    global player

    square = get_square(x,y)

    if square in The_Board and The_Board[square] == "":

        The_Board[square] = player
        px,py = positions[square]

        if player == "X":
            draw_X(px,py)
        else:
            O_turtle.goto(px,py)
            O_turtle.stamp()

        winner = check_win()

        if winner:
            print(winner,"wins!")
            screen.onclick(None)
            return

        if "" not in The_Board.values():
            print("Draw!")
            screen.onclick(None)
            return

        player = "O" if player=="X" else "X"


screen.onclick(click)

turtle.done()