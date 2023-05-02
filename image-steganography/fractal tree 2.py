import turtle
import random

def tree(branch_len, t, branch_width):
    if branch_len < 10:
        return
    angle = random.randint(20, 45)
    sf = random.uniform(0.6, 0.8)
    t.pensize(branch_width)
    colour = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
    clr = colour[random.randrange(0,7)]
    t.pencolor()
    t.forward(branch_len)
    t.right(angle)
    tree(branch_len*sf, t, branch_width*sf)
    t.left(angle*2)
    tree(branch_len*sf, t, branch_width*sf)
    t.right(angle)
    t.backward(branch_len)

def draw_tree(x, y):
    t = turtle.Turtle()
    t.speed("fastest")
    t.left(90)
    t.up()
    t.goto(x, y)
    t.down()
    tree(70, t, 7)

def main():
    turtle.Screen().bgcolor("white")
    for i in range(10):
        x = random.randint(-300, 300)
        y = random.randint(-200, 200)
        draw_tree(x, y)
    turtle.done()

main()
