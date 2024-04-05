from turtle import *

#square

width(7)
color("purple")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)
 
forward(200)
left(90)

forward(200)
left(90)
end_fill()

forward(70)

#door

color("yellow")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

#roof

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(50, 160)
pendown()

#window 1

color("yellow")
begin_fill()
left(30)
forward(60)
right(90)
forward(30)
right(90)
forward(60)
right(90)
forward(30)
end_fill()

penup()
goto(150, 160)
pendown()

#window 2

color("yellow")
begin_fill()
forward(30)
right(90)
forward(60)
right(90)
forward(30)
right(90)
forward(60)
end_fill()

exitonclick()