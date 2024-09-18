import tkinter as tk 
import random

import turtle as trtl
from PIL import Image
import math
root = tk.Tk()
root.geometry("700x700")
root.title('Basketball Game Simulation')





canvas = tk.Canvas(root, width=1200, height=1200)
canvas.grid()
screen=trtl.Screen()
screen.screensize(1200, 1200)
screen.bgcolor("white")
screen._root = root
screen._canvas = canvas
image = Image.open("hoop.gif")
image = image.resize((50,250))
image.save('new_hoop.gif')
image2=Image.open('new_hoop.gif')
image2=image2.transpose(Image.FLIP_LEFT_RIGHT)
image2.save('second_hoop.gif')
screen.register_shape("second_hoop.gif")
basket_left = trtl.RawTurtle(screen)
basket_left.shape("second_hoop.gif")
basket_left.hideturtle()
basket_left.penup()
basket_left.goto(-300,0)
basket_left.showturtle()

screen.register_shape("new_hoop.gif")
basket_right = trtl.RawTurtle(screen)
basket_right.shape("new_hoop.gif")
basket_right.hideturtle()
basket_right.penup()
basket_right.goto(300,0)
basket_right.showturtle()
def stick_figure_left():#team1
  turtle=trtl.RawTurtle(screen)
  turtle.hideturtle()
  turtle.speed(0)
  turtle.penup()
  turtle.goto(-70,-40)
  turtle.pendown()
  turtle.circle(10)  # Head
  turtle.right(90)
  turtle.forward(20)# Body
  turtle.right(135)
  turtle.forward(25)
  turtle.backward(25)
  turtle.left(135)
  turtle.forward(5)
  turtle.right(135)
  turtle.forward(25)
  turtle.backward(25)
  turtle.left(135)
  turtle.forward(15)
  turtle.right(28)
  turtle.forward(25)
  turtle.backward(25)
  turtle.left(28)
  turtle.forward(25)
  turtle.penup()
  turtle.hideturtle()
stick_figure_left()
def stick_figure_right():#team2
  turtle=trtl.RawTurtle(screen)
  turtle.hideturtle()
  turtle.speed(0)
  turtle.penup()
  turtle.goto(70,-40)
  turtle.pendown()
  turtle.circle(10)  # Head
  turtle.right(90)
  turtle.forward(20)# Body
  turtle.left(135)
  turtle.forward(25)
  turtle.backward(25)
  turtle.right(135)
  turtle.forward(5)
  turtle.left(135)
  turtle.forward(25)
  turtle.backward(25)
  turtle.right(135)
  turtle.forward(15)
  turtle.left(28)
  turtle.forward(25)
  turtle.backward(25)
  turtle.right(28)
  turtle.forward(25)
  turtle.penup()
  turtle.hideturtle()
stick_figure_right()

def probably(pointguard_efficiency):
  return random.random() < pointguard_efficiency#prints booleans true or false

#condensed my function down because of repition
#previous in team_2
def calculate_points(volume, volume_range, efficiency, efficiency_range, defense):
  points = []
  #volume slider logic
  if volume <= 50:
    volume_points = round((volume / 50) * (volume_range[0] - 0) + 0)
  else:
    volume_points = round(((volume - 50) / 50) * (volume_range[1] - volume_range[0]) + volume_range[0])
#if no shots taken 0 points put up
  if volume_points == 0:
    return [2]
#efficiency slider logic
  if efficiency <= 50:
    player_efficiency = (efficiency / 50) * (efficiency_range[0] - 0) + 0
  else:
    player_efficiency = ((efficiency - 50) / 50) * (efficiency_range[1] - efficiency_range[0]) + efficiency_range[0]
#defense effectiveness
  player_efficiency *= 0.01
  efficiency_drop = defense * 0.001
  player_efficiency -= efficiency_drop
#amount of shots that will be made
  for i in range(volume_points):
    player_points = 0
    if probably(player_efficiency):
      player_points += 1
    points.append(player_points)#sum_points equals number of shots fieldgoals made
  return points



