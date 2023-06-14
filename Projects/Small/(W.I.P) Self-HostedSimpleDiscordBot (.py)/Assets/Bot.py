# Note that when launching bot.py directly the virtual environment won't be applied and the script might not work.


# 1. Setup
#  $$$$$$\             $$\
# $$  __$$\            $$ |
# $$ /  \__| $$$$$$\ $$$$$$\   $$\   $$\  $$$$$$\
# \$$$$$$\  $$  __$$\\_$$  _|  $$ |  $$ |$$  __$$\
#  \____$$\ $$$$$$$$ | $$ |    $$ |  $$ |$$ /  $$ |
# $$\   $$ |$$   ____| $$ |$$\ $$ |  $$ |$$ |  $$ |
# \$$$$$$  |\$$$$$$$\  \$$$$  |\$$$$$$  |$$$$$$$  |
#  \______/  \_______|  \____/  \______/ $$  ____/
#                                        $$ |
#                                        $$ |
#                                        \__|


import time
import os
import discord


# Make sure that the working directory is correct
# This is for emergency situations when bot.py has been launched directly.
if os.getcwd().split('\\')[-1] == 'Assets':
    os.chdir('./..')

TokenFile = r'.\Assets\Token.txt'
TokenFile_TextReadMode = open(TokenFile, 'rt')

TokenFile_FirstRead = TokenFile_TextReadMode.read()
TOKEN = TokenFile_FirstRead
TokenFile_TextReadMode.close()


def get_m_boundary(message_body, character='-'):
    longest_m_line_length = len(max(message_body.splitlines(), key=len))
    characters = ''

    for i in range(longest_m_line_length):
        characters += character

    return characters


def get_m_body(*lines):
    message = ''

    for i in range(len(lines) - 1):
        message += lines[i] + '\n'

    message += lines[-1]

    return message


def print_message(mode, boundary='', message='',):
    """
    modes:
        1 (default) - Print the entire message
        2 - Print only the first half (message_body and the first boundary)
        3 - Print only the second half (message_body and the second boundary)
        call(2, your_boundary) - Print only the first boundary
        call(3, your_boundary) - Print only the ending boundary
    """

    if boundary == '':
        boundary = get_m_boundary(message)

    if mode == 2:

        if message == '':
            to_print = ('\n' + boundary + '>')
        else:
            to_print = ('\n' + boundary + '>\n' + message)

    elif mode == 3:

        if message == '':
            to_print = ('<' + boundary)
        else:
            to_print = (message + '<\n' + boundary)

    else:
        to_print = ('\n' + boundary + '>\n' + message + '\n<' + boundary)

    print(to_print)


def print_wrong_answer(bad_answer, first_time, comment="None"):

    m1 = "Your answer wasn't accepted!"
    m2 = "Comment: " + comment

    if bad_answer == '':
        m3 = "Your answer was: You didn't write anything!"
    else:
        m3 = "Your answer was: " + bad_answer

    def shared_print_message():
        print_message(1, message=get_m_body(m1, m2, m3, m4))

    if first_time:
        m4 = "The question will be repeated in " + str(BadAnswer_SleepSeconds) + " seconds..."
        shared_print_message()
        time.sleep(BadAnswer_SleepSeconds)
    else:
        m4 = "The question will be repeated..."
        shared_print_message()


def ask_input(message):

    m_boundary = get_m_boundary(message)

    print_message(2, m_boundary, message)
    answer = input("\n: ")
    print_message(3, m_boundary)

    return answer


if len(TokenFile_FirstRead) <= 1:
    """m means message!"""
    BadAnswer_SleepSeconds = 3

    Answer1_FirstBad = True
    Answer2_FirstBad1 = True
    Answer2_FirstBad2 = True

    while True:
        
        Answer2_N_Selected = False

        m1_1 = "No token was found on the first line of " + TokenFile + '.'
        m1_2 = "The token You pass below will be saved to " + TokenFile
        m1_3 = "Please enter the token of Your Discord bot below."

        Answer1 = ask_input(get_m_body(m1_1, m1_2, m1_3))

        if len(Answer1) >= 1:

            while True:
                m3_1 = "Your bot will run with the token: " + Answer1
                m3_2 = "Is the above token Correct? Answer below. (Y/N)"

                Answer2 = ask_input(get_m_body(m3_1, m3_2)).lower()

                if Answer2 == "y":

                    m5_1 = "Saved the token."
                    m5_2 = "Continuing the script..."

                    print_message(1, message=get_m_body(m5_1, m5_2))

                    TokenFile_TextWriteMode = open(TokenFile, 'wt')
                    TokenFile_TextWriteMode.write(Answer1)
                    TokenFile_TextWriteMode.close()

                    break

                elif Answer2 == "n":

                    Answer2_N_Selected = True
                    
                    def m4_shared_print_message():
                        print_message(1, message=m4_1)

                    if Answer2_FirstBad1:
                        Answer2_FirstBad1 = False
                        m4_1 = "Repeating the question in 3 seconds..."
                        m4_shared_print_message()
                        time.sleep(BadAnswer_SleepSeconds)
                    else:
                        m4_1 = "Repeating the question..."
                        m4_shared_print_message()
                        
                    break

                else:
                    Answer2_FirstBad2 = False
                    print_wrong_answer(Answer2, Answer2_FirstBad2)

            if not Answer2_N_Selected:
                break

        else:

            print_wrong_answer(Answer1, Answer1_FirstBad)
            Answer1_FirstBad = False


# 2. The Discord Bot
# $$$$$$$\  $$\                                               $$\       $$$$$$$\             $$\
# $$  __$$\ \__|                                              $$ |      $$  __$$\            $$ |
# $$ |  $$ |$$\  $$$$$$$\  $$$$$$$\  $$$$$$\   $$$$$$\   $$$$$$$ |      $$ |  $$ | $$$$$$\ $$$$$$\
# $$ |  $$ |$$ |$$  _____|$$  _____|$$  __$$\ $$  __$$\ $$  __$$ |      $$$$$$$\ |$$  __$$\\_$$  _|
# $$ |  $$ |$$ |\$$$$$$\  $$ /      $$ /  $$ |$$ |  \__|$$ /  $$ |      $$  __$$\ $$ /  $$ | $$ |
# $$ |  $$ |$$ | \____$$\ $$ |      $$ |  $$ |$$ |      $$ |  $$ |      $$ |  $$ |$$ |  $$ | $$ |$$\
# $$$$$$$  |$$ |$$$$$$$  |\$$$$$$$\ \$$$$$$  |$$ |      \$$$$$$$ |      $$$$$$$  |\$$$$$$  | \$$$$  |
# \_______/ \__|\_______/  \_______| \______/ \__|       \_______|      \_______/  \______/   \____/


"sth"


# 3. End
# $$$$$$$$\                 $$\
# $$  _____|                $$ |
# $$ |      $$$$$$$\   $$$$$$$ |
# $$$$$\    $$  __$$\ $$  __$$ |
# $$  __|   $$ |  $$ |$$ /  $$ |
# $$ |      $$ |  $$ |$$ |  $$ |
# $$$$$$$$\ $$ |  $$ |\$$$$$$$ |
# \________|\__|  \__| \_______|

print_message(1, message="The end of the script has been reached!")
