###################################
# FILE : hello_turtle.py
# WRITER : Ayelet Avraham, ayeletavr, 313451932
# EXERCISE : intro2cs ex1 2019
# DESCRIPTION : A program that draws three flowers with turtle.
##################################

import turtle

# Function that draws a petal:
def draw_petal():
    turtle.circle(100, 90)
    turtle.left(90)
    turtle.circle(100, 90)
    if __name__ == "__main__":
        return

# Function that draws a single flower:
def draw_flower():
    turtle.setheading(0)
    draw_petal()
    turtle.setheading(90)
    draw_petal()
    turtle.setheading(180)
    draw_petal()
    turtle.setheading(270)
    draw_petal()
    turtle.setheading(270)
    turtle.forward(250)
    if __name__ == "__main__":
        return

# Function that draws a single flower and prapares for the next:
def draw_flower_advance():
    turtle.down()
    draw_flower()
    turtle.right(90)
    turtle.up()
    turtle.forward(250)
    turtle.right(90)
    turtle.forward(250)
    turtle.left(90)
    if __name__ == "__main__":
        return

# Function that draws 3 flowers:
def draw_flower_bed():
    turtle.up()
    turtle.forward(200)
    turtle.left(180)
    draw_flower_advance()
    draw_flower_advance()
    draw_flower_advance()
    if __name__ == "__main__":
        print(draw_flower_bed()) #to print the final result.

if __name__ == "__main__":
    draw_flower_bed()
    turtle.done()