def team1():
  pointguard_threes= calculate_points(pg_slider2.get(), (7.3, 10.2), pg_slider1.get(), (36.3, 45.1), pg2_slider5.get())
  pointguard_twos = calculate_points(pg_slider4.get(), (9.3, 12.4), pg_slider3.get(), (47.1, 50.2), pg2_slider5.get())
  pointguard_points=pointguard_threes+pointguard_twos
  # shooting guard
  shootingguard_threes = calculate_points(sg_slider2.get(), (7.7, 12.7), sg_slider1.get(), (36.6, 47.5), sg2_slider5.get())
  shootingguard_twos = calculate_points(sg_slider4.get(), (9.9, 14.4), sg_slider3.get(), (49.4, 53.2), sg2_slider5.get())
  shootingguard_points = (shootingguard_threes*3) + (shootingguard_twos*2)
  
  # small forward
  smallforward_threes = calculate_points(sf_slider2.get(), (5.8, 8.5), sf_slider1.get(), (36.5, 40.8), sf2_slider5.get())
  smallforward_twos = calculate_points(sf_slider4.get(), (9.9, 14.6), sf_slider3.get(), (50.4, 55.3), sf2_slider5.get())
  smallforward_points = (smallforward_threes*3) + (smallforward_twos*2)
  
  # power forward
  powerforward_threes = calculate_points(pf_slider2.get(), (4.7, 8), pf_slider1.get(), (35.1, 39.5), pf2_slider5.get())
  powerforward_twos = calculate_points(pf_slider4.get(), (10.5, 16.2), pf_slider3.get(), (51.1, 55.5), pf2_slider5.get())
  powerforward_points = (powerforward_threes*3) + (powerforward_twos*2)
  
  # center
  center_threes = calculate_points(center_slider2.get(), (0.3, 3.7), center_slider1.get(), (33.3, 38.8), center2_slider5.get())
  center_twos = calculate_points(center_slider4.get(), (9.2, 13.1), center_slider3.get(), (47.6, 51.9), center2_slider5.get())
  center_points = (center_threes*3) + (center_twos*2)
  team1_threes= pointguard_threes+shootingguard_threes+smallforward_threes+powerforward_threes+center_threes
  team1_twos= pointguard_twos+shootingguard_twos+smallforward_twos+powerforward_twos+center_twos
  print(team1_threes)
  return team1_threes,team1_twos
  


def team2():
  # point guard
  pointguard_threes =calculate_points(pg2_slider2.get(), (5.3, 11.3), pg2_slider1.get(), (36.3, 45.1), pg_slider5.get())
  pointguard_twos = calculate_points(pg2_slider4.get(), (9.3, 12.4), pg2_slider3.get(), (47.1, 50.2), pg_slider5.get())
  pointguard_points = (pointguard_threes*3) + (pointguard_twos*2)
  
  # shooting guard
  shootingguard_threes = calculate_points(sg2_slider2.get(), (7.7, 12.7), sg2_slider1.get(), (36.6, 47.5), sg_slider5.get())
  shootingguard_twos = calculate_points(sg2_slider4.get(), (9.9, 14.4), sg2_slider3.get(), (49.4, 53.2), sg_slider5.get())
  shootingguard_points = (shootingguard_threes*3) + (shootingguard_twos*2)
  
  # small forward
  smallforward_threes = calculate_points(sf2_slider2.get(), (5.8, 8.5), sf2_slider1.get(), (36.5, 40.8), sf_slider5.get())
  smallforward_twos = calculate_points(sf2_slider4.get(), (9.9, 14.6), sf2_slider3.get(), (50.4, 55.3), sf_slider5.get())
  smallforward_points = (smallforward_threes*3) + (smallforward_twos*2)
  
  # power forward
  powerforward_threes = calculate_points(pf2_slider2.get(), (4.7, 8), pf2_slider1.get(), (35.1, 39.5), pf_slider5.get())
  powerforward_twos = calculate_points(pf2_slider4.get(), (10.5, 16.2), pf2_slider3.get(), (51.1, 55.5), pf_slider5.get())
  powerforward_points = (powerforward_threes*3) + (powerforward_twos*2)
  
  # center
  center_threes = calculate_points(center2_slider2.get(), (0.3, 3.7), center2_slider1.get(), (33.3, 38.8), center_slider5.get())
  center_twos = calculate_points(center2_slider4.get(), (9.2, 13.1), center2_slider3.get(), (47.6, 51.9), center_slider5.get())
  center_points = (center_threes*3) + (center_twos*2)
  
  team2_threes= pointguard_threes+shootingguard_threes+smallforward_threes+powerforward_threes+center_threes
  team2_twos= pointguard_twos+shootingguard_twos+smallforward_twos+powerforward_twos+center_twos
  
  return team2_threes,team2_twos


def total_points(team,tuple,point_value):
  shots=team[tuple]
  shots = [x for x in shots if x != 2]
  points=sum(shots)*point_value
  return points
    

  
  
  

    
