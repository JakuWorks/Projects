"""
This module was created by me to simplify the process of printing messages into the
terminal.
"""


from time import sleep


answers_positive: list = ["Y", "Yes", "Yea"]
answers_negative: list = ["N", "No", "Nah"]

answers_positive_lower: list = [*map(str.lower, answers_positive)]
answers_negative_lower: list = [*map(str.lower, answers_negative)]


def get_m_boundary(message_body: str, character: str = '=') -> str:
    """
    :param message_body: A block of text to generate the boundary for.
    :param character: The character to make the boundary's body of.
    :return: A boundary body i.e. '====' of the same length as the longest line \
    of message_body.
    """

    longest_line_length: int = len(max(message_body.splitlines(), key=len))
    boundary_body: str = character * longest_line_length
    return boundary_body


def get_m_body(*lines: str) -> str:
    """
    :param lines: The lines of text to merge
    :return: The passed lines merged into one block of code.
    """

    return '\n'.join(lines)


def print_message(mode: int = 1, boundary_body: str = '', message: str = '',
                  new_boundary_character: str = '-',
                  new_lines_before_first_boundary: int = 1) -> None:
    r"""
    Note: If the message is empty, only the boundaries will be printed. This is useful \
    with modes 2 and 3.
    :param mode: 1-the first boundary+message+second boundary; 2-first boundary+\
    message; 3-message+second boundary
    :param boundary_body: the body of the boundary i.e. '------'
    :param message: the message to print, without the boundaries
    :param new_boundary_character: if the boundary was not passed, this will be \
    the boundaries body character
    :param new_lines_before_first_boundary: This is the amount of newlines written \
    before the first boundary
    :return:Nothing, this function only prints.
    """

    if not boundary_body:

        if message:
            boundary_body: str = get_m_boundary(message, new_boundary_character)
        else:
            print()
            return

    new_lines: str = '\n' * new_lines_before_first_boundary
    first_boundary: str = f'{new_lines}{boundary_body}>'
    second_boundary: str = f'<{boundary_body}'

    if mode == 1:

        if message:
            print(f"{first_boundary}\n{message}\n{second_boundary}")
        else:
            print(f"{first_boundary}\n{second_boundary}")

    elif mode == 2:

        if message:
            print(f"{first_boundary}\n{message}")
        else:
            print(f"{first_boundary}")

    elif mode == 3:

        if message:
            print(f"{message}\n{second_boundary}")
        else:
            print(f"{second_boundary}")


def print_wrong_answer(bad_answer: str, comment: str = "None", do_wait: bool = None,
                       wait_seconds: float = 3) -> None:
    """
    :param do_wait: Should the script wait the wait_seconds
    :param bad_answer: The user's bad answer.
    :param comment: Comment of the bad answer.
    :param wait_seconds: How long should the script wait after printing if \
    'do_wait' is true.
    :return:Nothing, this function only prints.
    """

    message1: str = "Your answer was rejected!"
    message2: str = f"Comment: {comment}"

    if bad_answer:
        message3: str = f"Your answer was: {bad_answer}"
    else:
        message3: str = "Your answer was: You didn't write anything!"

    def shared_print_message() -> None:
        print_message(1, message=get_m_body(message1, message2, message3, message4))

    if do_wait:
        message4: str = f"The question will be repeated in {wait_seconds} seconds..."
        shared_print_message()
        sleep(wait_seconds)
    else:
        message4: str = "The question will be repeated..."
        shared_print_message()


def ask_input(question: str) -> str:
    """
    :param question: The message that should tell the user what question is He \
    answering.
    :return: The user's answer.
    """

    m_boundary: str = get_m_boundary(question)

    print_message(2, m_boundary, question)
    answer: str = input("\n ")
    print_message(3, m_boundary)

    return answer


def ask_bool_input(*question_lines: str) -> bool or None:
    """
    :param question_lines: These are the lines of the question to be printed.
    :return: Bool if answer was pos/negative, None if it was \
    incorrect,
    """

    answer = ask_input(get_m_body(*question_lines))
    a_lower = answer.lower()

    boolean = True if a_lower in answers_positive_lower \
        else False if a_lower in answers_negative_lower else None
    return [boolean, answer]
