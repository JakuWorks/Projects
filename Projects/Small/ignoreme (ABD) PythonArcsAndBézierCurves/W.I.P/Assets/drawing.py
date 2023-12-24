"""
This module contains functions that take care of the arc/Bezier drawing animations.
"""

from math import cos, radians, sin
from turtle import Turtle, colormode, exitonclick, tracer, update
from typing import Tuple
import requests

tracer(0)


def make_custom_turtle(color: str | tuple | None = None,
                       new_pos: tuple | None = None,
                       pensize: int = 5,
                       do_dot: bool = True) -> Turtle:
    """
        This function creates a custom turtle for the needs of this module.
        :param color: The turtle's color.
        :param new_pos: The turtle's new position.
        :param pensize: The turtle's pensize
        :param do_dot: Determines if a dot is placed where the turtle is after creation.
        :return: The Turtle object set-up and ready to go!
        """
    new_turtle: Turtle = Turtle()
    new_turtle.hideturtle()
    new_turtle.pensize(pensize)

    if color:
        old_colormode: any = colormode()
        colormode(255)
        new_turtle.color(color)
        colormode(old_colormode)

    if new_pos:
        new_turtle.penup()
        new_turtle.goto(new_pos)
        new_turtle.pendown()

    if do_dot:
        new_turtle.dot(pensize)

    new_turtle.speed(0)
    new_turtle.speed(0)  # This repeated line makes sure when calling \
    # new_turtle.undo(), nothing essential will be undone.

    return new_turtle


default_liner_turtle: Turtle = make_custom_turtle(do_dot=False)
default_dotter_turtle: Turtle = make_custom_turtle(do_dot=False)
bezier_turtle: Turtle = make_custom_turtle('green', pensize=5, do_dot=False)
target1_turtle: Turtle = make_custom_turtle('black', pensize=1, do_dot=False)
target2_turtle: Turtle = make_custom_turtle('black', pensize=1, do_dot=False)
bezier_liner_turtle1: Turtle = make_custom_turtle('black', pensize=1, do_dot=False)
bezier_liner_turtle2: Turtle = make_custom_turtle('black', pensize=1, do_dot=False)
arc_turtle: Turtle = make_custom_turtle('black', pensize=1, do_dot=False)
arc_turtle.showturtle()


def setup_global_turtle(my_turtle: Turtle, new_position: tuple,
                        clean_latest_undo: bool = False) -> None:
    """
    This function can set up one of the global turtles from this function for the \
    turtle to be usable without remains from the previous 'drawing session.'
    :param my_turtle: The turtle to set up.
    :param new_position: The new position of the turtle.
    :param clean_latest_undo: Determines if the latest turtle's undo should be cleaned.
    """
    turtle_silent_move(my_turtle, new_position)
    if clean_latest_undo:
        turtle_clean_nearest_undo(my_turtle)


def make_line(line_start_pos: tuple, line_end_pos: tuple, line_color: any = None,
              color_mode: any = 255,
              liner_turtle: Turtle = default_liner_turtle) -> None:
    """
    This function draws a line on between the passed coordinates.
    :param line_start_pos: The line's first end
    :param line_end_pos: The line's second end
    :param line_color: The object passed as an argument to liner_turtle.color()
    :param color_mode: The color mode for the passed line_color
    :param liner_turtle: The turtle to draw the line.
    """
    setup_global_turtle(liner_turtle, line_start_pos)
    if line_color:
        colormode(color_mode)
        liner_turtle.color(line_color)
    liner_turtle.pendown()
    liner_turtle.goto(line_end_pos)


def make_dots(dots: tuple, dots_size: int = 10,
              dotter_turtle: Turtle = default_dotter_turtle) -> None:
    """
    :param dots: A tuple like this: ( and ) indicate a tuple.
    (
    (color, (x, y)),
    (color, (x, y))
    )
    :param dots_size: The size of the dots
    :param dotter_turtle: The turtle to make dots with (note: the turtle doesn't come \
    back to the original position, nor it keeps its old color.
    """

    dotter_turtle.penup()

    for dot_info in dots:
        dotter_turtle.color(dot_info[0])
        dotter_turtle.goto(dot_info[1])
        dotter_turtle.dot(dots_size)


