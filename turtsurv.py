import random
import turtle
import time
turtle.speed(0)
turtle.bgcolor("blue")
turtle.ht()
turtle.title("Turtle Survival")
turtle.setundobuffer(1)
turtle.tracer(0)
class Sprite(turtle.Turtle):
  def __init__(self, spriteshape, color, startx, starty) :
    turtle.Turtle.__init__(self, shape = spriteshape)
    self.speed(0)
    self.penup()
    self.color(color)
    self.fd(0)
    self.goto(startx, starty)
    self.speed = 1
  def move(self) :
    self.fd(self.speed)
    if self.xcor() > 290 :
      self.setx(290)
      self.rt(60)
    if self.xcor() < -290 :
      self.setx(-290)
      self.rt(60)
    if self.ycor() > 290 :
      self.sety(290)
      self.rt(60)
    if self.ycor() < -290 :
      self.sety(-290)
      self.rt(60)
  def coll__(self, other) :
    if (self.xcor() >= (other.xcor() - 20)) and \
       (self.xcor() <= (other.xcor() + 20)) and \
       (self.ycor() >= (other.ycor() - 20)) and \
       (self.ycor() <= (other.ycor() + 20)) :
      return True
    else :
      return False

class Turt(Sprite):
  def __init__(self, spriteshape, color, startx, starty) :
    Sprite.__init__(self, spriteshape, color, startx, starty)
    self.shapesize(stretch_wid = 1.5, stretch_len = 1.5)
    self.speed = 4
    self.lives = 3
  def turn_left(self) :
    self.lt(45)
  def turn_right(self) :
    self.rt(45)
  def accelerate(self) :
    self.speed += 1
  def decelerate(self) :
    self.speed -= 1

class Straw(Sprite):
  def __init__(self, spriteshape, color, startx, starty) :
    Sprite.__init__(self, spriteshape, color, startx, starty)
    self.shapesize(stretch_wid = 0.15, stretch_len = 1.5)
    self.speed = 6
    self.setheading(random.randint(0, 360))

class Bubble(Sprite):
  def __init__(self, spriteshape, color, startx, starty) :
    Sprite.__init__(self, spriteshape, color, startx, starty)
    self.shapesize(stretch_wid = 0.3, stretch_len = 0.3)
    self.speed = 40
    self.status = "ready"
    self.goto(-1000, 1000)
  def pew(self):
    if self.status == "ready":
      self.goto(player.xcor(), player.ycor())
      self.setheading(player.heading())
      self.status = "dart"
  def move(self):
    if self.status == "ready" :
      self.goto(-1000, 1000)
    if self.status == "dart" :
      self.fd(self.speed)
    if self.xcor() < -290 or self.xcor() > 290 or \
       self.ycor() < -290 or self.ycor() > 290 :
      self.goto(-1000, 1000)
      self.status = "ready"

class Kelp(Sprite):
 def __init__(self, spriteshape, color, startx, starty) :
    Sprite.__init__(self, spriteshape, color, startx, starty)
    self.shapesize(stretch_wid = 0.409, stretch_len = 0.75)
    self.speed = 8
    self.setheading(random.randint(0, 360))
 def move(self) :
    self.fd(self.speed)
    if self.xcor() > 290 :
      self.setx(290)
      self.lt(60)
    if self.xcor() < -290 :
      self.setx(-290)
      self.lt(60)
    if self.ycor() > 290 :
      self.sety(290)
      self.lt(60)
    if self.ycor() < -290 :
      self.sety(-290)
      self.lt(60)

class Particle(Sprite):
  def __init__(self, spriteshape, color, startx, starty) :
    Sprite.__init__(self, spriteshape, color, startx, starty)
    self.shapesize(stretch_wid = 0.1, stretch_len = 0.1)
    self.goto(-1000, 1000)
    self.frame = 0
  def destroy(self, startx, starty) :
    self.goto(startx, starty)
    self.setheading(random.randint(0, 360))
    self.frame = 1
  def move (self) :
    if self.frame > 0 :
     self.fd(10)
     self.frame += 1
    if self.frame > 15 :
     self.frame = 0
     self.goto(-1000, 1000)

class Main():
  def __init__(self):
    self.level = 1
    self.score = 0
    self.state = "playing"
    self.pen = turtle.Turtle()
  def draw_border(self):
    self.pen.speed(0)
    self.pen.color("black")
    self.pen.pensize(3)
    self.pen.penup()
    self.pen.goto(-300, 300)
    self.pen.pendown()
    for side in range(4):
      self.pen.fd(600)
      self.pen.rt(90)
    self.pen.penup()
    self.pen.ht()
  def show_status(self):
    self.pen.undo()
    msg = "Health: %s" %(self.score)
    self.pen.penup()
    self.pen.goto(-300, 310)
    self.pen.write(msg, font=("Arial", 16, "normal"))

game = Main()
game.draw_border()
game.show_status()
player = Turt("turtle", "lightgreen", 0, 0)
# straw = Straw("square", "white", -100, 0)
bubble = Bubble("circle", "skyblue", 0, 0)
# kelp = Kelp("triangle", "green", 0, 0)
straws = []
kelps = []
particles = []
for i in range(6) :
  kelps.append(Kelp("triangle", "lightgreen", 100, 0))
for i in range(6) :
  straws.append(Straw("square", "white", -100, 0))
for i in range(20) :
  particles.append(Particle("circle", "white", 0, 0))
turtle.onkey(player.turn_left, "Left")
turtle.onkey(player.turn_right, "Right")
turtle.onkey(player.accelerate, "Up")
turtle.onkey(player.decelerate, "Down")
turtle.onkey(bubble.pew, "space")
turtle.listen()
while True :
  turtle.update()
  time.sleep(0.02)
  player.move()
  bubble.move()
  for straw in straws :
    straw.move()
    if player.coll__(straw) :
     x = random.randint(-250, 250)
     y = random.randint(-250, 250)
     straw.goto(x, y)
     game.score -= 100
     game.show_status()
    if bubble.coll__(straw) :
     x = random.randint(-250, 250)
     y = random.randint(-250, 250)
     straw.goto(x, y)
     straw.status = "ready"
     game.score += 100
     game.show_status()
     for particle in particles :
       particle.destroy()
       particle.goto(bubble.xcor(), bubble.ycor())
       particle.setheading(random.randint(0, 360))
  for kelp in kelps :
    kelp.move()
    if player.coll__(kelp) :
     x = random.randint(-250, 250)
     y = random.randint(-250, 250)
     kelp.goto(x, y)
     game.score += 50
     game.show_status()
    if bubble.coll__(kelp) :
     x = random.randint(-250, 250)
     y = random.randint(-250, 250)
     kelp.goto(x, y)
     straw.status = "ready"
     game.score -= 50
     game.show_status()
turtle.done()