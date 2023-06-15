#Burak Gürkan ÜNAL 190200018
#Ezgi ÖZCAN 190200015
#İrem ÇELEBİLER 190200016

import turtle
import pandas
from tkinter import messagebox

screen = turtle.Screen()
screen.setup(width=1280, height=720)

unnamed = 'unnamed.gif'
named = 'named.gif'
screen.addshape(unnamed)
turtle.shape(unnamed)


pen = turtle.Turtle()
pen.hideturtle()
pen.penup()


pen2 =turtle.Turtle()
pen2.hideturtle()
pen2.penup()


pen3=turtle.Turtle()
pen3.hideturtle()
pen3.penup()


data = pandas.read_csv('States.csv')
states = data['States'].to_list()
correctanswers = []
tries =0

while len(correctanswers) < 82:
	answer = screen.textinput(
		title=f'Guess the State {len(correctanswers)}/82',	prompt='Type State Name to Start or Exit,Retry')
	answer = answer.title()
	if answer == "Retry":
		screen.clear()
		screen.addshape(unnamed)
		turtle.shape(unnamed)
		tries = 0
		correctanswers = []
	elif answer in correctanswers:
		messagebox.showwarning("Warning","You have guessed this state.")
	elif answer == "Exit":
		break
	elif answer in states:
		tries=tries+1
		state = data[data.States == answer]
		x_ = int(state.x)
		y_ = int(state.y)
		correctanswers.append(answer)
		pen.goto(x=x_, y=y_)
		pen.write(f"{answer}", font=('Arial', 8, 'normal'))
		pen2.clear()
		pen2.goto(-100,325)
		pen2.write("Guessed/Remaining= "+f"{len(correctanswers)}"+"/"+f"{82-len(correctanswers)}",font=('Arial', 12, 'normal'))
		pen3.clear()
		pen3.goto(-100,300)
		pen3.write("Tries= " +f"{tries}",font=('Arial', 12, 'normal'))
	else:
		messagebox.showwarning("Warning",answer+" is not state of Turkey")
		tries = tries + 1
		pen3.clear()
		pen3.goto(-100, 300)
		pen3.write("Tries= " + f"{tries}", font=('Arial', 12, 'normal'))


screen.clear()
screen.addshape(named)
turtle.shape(named)
pen2.clear()
pen2.goto(-100,300)
score = len(correctanswers)/tries*100
pen2.write("Your Score is: "f"{score}",font=('Arial', 12, 'bold'))
turtle.mainloop()