def multiple_games():
  total=0
  total2=0
  col=5
  col2=7
  number_games=history_slider.get()
  history_frame.tkraise()
  total_label1=tk.Label(history_frame,text='Total')
  total_label1.grid(column=6,row=0)
  total_label2=tk.Label(history_frame,text='Total')
  total_label2.grid(column=8,row=0)
  label=tk.Label(history_frame,text='Team 1:')
  label.grid(column=5,row=0)
  label2=tk.Label(history_frame,text='Team 2:')
  label2.grid(column=7,row=0)
  rows=0
  for i in range(number_games):
    rows+=1
    threes_team2=total_points(team2(),0,3)
    threes_team1=total_points(team1(),0,3)
    twos_team2=total_points(team2(),1,2)
    twos_team1=total_points(team1(),1,2)
    one_team=threes_team1+twos_team1
    two_team=threes_team2+twos_team2
    if one_team>two_team:
      total+=1
      win='W'
    else:
      win='L'
    if two_team>one_team:
      total2+=1
      win2='W'
    else:
      win2='L'
    if two_team==one_team:
      win='T'
      win2='T'
    if i==32:
      rows=0
      col+=4
      col2+=3
    if i==65:
      rows=0
      col+=2
      col2+=2
    if i==98:
      rows=0
      col+=2
      col2+=2
    score_label=tk.Label(history_frame,text=(one_team,win))
    score_label.grid(column=col,row=rows)
    score_label2=tk.Label(history_frame,text=(two_team,win2))
    score_label2.grid(column=col2,row=rows)
  total_label=tk.Label(history_frame,text=total)
  total_label.grid(column=6, row=1)
  total_label2=tk.Label(history_frame,text=total2)
  total_label2.grid(column=8,row=1)



def basketball_visual():
  def shot_order(team,tuple,point_value):
    shots=team[tuple]
    print(shots)
    random.shuffle(shots)
    print(shots)
    shots = [x for x in shots if x != 2]
    for i in range(len(shots)):
      if shots[i] == 1:
        shots[i]=point_value
    return shots
  threes_team2=shot_order(team2(),0,3)
  threes_team1=shot_order(team1(),0,3)
  twos_team2=shot_order(team2(),1,2)
  twos_team1=shot_order(team1(),1,2)
  t2=threes_team2+twos_team2
  print(t2)
  t1=threes_team1+twos_team1
  print(t1)
  
  ball1 = trtl.RawTurtle(screen)
  ball1.shape('circle')
  ball1.color('orange')
  
  ball2 = trtl.RawTurtle(screen)
  ball2.shape('circle')
  ball2.color('orange')
  
  ball1.start_x = -95
  ball1.start_y = -30
  ball1.penup()
  ball1.goto(ball1.start_x, ball1.start_y)
  
  ball2.start_x = 95
  ball2.start_y = -30
  ball2.penup()
  ball2.goto(ball2.start_x, ball2.start_y) 
  def setup_scoreboard(scoreboard, x, y):
    scoreboard.penup()
    scoreboard.goto(x, y)
    scoreboard.hideturtle()

  def update_score(scoreboard, score):
    scoreboard.clear()
    scoreboard.write(str(score), align="center", font=("Arial", 24, "normal"))
  def shot(turtle, angle, v1, end):
    grav = -8.87
    time = 0
    height = 0
    y2 = 0
    x2 = 0
    score=0
    turtle.showturtle()
    x = v1 * math.cos(math.radians(angle))
    y = v1 * math.sin(math.radians(angle))
    while abs(x2) <= end:
      y2 = .5 * grav * (time ** 2) + y * time + height
      x2 = x * time
      turtle.goto(turtle.start_x + x2, turtle.start_y + y2)
      time += 1 
      
    turtle.clear()
    turtle.hideturtle()
  threes_team2=total_points(team2(),0,3)
  threes_team1=total_points(team1(),0,3)
  twos_team2=total_points(team2(),1,2)
  twos_team1=total_points(team1(),1,2)
  final_score1=threes_team1+twos_team1
  final_score2=threes_team2+twos_team2
  team1_score = 0
  team2_score = 0
  team1_scoreboard = trtl.RawTurtle(screen)
  team2_scoreboard = trtl.RawTurtle(screen)
  setup_scoreboard(team1_scoreboard, -100, 0)
  setup_scoreboard(team2_scoreboard, 100, 0)
  root.destroy()
  
  for value in t1:
    if team1_score < final_score1:
      shot(ball1, 120, 50, 180)
      team1_score += value
      update_score(team1_scoreboard, team1_score)
  for value in t2:
    if team2_score < final_score2:
      shot(ball2, 60, 50, 180)
      team2_score += value
      update_score(team2_scoreboard, team2_score)

    if team1_score >= final_score1 and team2_score >= final_score2:
      break
  
  
  if team1_score > team2_score:
    winner = "Team 1 win"
  elif team2_score > team1_score:
    winner = "Team 2 win"
  else:
    winner = "Tie"
  #clear for winners
  team1_scoreboard.clear()
  team2_scoreboard.clear()
  
  team1_scoreboard.goto(-100, 0)
  team1_scoreboard.write("Final Score:\nTeam 1: {}\n{}".format(team1_score, winner), align="center", font=("Arial", 24, "normal"))
  team2_scoreboard.goto(100, 0)
  team2_scoreboard.write("Final Score:\nTeam 2: {}\n{}".format(team2_score,winner), align="center", font=("Arial", 24, "normal"))
  
  trtl.done()
  
      
  
    
      
    
  
  
  







