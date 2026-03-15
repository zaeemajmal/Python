import random
import math
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk

print("Welcome to Cricket Scorer App")

team_name1=input("Enter Team 1 name: ")
team_name2=input("Enter Team 2 name: ")

T1={}
T2={}

T1_list=[]
T2_list=[]

print("Enter 11 players of",team_name1)
for i in range(11):
    name=input()
    T1[name]={"Runs":0,"Balls":0,"How Out":"Not Out"}
    T1_list.append(name)

print("Enter 11 players of",team_name2)
for i in range(11):
    name=input()
    T2[name]={"Runs":0,"Balls":0,"How Out":"Not Out"}
    T2_list.append(name)

print("Match Type")
match_type=input("T20 / ODI / Custom : ")

if match_type=="T20":
    total_overs=20
elif match_type=="ODI":
    total_overs=50
else:
    total_overs=int(input("Enter overs: "))

toss=input("Who won toss (T1/T2): ")

if toss=="T1":
    choice=input("Team1 Bat/Bowl: ")
    if choice=="Bat":
        batting=T1
        bowling=T2
        batting_list=T1_list
        bowling_list=T2_list
    else:
        batting=T2
        bowling=T1
        batting_list=T2_list
        bowling_list=T1_list
else:
    choice=input("Team2 Bat/Bowl: ")
    if choice=="Bat":
        batting=T2
        bowling=T1
        batting_list=T2_list
        bowling_list=T1_list
    else:
        batting=T1
        bowling=T2
        batting_list=T1_list
        bowling_list=T2_list

bowling_stats={}
for p in T1_list+T2_list:
    bowling_stats[p]={"Runs":0,"Balls":0,"Wkts":0}

extras={"wd":0,"nb":0,"b":0,"lb":0}

runs=0
wkts=0
balls=0

fall_of_wickets=[]
over_summary=[]
current_over_runs=0

partnership_runs=0
partnership_balls=0
partnerships=[]

commentary=[]

shots=[]

striker=batting_list[0]
non_striker=batting_list[1]
next_batsman=2

last_wicket="None"

print("First Innings Start")