def get_point_pos_from_line_percentage(end1: tuple, end2: tuple,
                                       progress: float) -> tuple:
    """
    :param end1: The line's first end position - tuple(x, y)
    :param end2: The line's second end position - tuple(x,y)
    :param progress: The decimal from 0 to 1 determining where on the line's length \
    is the point.
    :return: The position of the point on the line as an (x, y) tuple.
    """

    return (
        (end2[0] - end1[0]) * progress + end1[0],
        (end2[1] - end1[1]) * progress + end1[1]
    )


def turtle_silent_move(my_turtle: Turtle, position: tuple) -> None:
    """
    This function moves the turtle without drawing a line.
    :param my_turtle: The turtle to move.
    :param position: The position to move it to.
    """
    my_turtle.penup()
    my_turtle.goto(position)
    my_turtle.pendown()


def turtle_clean_nearest_undo(my_turtle: Turtle) -> None:
    """
    This function clears the passed turtle's first undo history item by moving it one \
    undo history space backwards.
    :param my_turtle: The turtle to clean the nearest undo for.
    """
    if my_turtle.isvisible():
        my_turtle.showturtle()
    else:
        my_turtle.hideturtle()


def draw_quadratic_bezier(fragments: int, target1_start_pos: (float, float),
                          target2_start_pos: (float, float),
                          end_pos: (float, float)) -> None:
    """
    This function draws a quadratic Bézier curve.
    :param fragments: The fragments (detail) of the curve
    :param target1_start_pos: The starting position of target 1 (the beginning of the \
    curve)
    :param target2_start_pos: The starting position of target 2 (the 'middle' of the \
    curve)
    :param end_pos: Curve end's position.
    """

    setup_global_turtle(bezier_turtle, target1_start_pos)
    setup_global_turtle(target1_turtle, target1_start_pos, clean_latest_undo=True)
    setup_global_turtle(target2_turtle, target2_start_pos, clean_latest_undo=True)
    setup_global_turtle(bezier_liner_turtle1, target1_start_pos)
    setup_global_turtle(bezier_liner_turtle2, target1_start_pos)

    bezier_turtle.dot(10)
    make_dots((('red', target2_start_pos), ('blue', end_pos)))

    for index, progress in enumerate((fragment / fragments
                                      for fragment in range(fragments + 1))):
        target1_pos: tuple = get_point_pos_from_line_percentage(target1_start_pos,
                                                                target2_start_pos,
                                                                progress)

        target2_pos: tuple = get_point_pos_from_line_percentage(target2_start_pos,
                                                                end_pos, progress)

        curve_pos: tuple = get_point_pos_from_line_percentage(target1_pos, target2_pos,
                                                              progress)

        if index % 2:  # Every other index
            bezier_liner_turtle1.goto(target1_pos)
            bezier_liner_turtle1.goto(target2_pos)
            bezier_liner_turtle2.undo()
        else:
            bezier_liner_turtle2.goto(target1_pos)
            bezier_liner_turtle2.goto(target2_pos)
            bezier_liner_turtle1.undo()

        target1_turtle.goto(target1_pos)
        target2_turtle.goto(target2_pos)
        bezier_turtle.goto(curve_pos)

        update()

    exitonclick()


def draw_arc(fragments: int, size: float, full_angle: float):
    """
    This function draws an arc in the middle of the turtle screen.
    :param fragments: The lines of the arc (how much detail) are
    :param size: The size of the arc
    :param full_angle: The arc's angle.
    :return:
    """

    def get_pos(fragment_angle: float) -> tuple:
        return (size * cos(fragment_angle),
                size * sin(fragment_angle))

    setup_global_turtle(arc_turtle, get_pos(0))

    one_fragment_angle = radians(full_angle / fragments)

    for angle in (one_fragment_angle * index for index in range(1, fragments + 1)):
        arc_turtle.goto(get_pos(angle))
    update()

    exitonclick()
