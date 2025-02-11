import turtle

def draw_axes_and_connections(n_points):
    # Set some constants for the axis lengths
    X_max = 300
    Y_max = 300

    turtle.speed(0)        # High drawing speed
    turtle.hideturtle()    # Hide the turtle shape
    turtle.penup()

    # Draw the x-axis from (0,0) to (X_max,0)
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.goto(X_max, 0)
    turtle.penup()

    # Draw the y-axis from (0,0) to (0,Y_max)
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.goto(0, Y_max)
    turtle.penup()

    # Draw ticks on the x-axis and label the numbers
    for i in range(1, n_points + 1):
        x = i * (X_max / n_points)
        # Draw a small line downward from the tick
        turtle.goto(x, 0)
        turtle.pendown()
        turtle.goto(x, -5)
        turtle.penup()
        # Write the number below the tick
        turtle.goto(x, -20)
        turtle.write(str(i), align="center", font=("Arial", 10, "normal"))

    # Draw ticks on the y-axis and label the numbers
    for i in range(1, n_points + 1):
        y = i * (Y_max / n_points)
        # Draw a small line to the left of the tick
        turtle.goto(0, y)
        turtle.pendown()
        turtle.goto(-5, y)
        turtle.penup()
        # Write the number to the left of the tick
        turtle.goto(-20, y - 5)
        turtle.write(str(i), align="right", font=("Arial", 10, "normal"))

    # Draw the connecting lines:
    # Based on the example: If we have 10 points
    # We connect: point x1 with y10, x2 with y9, x3 with y8, and so on.
    for i in range(1, n_points + 1):
        x = i * (X_max / n_points)
        # The corresponding point on the y-axis is:
        y = (n_points - i + 1) * (Y_max / n_points)
        # Starting from a point on the x-axis
        turtle.goto(x, 0)
        turtle.pendown()
        # Move to the corresponding point on the y-axis
        turtle.goto(0, y)
        turtle.penup()

    turtle.done()

# Input the number of points from the user
n = int(input("Enter the number of points: "))
draw_axes_and_connections(n)
