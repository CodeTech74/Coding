import turtle

def draw_square(side_length):
    """
    Draws a square using the turtle graphics library.

    Args:
        side_length: The length of each side of the square.
    """
    my_turtle = turtle.Turtle()  # Create a turtle object
    my_turtle.speed(0) #set speed to fastest
    for _ in range(4):  # Loop 4 times for 4 sides
        my_turtle.forward(side_length)
        my_turtle.left(90)  # Turn left 90 degrees

    turtle.done()  # Keep the window open until closed manually

# Example usage:
side = 100
draw_square(side)

side2 = 200
draw_square(side2)

side3 = 50
draw_square(side3)