def history():
  history_frame.tkraise()
def edit():
  edit_team_frame.tkraise()
def edit2():
  edit_team2_frame.tkraise()
def place():
  start_frame.tkraise()




start_frame=tk.Frame(root)
start_frame.grid(row=0, column=0, sticky='news')


edit_team_frame=tk.Frame(root)
edit_team_frame.grid(row=0, column=0, sticky='news')

edit_team2_frame=tk.Frame(root)
edit_team2_frame.grid(row=0, column=0, sticky='news')
history_frame=tk.Frame(root)
history_frame.grid(row=0, column=0, sticky='news')

start_frame.tkraise()


#start_frame
team1_label=tk.Label(start_frame,text='Team 1')
team1_label.grid(row=0,column=0)


team1_button=tk.Button(start_frame,text='Edit Abilities',command=edit)
team1_button.grid(row=1,column=0)

team2_label=tk.Label(start_frame,text='Team 2')
team2_label.grid(row=0, column=3)
team2_button=tk.Button(start_frame,text='Edit Abilities',command=edit2)
team2_button.grid(row=1,column=3)




#edit player sliders 
pointguard1_label = tk.Label(edit_team_frame, text='Pointguard')
pointguard1_label.grid(row=0, column=1)

slider1_label = tk.Label(edit_team_frame, text='3 point efficiency')
slider1_label.grid(row=2, column=0)


slider2_label = tk.Label(edit_team_frame, text='3 point volume')
slider2_label.grid(row=4, column=0)


slider3_label = tk.Label(edit_team_frame, text='2 point efficiency')
slider3_label.grid(row=6, column=0)


slider4_label = tk.Label(edit_team_frame, text='2 point volume')
slider4_label.grid(row=8, column=0)


slider5_label = tk.Label(edit_team_frame, text='Defense')
slider5_label.grid(row=10, column=0)

pg_slider1 = tk.Scale(edit_team_frame, from_=0, to=100, orient='horizontal')
pg_slider1.grid(row=2, column=1)


pg_slider2 = tk.Scale(edit_team_frame, from_=0, to=100, orient='horizontal')
pg_slider2.grid(row=4, column=1)

pg_slider3 = tk.Scale(edit_team_frame, from_=0, to=100, orient='horizontal')
pg_slider3.grid(row=6, column=1)

pg_slider4 = tk.Scale(edit_team_frame, from_=0, to=100, orient='horizontal')
pg_slider4.grid(row=8, column=1)

pg_slider5 = tk.Scale(edit_team_frame, from_=0, to=100, orient='horizontal')
pg_slider5.grid(row=10, column=1)


shootingguard1_label = tk.Label(edit_team_frame, text='Shooting Guard')
shootingguard1_label.grid(row=0, column=2)


sg_slider1 = tk.Scale(edit_team_frame, from_=0, to=100, orient='horizontal')
sg_slider1.grid(row=2, column=2)


sg_slider2 = tk.Scale(edit_team_frame, from_=0, to=100, orient='horizontal')
sg_slider2.grid(row=4, column=2)

sg_slider3 = tk.Scale(edit_team_frame, from_=0, to=100, orient='horizontal')
sg_slider3.grid(row=6, column=2)

sg_slider4 = tk.Scale(edit_team_frame, from_=0, to=100, orient='horizontal')
sg_slider4.grid(row=8, column=2)

