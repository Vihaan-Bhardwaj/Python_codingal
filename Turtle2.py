import turtle
turtle.Screen().bgcolor("blue")
sc = turtle.Screen()
sc.setup(900,900)
turtle.title("Welcome to Turtle Window")
board = turtle.Turtle()
for i in range(4):
  board.forward(100)  
  board.left(90)
  i = i + 1

turtle.done()  