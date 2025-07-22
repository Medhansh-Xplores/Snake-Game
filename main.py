import turtle
import time
import random

delay = 0.1

#screen
scrn = turtle.Screen()
scrn.title("Snake Game by Medhansh")
scrn.bgcolor("yellow")
scrn.setup(width=600, height=600)
scrn.tracer(0)

#Snake Head
hd = turtle.Turtle()
hd.speed(0)
hd.shape("square")
hd.color("black")
hd.penup()
hd.goto(0, 0)
hd.direction = "stop"

#Snake food
fd = turtle.Turtle()
fd.speed(2)
fd.shape("circle")
fd.color("red")
fd.penup()
fd.goto(0, 200)

#score
score = 0
high_score = 0

#scoring pen
pen = turtle.Turtle()
pen.shape("square")
pen.color("blue")
pen.penup()
pen.hideturtle()
pen.goto(0, 280)
pen.write("Score: 0     Highscore:0",
          align="center",
          font=("Courier", 12, "normal"))

#Functions


def go_up():
  if hd.direction != "down":
    hd.direction = "up"


def go_down():
  if hd.direction != "up":
    hd.direction = "down"


def go_left():
  if hd.direction != "right":
    hd.direction = "left"


def go_right():
  if hd.direction != "left":
    hd.direction = "right"


def move():
  if hd.direction == "up":
    y = hd.ycor()
    hd.sety(y + 20)
  if hd.direction == "down":
    y = hd.ycor()
    hd.sety(y - 20)
  if hd.direction == "left":
    x = hd.xcor()
    hd.setx(x - 20)
  if hd.direction == "right":
    x = hd.xcor()
    hd.setx(x + 20)


#keyboard bindings
scrn.onkeypress(go_up, "Up")
scrn.onkeypress(go_down, "Down")
scrn.onkeypress(go_left, "Left")
scrn.onkeypress(go_right, "Right")
scrn.listen()

body = []  #empty body

#Main loop
while 1:
  scrn.update()

  if hd.xcor() > 290 or hd.xcor() < -290 or hd.ycor() > 290 or hd.ycor(
  ) < -290:  #Border collision
    pen.clear()
    score = 0
    pen.write(f"Score: 0     Highscore: {high_score}",
              align="center",
              font=("Courier", 12, "normal"))

    time.sleep(0.5)
    hd.goto(0, 0)
    hd.direction = "stop"

    for i in body:
      i.hideturtle()  #hiding the body

    body.clear()  #clearing body before next run

  if hd.distance(fd) < 20:  #Food Collision

    score = score + 1  #score
    high_score = max(high_score, score)

    pen.clear()
    pen.write(f"Score: {score}   Highscore: {high_score}",
              align="center",
              font=("Courier", 12, "normal"))

    x = random.randint(-290, 290)
    y = random.randint(-290, 290)
    fd.goto(x, y)

    new_body = turtle.Turtle()  #adding body
    new_body.color("grey")
    new_body.shape("square")
    new_body.speed(0)
    new_body.penup()
    body.append(new_body)

  for i in range(len(body) - 1, 0, -1):  #moving all body except 0th body
    x = body[i - 1].xcor()
    y = body[i - 1].ycor()
    body[i].goto(x, y)

  if len(body) > 0:  #moving 0th body
    x = hd.xcor()
    y = hd.ycor()
    body[0].goto(x, y)

  time.sleep(delay)
  move()

  for i in body:  #body collision
    if i.distance(hd) < 20:
      time.sleep(0.5)
      hd.goto(0, 0)
      hd.direction = "stop"

      for j in body:
        j.hideturtle()

      body.clear()

      pen.clear()
      score = 0
      pen.write(f"Score: 0     Highscore: {high_score}",
                align="center",
                font=("Courier", 12, "normal"))

scrn.mainloop()
