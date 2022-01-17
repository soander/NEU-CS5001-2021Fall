"""
Code to design the spiral by turtle

Author: Yaozheng Wang
CS5001 homework
homework 5
2021-11-1
"""
# Import the turtle to draw the spiral
import turtle
# Set the background black
background = turtle.Screen()
background.bgcolor('black')
# Set five colors will be used
colors = ["red", "green", "blue", "white", "orange"]


# The function will draw tangent_circle_shape
def tangent_circle_shape(number):
    """
    Function: The function will draw tangent_circle_shape
    :param number: It's the repeat times
    :return: tangent_circle_shape with five colors
    """
    times = 0
    # Use while loop to repeat the tangent_circle_shape
    while times <= number:
        turtle.circle(times)
        times += 1
        turtle.color(colors[(times % 5)])


# The function to draw curve_shape
def curve_shape(number):
    """
    Function: The function to draw curve_shape
    :param number: It's the repeat times
    :return: curve_shape with five colors
    """
    # Use for loop to repeat curve_shape
    for i in range(number):
        turtle.forward(20 + i)
        turtle.left(30 - i / 0.5)
        turtle.color(colors[(i % 5)])


# The function to draw pentagon_shape
def pentagon_shape(side_length, number):
    """
    Function: The function to draw pentagon_shape
    :param side_length: The pentagon's side length
    :param number: It's the repeat times
    :return: pentagon_shape with five colors
    """
    # Use for loop to repeat the pentagon_shape
    for times in range(number):
        turtle.forward(side_length)
        turtle.right(360 / 5)
        side_length = side_length - 1
        turtle.color(colors[(times % 5)])


# The function to use above functions to draw spirals
def main():
    # Set the turtle speed as the fastest
    turtle.speed(0)
    # Use for loop to repeat each function 18 times
    for times in range(18):
        #
        tangent_circle_shape(20)
        curve_shape(20)
        pentagon_shape(50, 40)
    # Finish the turtle
    turtle.done()


if __name__ == "__main__":
    main()
