from turtle import*

speed(30)
#we want to paint a house
shape("turtle")
#step 1 draw a square  
width(7)
color("purple")
forward(200)
left(90)


forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square




#drawing a door

forward(70)
color('yellow')
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()
penup()
goto(200 , 200)
pendown()
begin_fill()
color("red")
right(150)
forward(200)
left(120)
forward(200)
end_fill()
penup()
goto(15 , 185)
pendown()
color("black")
left(30)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
penup()
goto(185 , 185)
pendown()

forward(30)
left(90)

forward(30)
left(90)

forward(30)
left(90)

forward(30)
left(90)


exitonclick()