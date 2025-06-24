import turtle
import math

def draw_pythagoras_tree(t, branch_length, level, angle=45):
    if level == 0:
        return
    t.forward(branch_length)
    x, y = t.position()
    heading = t.heading()
    t.left(angle)
    draw_pythagoras_tree(t, branch_length * math.cos(math.radians(angle)), level - 1, angle)
    t.penup()
    t.setposition(x, y)
    t.setheading(heading)
    t.pendown()
    t.right(angle)
    draw_pythagoras_tree(t, branch_length * math.sin(math.radians(angle)), level - 1, angle)
    t.penup()
    t.setposition(x, y)
    t.setheading(heading)
    t.pendown()

def main():
    level = int(input("Введіть рівень рекурсії (наприклад, 6): "))

    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.color("brown")
    t.speed(0)
    t.left(90)

    t.penup()
    t.goto(0, -250)
    t.pendown()

    draw_pythagoras_tree(t, 100, level)
    t.hideturtle()
    screen.exitonclick()

if __name__ == "__main__":
    main()

