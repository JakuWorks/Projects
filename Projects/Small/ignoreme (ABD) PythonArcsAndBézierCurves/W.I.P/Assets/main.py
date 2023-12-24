"""
This script asks the user to define what He wants to draw (arc or Bezier) and then \
draws it.
"""

from math import isinf
from shutil import get_terminal_size
from time import sleep
from typing import Union


def clear_terminal() -> None:
    """
    This function prints new lines into the terminal to make it look like it has \
    been cleared.
    """
    print('\n' * get_terminal_size().lines, end='')


def process_input_to_float(user_input_string: str,
                           float_min: float,
                           float_max: float,
                           can_be_equal: bool = True,
                           allow_infinity: bool = False) -> float | None:
    """
    :param user_input_string: The raw string that the user has inputted.
    :param float_min: The minimum value of the generated float, before it is incorrect
    :param float_max: The maximum value of the generated float, before it is incorrect.
    :param can_be_equal: Determines if the float can be equal to float_min and \
    float_max and still be accepted
    :param allow_infinity: Determines if the generated float can be math.inf and be \
    accepted
    :return: The generated float or None if it couldn't be generated.
    """
    user_input_processed: str = ''

    # Filtering for digits only (this also removes newlines)
    for character in user_input_string:
        if character.isdigit() or character == ',' or character == '.':
            user_input_processed += character

    user_input_processed: str = user_input_processed.replace(',', '.')
    user_input_processed: str = user_input_processed.replace(' ', '')

    try:
        my_float = float(user_input_processed)
    except ValueError:
        return None

    if not allow_infinity and isinf(my_float):
        return None

    if can_be_equal:
        if my_float < float_min or my_float > float_max:
            return None
    elif my_float <= float_min or my_float >= float_max:
        return None

    return my_float


def ask_until_correct_input_wrap(first_message: str,
                                 retry_message: str,
                                 callable_to_handle_input: callable,
                                 callable_to_check_is_answer_good: callable) \
        -> FunctionType:
    """
    This is a function that wraps
    :param first_message: This is usually the 'question' sent to the user. It is just \
    what is printed before the input 'box.'
    :param retry_message: This message is printed when the user fails to give a \
    correct answer.
    :param callable_to_handle_input: This function will handle the input() function \
    and the additional processing to the answer.
    :param callable_to_check_is_answer_good: This function will handle checking if the \
    answer provided by the user can be accepted or declined.
    :return: A function that handles asking the user for input until the input is \
    correct.
    """

    def wrap() -> any:
        clear_terminal()
        print(first_message)
        processed_input: any = callable_to_handle_input()

        while not callable_to_check_is_answer_good(processed_input):
            clear_terminal()
            print(retry_message)
            sleep(0.3)
            print('\n' + first_message)
            processed_input = callable_to_handle_input()

        return processed_input

    return wrap


def ask_until_option_input(options_tuple: tuple,
                           first_message: str,
                           retry_message: str) -> str:
    """
    :param options_tuple: The tuple of options that can be chosen.
    :param first_message: This is usually the 'question' sent to the user. It is just \
    what is printed before the input 'box.'
    :param retry_message: This message is printed when the user fails to give a \
    correct answer.
    :return: The string of the selected option.
    """

    return ask_until_correct_input_wrap(
        first_message,
        retry_message,
        lambda: input(f" - Possible Options: {', '.join(options_tuple)}"
                      f"\n  Your Option: "),
        lambda processed_input: processed_input in options_tuple
    )()


def ask_until_float_input(first_message: str,
                          retry_message: str,
                          float_min: float or None = None,
                          float_max: float or None = None) -> float:
    """
    :param first_message: This is usually the 'question' sent to the user. It is just \
    what is printed before the input 'box.'
    :param retry_message: This message is printed when the user fails to give a \
    correct answer.
    :param float_min: The minimum value of the generated float, before it is incorrect
    :param float_max: The maximum value of the generated float, before it is incorrect.
    :return: The float inputted by the user.
    """

    return ask_until_correct_input_wrap(
        first_message,
        retry_message,
        lambda: process_input_to_float(input("  Your Input: "),
                                       float_min=float_min,
                                       float_max=float_max),
        lambda processed_input: processed_input is not None
    )()


def ask_quadratic_bezier() -> callable:
    """
    This function asks the user to specify the quadratic bezier's mode, and then \
    returns a function to draw the curve.
    :return:
    """
    m1_1: str = "Please Select a Mode: " \
                "\n 1 - Custom - Lets customise all positions." \
                "\n 2 - Preview - All positions are preset." \
                "\n 3 - Full Random - All positions are random." \
                "\n\n To select a Mode, type its number from the list and press enter."

    m1_error1: str = "No mode found! Please answer again correctly!"

    m2_error1: str = "Wrong input passed! Try Again!"

    bezier_positions_mode: str = ask_until_option_input(('1', '2', '3'),
                                                        m1_1, m1_error1)

    if bezier_positions_mode == "1":

        max_position: float = 400

        ask_pattern: callable = lambda question_subject, axis: ask_until_float_input(
            f"Input {question_subject} Position {axis} "
            f"(a number between -{max_position} and {max_position}.",
            m2_error1, -max_position, max_position)

        ask_both_axis: callable = lambda question_subject: (
            ask_pattern(question_subject, "X"), ask_pattern(question_subject, "Y"))

        starting_position: tuple = ask_both_axis("Staring Point")
        control_point: tuple = ask_both_axis("Control Point")
        end_position: tuple = ask_both_axis("End")

        print("DONE!")


ask_quadratic_bezier()