sg_slider5 = tk.Scale(edit_team_frame, from_=0, to=100, orient='horizontal')
sg_slider5.grid(row=10, column=2)

smallforward1_label = tk.Label(edit_team_frame, text='Small Forward')
smallforward1_label.grid(row=0, column=3)

sf_slider1 = tk.Scale(edit_team_frame, from_=0, to=100, orient='horizontal')
sf_slider1.grid(row=2, column=3)

sf_slider2 = tk.Scale(edit_team_frame, from_=0, to=100, orient='horizontal')
sf_slider2.grid(row=4, column=3)

sf_slider3 = tk.Scale(edit_team_frame, from_=0, to=100, orient='horizontal')
sf_slider3.grid(row=6, column=3)

sf_slider4 = tk.Scale(edit_team_frame, from_=0, to=100, orient='horizontal')
sf_slider4.grid(row=8, column=3)

sf_slider5 = tk.Scale(edit_team_frame, from_=0, to=100, orient='horizontal')
sf_slider5.grid(row=10, column=3)


powerforward1_label = tk.Label(edit_team_frame, text='Power Forward')
powerforward1_label.grid(row=0, column=4)

pf_slider1 = tk.Scale(edit_team_frame, from_=0, to=100, orient='horizontal')
pf_slider1.grid(row=2, column=4)

pf_slider2 = tk.Scale(edit_team_frame, from_=0, to=100, orient='horizontal')
pf_slider2.grid(row=4, column=4)

pf_slider3 = tk.Scale(edit_team_frame, from_=0, to=100, orient='horizontal')
pf_slider3.grid(row=6, column=4)

pf_slider4 = tk.Scale(edit_team_frame, from_=0, to=100, orient='horizontal')
pf_slider4.grid(row=8, column=4)

pf_slider5 = tk.Scale(edit_team_frame, from_=0, to=100, orient='horizontal')
pf_slider5.grid(row=10, column=4)

center1_label = tk.Label(edit_team_frame, text='Center')
center1_label.grid(row=0, column=5)

center_slider1 = tk.Scale(edit_team_frame, from_=0, to=100, orient='horizontal')
center_slider1.grid(row=2, column=5)

center_slider2 = tk.Scale(edit_team_frame, from_=0, to=100, orient='horizontal')
center_slider2.grid(row=4, column=5)

center_slider3 = tk.Scale(edit_team_frame, from_=0, to=100, orient='horizontal')
center_slider3.grid(row=6, column=5)

center_slider4 = tk.Scale(edit_team_frame, from_=0, to=100, orient='horizontal')
center_slider4.grid(row=8, column=5)

center_slider5 = tk.Scale(edit_team_frame, from_=0, to=100, orient='horizontal')
center_slider5.grid(row=10, column=5)

team1_submit=tk.Button(edit_team_frame,text='Create Team',command=place)
team1_submit.grid(row=11,column=3)
#team 2
pointguard2_label = tk.Label(edit_team2_frame, text='Pointguard')
pointguard2_label.grid(row=0, column=1)

slider6_label = tk.Label(edit_team2_frame, text='3 point efficiency')
slider6_label.grid(row=2, column=0)

slider7_label = tk.Label(edit_team2_frame, text='3 point volume')
slider7_label.grid(row=4, column=0)

slider8_label = tk.Label(edit_team2_frame, text='2 point efficiency')
slider8_label.grid(row=6, column=0)

slider9_label = tk.Label(edit_team2_frame, text='2 point volume')
slider9_label.grid(row=8, column=0)

slider10_label = tk.Label(edit_team2_frame, text='Defense')
slider10_label.grid(row=10, column=0)

pg2_slider1 = tk.Scale(edit_team2_frame, from_=0, to=100, orient='horizontal')
pg2_slider1.grid(row=2, column=1)

pg2_slider2 = tk.Scale(edit_team2_frame, from_=0, to=100, orient='horizontal')
pg2_slider2.grid(row=4, column=1)

pg2_slider3 = tk.Scale(edit_team2_frame, from_=0, to=100, orient='horizontal')
pg2_slider3.grid(row=6, column=1)

pg2_slider4 = tk.Scale(edit_team2_frame, from_=0, to=100, orient='horizontal')
pg2_slider4.grid(row=8, column=1)

pg2_slider5 = tk.Scale(edit_team2_frame, from_=0, to=100, orient='horizontal')
pg2_slider5.grid(row=10, column=1)