while balls<total_overs*6 and wkts<10:

    bowler=input("Bowler: ")
    event=input("Ball result: ")

    over=str(balls//6)+"."+str(balls%6+1)

    if event in ["0","1","2","3","4","6"]:

        r=int(event)

        runs+=r
        balls+=1
        current_over_runs+=r

        batting[striker]["Runs"]+=r
        batting[striker]["Balls"]+=1

        bowling_stats[bowler]["Runs"]+=r
        bowling_stats[bowler]["Balls"]+=1

        partnership_runs+=r
        partnership_balls+=1

        angle=random.randint(0,360)
        power=random.randint(30,80)
        shots.append((angle,power,r))

        commentary.append(bowler+" to "+striker+" "+event+" runs")

        print(over,bowler,"to",striker,"-",r)

        if r%2==1:
            striker,non_striker=non_striker,striker

    elif event.startswith("wd"):

        r=int(event[2:])
        runs+=1+r
        extras["wd"]+=1+r
        current_over_runs+=1+r
        bowling_stats[bowler]["Runs"]+=1+r

        commentary.append("Wide ball")

    elif event.startswith("nb"):

        r=int(event[2:])
        runs+=1+r
        extras["nb"]+=1
        current_over_runs+=1+r
        bowling_stats[bowler]["Runs"]+=1+r
        batting[striker]["Runs"]+=r

    elif event.startswith("b"):

        r=int(event[1:])
        runs+=r
        extras["b"]+=r
        balls+=1
        current_over_runs+=r
        bowling_stats[bowler]["Balls"]+=1

    elif event.startswith("lb"):

        r=int(event[2:])
        runs+=r
        extras["lb"]+=r
        balls+=1
        current_over_runs+=r
        bowling_stats[bowler]["Balls"]+=1

    elif event=="w":

        balls+=1
        wkts+=1

        bowling_stats[bowler]["Balls"]+=1
        bowling_stats[bowler]["Wkts"]+=1

        how=input("bowled/lbw/runout/hitwicket/catch: ")

        if how=="bowled":
            out_text="b "+bowler
        elif how=="lbw":
            out_text="lbw b "+bowler
        elif how=="runout":
            fielder=input("Fielder: ")
            out_text="run out ("+fielder+")"
        elif how=="hitwicket":
            out_text="hit wicket b "+bowler
        elif how=="catch":
            catcher=input("Catcher: ")
            out_text="c "+catcher+" b "+bowler

        batting[striker]["How Out"]=out_text

        last_wicket=striker+" "+out_text

        fow=str(runs)+"-"+str(wkts)
        fall_of_wickets.append(fow)

        text=striker+" partnership "+str(partnership_runs)+" runs"
        partnerships.append(text)

        partnership_runs=0
        partnership_balls=0

        if next_batsman<11:
            striker=batting_list[next_batsman]
            next_batsman+=1

    if balls%6==0 and balls!=0:

        over_no=balls//6
        over_summary.append(str(over_no)+" : "+str(current_over_runs)+" runs")
        current_over_runs=0
        striker,non_striker=non_striker,striker

    if balls>0:
        rr=round(runs/(balls/6),2)
    else:
        rr=0

    print("Score:",runs,"/",wkts,"(",balls//6,".",balls%6,")")
    print("Run Rate:",rr)

print("First innings finished")

target=runs+1

batting,bowling=bowling,batting
batting_list,bowling_list=bowling_list,batting_list

runs2=0
wkts2=0
balls2=0

striker=batting_list[0]
non_striker=batting_list[1]
next_batsman=2

print("Target:",target)

while balls2<total_overs*6 and wkts2<10 and runs2<target:

    event=input("Ball result: ")

    if event in ["0","1","2","3","4","6"]:

        r=int(event)

        runs2+=r
        balls2+=1

        batting[striker]["Runs"]+=r
        batting[striker]["Balls"]+=1

        if r%2==1:
            striker,non_striker=non_striker,striker

    elif event=="w":

        balls2+=1
        wkts2+=1

        if next_batsman<11:
            striker=batting_list[next_batsman]
            next_batsman+=1

    balls_left=total_overs*6-balls2
    runs_left=target-runs2

    if balls_left>0:
        rrr=round(runs_left/(balls_left/6),2)
    else:
        rrr=0

    win_prob=min(100,round((runs2/target)*100,1))

    print("Score:",runs2,"/",wkts2)
    print("Need",runs_left,"from",balls_left)
    print("RRR:",rrr)
    print("AI Win Probability:",win_prob,"%")

print("FINAL SCORECARD")

print(team_name1)
print("Batsman        How Out            R   B   SR")

for p in T1:

    r=T1[p]["Runs"]
    b=T1[p]["Balls"]

    if b>0:
        sr=round((r/b)*100,2)
    else:
        sr=0

    print(p.ljust(15),T1[p]["How Out"].ljust(18),r,b,sr)

print("Extras:",extras)

print("Fall of Wickets")
for f in fall_of_wickets:
    print(f)

print("Partnerships")
for p in partnerships:
    print(p)

print("Over Summary")
for o in over_summary:
    print(o)

print("Bowling Stats")

for b in bowling_stats:

    balls_b=bowling_stats[b]["Balls"]
    runs_b=bowling_stats[b]["Runs"]
    wkts_b=bowling_stats[b]["Wkts"]

    if balls_b>0:
        eco=round(runs_b/(balls_b/6),2)
    else:
        eco=0

    print(b,"Overs:",balls_b//6,".",balls_b%6,"Runs:",runs_b,"Wkts:",wkts_b,"Eco:",eco)

def run_worm():

    runs_progress=[]
    total=0

    for o in over_summary:
        r=int(o.split(":")[1].split()[0])
        total+=r
        runs_progress.append(total)

    plt.plot(runs_progress)
    plt.title("Run Worm")
    plt.show()

def manhattan():

    runs_per_over=[]
    for o in over_summary:
        r=int(o.split(":")[1].split()[0])
        runs_per_over.append(r)

    plt.bar(range(1,len(runs_per_over)+1),runs_per_over)
    plt.title("Manhattan Chart")
    plt.show()

def wagon_wheel():

    ax=plt.subplot(111,polar=True)

    for angle,power,r in shots:

        a=math.radians(angle)

        if r==6:
            c="red"
        elif r==4:
            c="green"
        else:
            c="blue"

        ax.scatter(a,power,c=c)

    plt.title("Wagon Wheel")
    plt.show()

def hawkeye():

    v=random.uniform(25,40)
    angle=random.uniform(20,45)

    g=9.8

    x=[]
    y=[]

    for t in np.linspace(0,5,100):

        X=v*math.cos(math.radians(angle))*t
        Y=v*math.sin(math.radians(angle))*t-0.5*g*t*t

        if Y<0:
            break

        x.append(X)
        y.append(Y)

    plt.plot(x,y)
    plt.title("Hawkeye Trajectory")
    plt.show()

def stadium():

    theta=np.linspace(0,2*np.pi,100)

    x=np.cos(theta)*70
    y=np.sin(theta)*70

    plt.plot(x,y)
    plt.scatter(0,0)
    plt.title("Stadium Field Map")
    plt.gca().set_aspect("equal")
    plt.show()

def dashboard():

    root=tk.Tk()

    root.title("Live Broadcast Dashboard")

    score=tk.Label(root,font=("Arial",40))
    score.pack()

    comm=tk.Text(root,height=15,width=60)
    comm.pack()

    score.config(text=str(runs)+"/"+str(wkts))

    for c in commentary[-10:]:
        comm.insert(tk.END,c+"\n")

    root.mainloop()

run_worm()
manhattan()
wagon_wheel()
hawkeye()
stadium()
dashboard()