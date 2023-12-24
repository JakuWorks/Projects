r"""
This module is used to help the main script continue the setup process of setting up \
the bot.

This process goes in the below order:
    ('.\' is the main project folder)
    .\RunBot.bat ->
    -> .\Assets\RunBotPhase2.ps1 ->
    -> .\Assets\main.py (with the help of this module
"""

from sys import exit as sys_exit
from time import sleep
from printing_utils import ask_input, print_wrong_answer, print_message, get_m_body, \
    ask_bool_input, answers_positive, answers_negative, get_m_boundary
from token_functions import try_get_saved_token, save_token
from project_config_shadow import config, config_main, ClearTokenIfBad, ConfigPath, \
    n_token_encrypted


def setup_token() -> str:
    """
    Notes:
    - 'm' in variable/function names means 'message'
    - 'a' in variable/function names means 'answer'

    This function gets the token by two means:
        1. Checks if it is in the token file
        2. Asks the user to input the token (and then saves it to the token file)
    :return: The token of the Discord bot.
    """

    token_file_first_read: str = try_get_saved_token()

    def user_questionnaire() -> str:

        a1_first_bad: bool = True
        a2_first_bad1: bool = True
        a2_first_bad2: bool = True

        def ask_for_token() -> str:
            m1_1: str = f"No token was found in {ConfigPath}."
            m1_2: str = f"The token You pass below will be saved to {ConfigPath}"
            m1_3: str = "Please enter the token of Your Discord bot below."
            return ask_input(get_m_body(m1_1, m1_2, m1_3))

        def ask_is_passed_token_correct() -> str:
            m2_1: str = f"Your bot will run with the token: {answer1}"
            m2_2: str = "Is the above token Correct? Answer below. " \
                        f"({answers_positive[0]}/{answers_negative[0]})"
            return ask_bool_input(m2_1, m2_2)

        def process_a2_is_positive() -> None:
            m3_1: str = "Saving the token and continuing the script..."
            print_message(1, message=m3_1)

        def process_a2_is_negative() -> None:
            nonlocal a2_first_bad1

            if a2_first_bad1:
                m4_wait_seconds: int = 3
                a2_first_bad1 = False
                print_message(1, message=f"Repeating the question in {m4_wait_seconds} "
                                         "seconds...")
                sleep(m4_wait_seconds)
            else:
                print_message(1, message="Repeating the question...")

        def process_a2_is_incorrect() -> None:
            nonlocal a2_first_bad2

            print_wrong_answer(answer2, comment="Your answer was not 'Y', nor 'N'",
                               do_wait=a2_first_bad2)
            a2_first_bad2 = False

        def process_a1_is_too_short() -> None:
            nonlocal a1_first_bad
            a1_too_short_comment = "Your token has to be at least 1 character long!"
            print_wrong_answer(answer1, comment=a1_too_short_comment,
                               do_wait=a1_first_bad)
            a1_first_bad = False

        while True:

            answer1 = ask_for_token()

            if len(answer1) >= 1:

                while True:

                    a2_is_positive, answer2 = ask_is_passed_token_correct()

                    if a2_is_positive:
                        process_a2_is_positive()
                        return answer1

                    if not a2_is_positive:
                        process_a2_is_negative()
                        break

                    if a2_is_positive is None:
                        process_a2_is_incorrect()

            else:
                process_a1_is_too_short()

    if len(token_file_first_read) <= 1:
        token: str = user_questionnaire()
        save_token(token_file_first_read)
        return token

    return token_file_first_read


def handle_bot_login_failure() -> None:
    """
    This function writes a message to the console about the \
    discord.errors.LoginFailure error that has occurred. It also clears the file with \
    the token so that the next launch of the script will ask for the correct token.
    """

    m_1: str = "Improper token has been passed!"

    if ClearTokenIfBad:
        m_2: str = "Cleared the passed Discord Bot Token and restarting the script " \
                   "to avoid further errors."

        print_message(1, message=get_m_body(m_1, m_2), new_boundary_character='=',
                      new_lines_before_first_boundary=3)

        with open(ConfigPath, 'w', encoding='utf-8') as token_file_wt:
            config_main[n_token_encrypted] = ''
            config.write(token_file_wt)

    else:
        print_message(1, message=m_1)


def handle_bot_bad_intents(error_message: str, override_retry_exit_code: int) -> None:
    """
    This function writes a message to the console about the \
    discord.errors.PrivilegedIntentsRequired error that has occurred.
    :param error_message: The error message that Discord has written.
    :param override_retry_exit_code: This is the exit code that will be sent and \
    named as "OverrideRetry" in the print.
    """
    m1_1: str = "Your token is correct, but You haven't enabled the correct " \
                "Intents in the configuration of Your bot. You have to enable them " \
                "before running the bot again."
    m1_2: str = "\nThe Intents that have to be enabled:"
    m1_3: str = " - SERVER MEMBERS INTENT"
    m1_4: str = " - MESSAGE CONTENT INTENT"
    m1_5: str = "\nDiscord's error message:"
    m1_6: str = f"    {error_message}"

    m_body_for_boundary: str = get_m_body(m1_1, m1_2, m1_3, m1_4, m1_5)
    m_boundary: str = get_m_boundary(m_body_for_boundary, '=')

    print_message(1, m_boundary, get_m_body(m_body_for_boundary, m1_6),
                  new_lines_before_first_boundary=3)

    print("\nExit Code:\n{override_retry_exit_code} - OverrideRetry")

    sys_exit(override_retry_exit_code)
