print("Welcome to Tic-Tac-Toe")
The_Board = {"A1": "" , "A2" : "" , "A3" : "",
            "B1" : "" , "B2" : "" , "B3" : "",
            "C1" : "" , "C2" : "" , "C3" : ""}
Board_Keys = []
for Key in The_Board:
    Board_Keys.append(Key)
#print(Board_Keys)   
def Current_Board(X): 
    print(X["A1"]+"  |  "+X["A2"]+"|  "+X["A3"])
    print("--+--+--")
    print(X["B1"]+"  |  "+X["B2"]+"|  "+X["B3"])
    print("--+--+--")
    print(X["C1"]+"  |  "+X["C2"]+"|  "+X["C3"])
Current_Board(The_Board)    
def game():
    Turn = "X"
    Count = 0

    for i in range(10):
        Current_Board(The_Board)
        print("It's your turn," + Turn + "  Move to which square?")
        move = input()
        if The_Board[move] == "":
            The_Board[move] = Turn
            Count += 1
        else:
            print("That place is already filled\nMove to which square?")
            continue
        if Count >= 5:
            if The_Board["A1"]  == The_Board["A2"] == The_Board["A3"] != "":
                Current_Board(The_Board)
                print("\nGame Over\n")
                print("----" + Turn + "Won----")
                break

            elif The_Board["B1"]  == The_Board["B2"] == The_Board["B3"] != "":
                Current_Board(The_Board)
                print("\nGame Over\n")
                print("----" + Turn + "Won----")
                break
            elif The_Board["C1"]  == The_Board["C2"] == The_Board["C3"] != "":
                Current_Board(The_Board)
                print("\nGame Over\n")
                print("----" + Turn + "Won----")
                break

            elif The_Board["A1"]  == The_Board["B1"] == The_Board["C1"] != "":
                Current_Board(The_Board)
                print("\nGame Over\n")
                print("----" + Turn + "Won----")
                break
            elif The_Board["A2"]  == The_Board["B2"] == The_Board["C2"] != "":
                Current_Board(The_Board)
                print("\nGame Over\n")
                print("----" + Turn + "Won----")
                break

            elif The_Board["A3"]  == The_Board["B3"] == The_Board["C3"] != "":
                Current_Board(The_Board)
                print("\nGame Over\n")
                print("----" + Turn + "Won----")
                break
            elif The_Board["A1"]  == The_Board["B2"] == The_Board["C3"] != "":
                Current_Board(The_Board)
                print("\nGame Over\n")
                print("----" + Turn + "Won----")
                break

            elif The_Board["A3"]  == The_Board["B2"] == The_Board["C1"] != "":
                Current_Board(The_Board)
                print("\nGame Over\n")
                print("----" + Turn + "Won----")
                break
        if Count == 9:
            print("\nGame Over\n")
            print("----It's a Tie")
        if Turn == "X":
            Turn = "O"
        else:
            Turn = "X"
    restart  = input("Do you want to play again? (Y/N)")  

    if restart == "Y" or restart == "y":
        for key in The_Board:
            The_Board[key] = ""
        game()
#if __name__ == "_main_":
game()






