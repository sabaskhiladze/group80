from turtle import*


#we want to paint a house

#step 1: draw a square

speed(30)
width(7)
color("black")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of spuare

# step 2: drawing a door

forward(70)
color("brown")
left(90)
forward(120)     #hetht of the door 
right(90)
forward(60)
right(90)
forward(120)

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

# step 3: drawing a window
color("black")
penup()
goto(175, 175)
pendown()
left(30)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
penup()
goto(20, 175)
pendown()
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
penup()
goto(155, 175)
pendown()
right(180)
forward(40)
penup()
goto(40, 175)
pendown()
forward(40)
penup()
goto(40, 155)
pendown()
left(90)
forward(20)
left(180)
forward(40)
penup()
goto(135, 155)
pendown()
left(180)
forward(40)
penup()
goto(10, 0)

exitonclick()