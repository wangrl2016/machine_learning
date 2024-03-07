import turtle

# Reference: https://eecs.wsu.edu/~schneidj/PyBook/chap13.pdf

def square(length):
    for i in range(4):
        turtle.fd(length)
        turtle.left(90)

if __name__ == '__main__':
    # Command to hide the turtle's shape from the screen.
    turtle.hideturtle()

    # Draw a square box.
    turtle.fd(100)
    turtle.left(90)
    turtle.fd(100)
    turtle.left(90)
    turtle.fd(100)
    turtle.left(90)
    turtle.fd(100)

    # Using `penup()` and `setposition()` to move the turtle without making a line.
    turtle.penup()
    turtle.setposition(100, -100)
    turtle.pendown()
    turtle.fd(130)

    # Remove previous drawings and reset turtle.
    turtle.reset()

    # Draw circle counterclockwise with radius 100.
    turtle.circle(100)
    # Draw circle clockwise with radius 50.
    turtle.circle(-50)

    # There is a `speed()` method for which the argument specifies the
    # speed as an integer between 0 and 10.
    turtle.reset()
    turtle.speed(0)
    turtle.circle(100)
    turtle.circle(-50)

    turtle.reset()
    turtle.color('blue')
    turtle.pensize(100)
    turtle.fd(100)

    colors = ['blue', 'green', 'purple', 'cyan', 'magenta', 'violet']
    turtle.reset()
    # Turning off the animation with `tracer()`.
    # turtle.tracer(0, 0)
    for i in range(45):
        turtle.color(colors[ i % 6])
        turtle.pendown()
        turtle.fd(2 + i * 5)
        turtle.left(45)
        turtle.width(i)
        turtle.penup()
    turtle.update()

    turtle.reset()
    turtle.color('green')
    turtle.begin_fill()
    square(100)
    turtle.end_fill()    

    turtle.done()