shootingguard2_label = tk.Label(edit_team2_frame, text='Shooting Guard')
shootingguard2_label.grid(row=0, column=2)

sg2_slider1 = tk.Scale(edit_team2_frame, from_=0, to=100, orient='horizontal')
sg2_slider1.grid(row=2, column=2)

sg2_slider2 = tk.Scale(edit_team2_frame, from_=0, to=100, orient='horizontal')
sg2_slider2.grid(row=4, column=2)

sg2_slider3 = tk.Scale(edit_team2_frame, from_=0, to=100, orient='horizontal')
sg2_slider3.grid(row=6, column=2)

sg2_slider4 = tk.Scale(edit_team2_frame, from_=0, to=100, orient='horizontal')
sg2_slider4.grid(row=8, column=2)

sg2_slider5 = tk.Scale(edit_team2_frame, from_=0, to=100, orient='horizontal')
sg2_slider5.grid(row=10, column=2)

smallforward2_label = tk.Label(edit_team2_frame, text='Small Forward')
smallforward2_label.grid(row=0, column=3)

sf2_slider1 = tk.Scale(edit_team2_frame, from_=0, to=100, orient='horizontal')
sf2_slider1.grid(row=2, column=3)

sf2_slider2 = tk.Scale(edit_team2_frame, from_=0, to=100, orient='horizontal')
sf2_slider2.grid(row=4, column=3)

sf2_slider3 = tk.Scale(edit_team2_frame, from_=0, to=100, orient='horizontal')
sf2_slider3.grid(row=6, column=3)

sf2_slider4 = tk.Scale(edit_team2_frame, from_=0, to=100, orient='horizontal')
sf2_slider4.grid(row=8, column=3)

sf2_slider5 = tk.Scale(edit_team2_frame, from_=0,to=100, orient='horizontal')
sf2_slider5.grid(row=10, column=3)

powerforward2_label = tk.Label(edit_team2_frame, text='Power Forward')
powerforward2_label.grid(row=0, column=4)

pf2_slider1 = tk.Scale(edit_team2_frame, from_=0, to=100, orient='horizontal')
pf2_slider1.grid(row=2, column=4)

pf2_slider2 = tk.Scale(edit_team2_frame, from_=0, to=100, orient='horizontal')
pf2_slider2.grid(row=4, column=4)

pf2_slider3 = tk.Scale(edit_team2_frame, from_=0, to=100, orient='horizontal')
pf2_slider3.grid(row=6, column=4)

pf2_slider4 = tk.Scale(edit_team2_frame, from_=0, to=100, orient='horizontal')
pf2_slider4.grid(row=8, column=4)

pf2_slider5 = tk.Scale(edit_team2_frame, from_=0, to=100, orient='horizontal')
pf2_slider5.grid(row=10, column=4)

center2_label = tk.Label(edit_team2_frame, text='Center')
center2_label.grid(row=0, column=5)

center2_slider1 = tk.Scale(edit_team2_frame, from_=0, to=100, orient='horizontal')
center2_slider1.grid(row=2, column=5)

center2_slider2 = tk.Scale(edit_team2_frame, from_=0, to=100, orient='horizontal')
center2_slider2.grid(row=4, column=5)

center2_slider3 = tk.Scale(edit_team2_frame, from_=0, to=100, orient='horizontal')
center2_slider3.grid(row=6, column=5)

center2_slider4 = tk.Scale(edit_team2_frame, from_=0, to=100, orient='horizontal')
center2_slider4.grid(row=8, column=5)

center2_slider5 = tk.Scale(edit_team2_frame, from_=0, to=100, orient='horizontal')
center2_slider5.grid(row=10, column=5)

team2_submit = tk.Button(edit_team2_frame, text='Create Team', command=place)
team2_submit.grid(row=11, column=3)

sim_label=tk.Label(start_frame,text='Simulate One Game')
sim_label.grid(row=3 ,column=2)

run_sim=tk.Button(start_frame,text='Run', command=basketball_visual)
run_sim.grid(row=4 ,column=2)

history_label=tk.Label(start_frame,text='Simulating Multiple Games 2-100')
history_label.grid(row=5,column=2)
history_slider=tk.Scale(start_frame, from_=2, to=100, orient='horizontal')
history_slider.grid(row=6,column=2)

history_button=tk.Button(start_frame,text='Run',command=multiple_games)
history_button.grid(row=7,column=2)
#history_frame


root.mainloop()


