from turtle import *
speed(100)
#huse 1

#square
penup()
goto(-200, -200)
pendown()

width(7)
color("cyan")
begin_fill()

forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)

end_fill()

#roof

penup()
goto(-100, -100)
pendown()

right(150)
color("blue")
begin_fill()

forward(100)
left(120)
forward(100)
end_fill()

#door. distance between the door and the edge of the house is 35

penup()
goto(-165, -200)
pendown()
begin_fill()
right(150)


forward(40)
right(90)
forward(30)
right(90)
forward(40)
end_fill()

#window 1

penup()
goto(-135, -150)
pendown()
color("blue")
begin_fill()

left(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
end_fill()

#window 2

penup()
goto(-185, -150)
pendown()
begin_fill()

left(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
end_fill()

#huse 2

#square
penup()
goto(-90, -100)
pendown()

width(7)
color("lavender")
begin_fill()

forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)

end_fill()

#roof

penup()
goto(10, -100)
pendown()

right(60)
color("purple")
begin_fill()

forward(100)
left(120)
forward(100)
end_fill()

#door

penup()
goto(-55, -200)
pendown()
right(150)
begin_fill()

forward(40)
right(90)
forward(30)
right(90)
forward(40)
end_fill()

#window 1

penup()
goto(-25, -150)
pendown()
begin_fill()

left(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
end_fill()

#window 2

penup()
goto(-55, -150)
pendown()
begin_fill()

right(90)
forward(20)
right(90)
forward(20)
right(90)
forward(20)
right(90)
forward(20)
end_fill()

#house 3

#square

penup()
goto(20, -100)
pendown()
color("orange")
begin_fill()

forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
end_fill()

#roof

penup()
goto(120, -100)
pendown()
color("red")
begin_fill()

right(60)
forward(100)
left(120)
forward(100)
end_fill()

#door

penup()
goto(55, -200)
pendown()
begin_fill()

right(150)
forward(40)
right(90)
forward(30)
right(90)
forward(40)
end_fill()

#window 1

penup()
goto(85, -150)
pendown()
begin_fill()

left(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
end_fill()

#window 2

penup()
goto(55, -150)
pendown()
begin_fill()

right(90)
forward(20)
right(90)
forward(20)
right(90)
forward(20)
right(90)
forward(20)
end_fill()

#sun

penup()
goto(100, 200)
pendown()
begin_fill()
color("yellow")

r=75
circle(r)
end_fill()

#stars

penup()
goto(-150, 156)
pendown()
color("blue")

for i in range(5):
    forward(20)
    right(144)

penup()
goto(150, 100)
pendown()

for i in range(5):
    forward(20)
    right(144)

penup()
goto(180, 10)
pendown()

for i in range(5):
    forward(20)
    right(144)

penup()
goto(-236, 28)
pendown()

for i in range(5):
    forward(20)
    right(144)

penup()
goto(0, 100)
pendown()

for i in range(5):
    forward(20)
    right(144)


penup()
goto(10, 300)
pendown()

for i in range(5):
    forward(20)
    right(144)


penup()
goto(-250, 250)
pendown()

for i in range(5):
    forward(20)
    right(144)

exitonclick()