import time
from turtle import *
import random
segments=[]
screensize(600,600)
positions = [(0, 0), (-20, 0), (-40, 0)]
game_is_on = True
score = 0
screen = Screen()
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
#Turtle
def add_segment(position):
    new_segment = Turtle("square")
    new_segment.color("red")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)
def extend():
    lastcor = positions[len(positions)-1]
    newcor = (lastcor[0],lastcor[1]+20)
    new_segment = Turtle("square")
    new_segment.color("red")
    new_segment.penup()
    positions.append(newcor)
    new_segment.goto(positions[len(positions)-1])
    segments.append(new_segment)
def create_snake():
    for position in positions:
       add_segment(position)
create_snake()

head = segments[0]
def move():
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    head.forward(20)

def up():
    if head.heading() != 270:
        head.setheading(UP)
        print("up")
def down():
    if head.heading() != 90:
        head.setheading(DOWN)
        print("down")
def right():
    if head.heading() != 180:
        head.setheading(RIGHT)
        print("right")
def left():
    if head.heading() != 0:
        head.setheading(LEFT)
        print("left")

screen.listen()

onkey(up, "Up")
onkey(down, "Down")
onkey(right, "Right")
onkey(left, "Left")

#Food
food = Turtle()
food.shape("circle")
food.penup()
food.shapesize(stretch_len=0.5,stretch_wid=0.5)
food.color("blue")
food.speed("fastest")

def refresh():
    random_x = random.randint(-260,260)
    random_y = random.randint(-260,260)
    food.goto(random_x,random_y)
#Score
Score = Turtle()
Score.color("white")
Score.hideturtle()
Score.penup()
Score.goto(250, 290)
Score.pendown()
def update_score(score):
    Score.write(f"Score: {score}",align="center" ,font=("Courier",24,"normal") )
def game_over():
    Score.goto(0,0)
    Score.write("GAME OVER", align="center", font=("Roboto",48,"bold"))
#Movement
while game_is_on:
    screen.update()
    time.sleep(0.15)
    move()
    print("score:",score)

    if head.distance(food) < 15:
        refresh()
        extend()
        score += 1
        Score.clear()
        update_score(score)

    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        print("Game Over")
        game_over()
        game_is_on = False
screen.exitonclick()
