import turtle
turtle.bgcolor("black")
turtle.pensize(1.5)
turtle.speed(500)

for i in range(16):
	for colours in ['red','green', 'cyan', 'white', 'yellow', 'blue', 'magenta' ]:
		turtle.color(colours)
		turtle.circle(100)
		turtle.left(10)


turtle.forward(10)	

for i in range(16):
	for colours in ['red','green', 'cyan', 'white', 'yellow', 'blue', 'magenta' ]:
		turtle.color(colours)
		turtle.circle(100)
		turtle.left(50)	

turtle.hideturtle()

input( 'ENTER' )