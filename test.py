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

# draw board
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

# ----- CREATE CUSTOM SHAPES -----

# X shape
Xshape = turtle.Shape("compound")

line1 = ((-20,-5),(20,-5),(20,5),(-20,5))
line2 = ((-5,-20),(5,-20),(5,20),(-5,20))

Xshape.addcomponent(line1,"black","black")
Xshape.addcomponent(line2,"black","black")

screen.register_shape("Xshape",Xshape)

# O shape (circle)
screen.register_shape("Oshape",((0,20),(14,14),(20,0),(14,-14),(0,-20),(-14,-14),(-20,0),(-14,14)))

# stamp turtles
X_turtle = turtle.Turtle()
X_turtle.penup()
X_turtle.hideturtle()
X_turtle.shape("Xshape")

O_turtle = turtle.Turtle()
O_turtle.penup()
O_turtle.hideturtle()
O_turtle.shape("circle")
O_turtle.shapesize(2)

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

def check_win():

    for combo in winning_combos:

        if all(The_Board[pos]=="X" for pos in combo):
            return "X"

        if all(The_Board[pos]=="O" for pos in combo):
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
            X_turtle.goto(px,py)
            X_turtle.stamp()
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