# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 11:22:52 2020

@author: gperc
"""

import turtle
import random
import time
from simplebeep import beep

delay = 0.18
score = 0
high_score = 0

#creating the screen

snake = turtle.Screen()
snake.title("Snake Game")
snake.bgcolor("black")
snake.setup(width=700, height=700)
snake.tracer(0)

#creating the snake's head

head = turtle.Turtle()
head.shape("circle")
head.color("green")
head.penup()
head.goto(0,0)
head.direction = "stop"

#creating the food

food = turtle.Turtle()
food.shape("circle")
food.color("yellow")
food.shapesize(0.7)
food.penup()
food.goto(0,100)

#creating the pen to write the score

pen = turtle.Turtle()
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,320)
pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 20, "normal"))

def gameover():
    beep(pitch=5, duration=.05)
    beep(pitch=7, duration=.07)
    beep(pitch=9, duration=.08)

#creating necessary functions for movement

def turnup():
    if head.direction != "down":
        head.direction = "up"
def turndown():
    if head.direction != "up":
        head.direction = "down"
def turnright():
    if head.direction != "left":
        head.direction = "right"
def turnleft():
    if head.direction != "right":
        head.direction = "left"
 
def move():
   if head.direction == "up":
        y = head.ycor() 
        head.sety(y + 20)
   if head.direction == "down":
        y = head.ycor() 
        head.sety(y - 20)
   if head.direction == "right":
        x = head.xcor() 
        head.setx(x + 20)
   if head.direction == "left":
        x = head.xcor() 
        head.setx(x - 20)   

#setting up the relationship between the keyboard and the movement

snake.listen()
snake.onkeypress(turnleft,"Left")
snake.onkeypress(turnright,"Right")
snake.onkeypress(turnup,"Up")
snake.onkeypress(turndown,"Down")

#creating a function to write the score

def wr_score():
    pen.clear() 
    pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 20, "normal")) 

segments = []

# the mainloop of our game

while True:
    snake.update()
    
    #checking for border collusions, if there is collusion setting the score to zero
    
    if head.xcor()  > 342 or head.xcor() < -342 or head.ycor() > 342 or head.ycor() < -342 :
        head.goto(0,0)
        head.direction = "stop"
        food.goto(0,100)
        gameover()
        
        for segment in segments:
            segment.goto(1000, 1000)
        segments = []
        score = 0
        wr_score()
        delay = 0.18
        
    #checking if the snake eats the food, if it eats the food adding an extra body part
        
    if head.distance(food) < 15:
           
    #creating snake's body and adding the body part
        
        body = turtle.Turtle()
        body.speed(0)
        body.shape("circle")
        body.color("green")
        body.penup()
        segments.append(body)
        
    # as the snake eats the food, the food appears at a random place
    
        x = random.randint(-330, 330)
        y = random.randint(-330, 300)
        x != head.xcor() and y != head.ycor()
        x != body.xcor() and y != body.ycor()
        food.goto(x, y)
    
    #updating the score as the snake eats the food
        score += 10
        if score > high_score:
            high_score = score
        wr_score()
        
    #at some milestones the snake will get faster
        
        if score == 50 or score==150 or score==250 or score==500 or score==1000:
           delay -= .035
        
    #rearranging the snake's body as it eats the food and gets bigger
            
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
        
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
        
    move()
    
    #checking for body collussion, if there is collusion setting the score to zero
    
    for segment in segments:
       if segment.distance(head) < 20 :
           head.goto(0,0)
           head.direction = "stop"
           food.goto(0,100)
           gameover()
            
           for segment in segments:
               segment.goto(1000, 1000)    
           segments = []
           score = 0  
           wr_score()
           delay = 0.18
           
    time.sleep(delay)
    
turtle.done()

