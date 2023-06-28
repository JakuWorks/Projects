"""
This module is used to generate the responses of the Discord Bot.
"""

from math import floor
from operator import itemgetter
from random import randint
import discord
from helper_functions import remove_non_letters_in_string, find_ints_in_string


def get_response(message: discord.Message, user_command: str) -> str or None:
    """
    This function returns a string response for the passed message and command.
    :param message: The message the user sent.
    :param user_command: The lowercase string of the user's message, without the \
    prefix.
    :return: If the command argument matched any of the commands, then a \
    string of the response, if not, then None.
    """

    commands: dict = {}

    def set_command_aliases(command_function: callable, aliases: list) -> None:
        for alias in aliases:
            commands[alias] = command_function

    def set_command(my_function: callable) -> None:
        commands[my_function.__name__[1:]] = my_function

    @set_command
    def _help() -> str:
        pass  # TODO

    @set_command
    def _hello() -> str:
        return "Hey there!"

    set_command_aliases(_hello, ["Hi"])

    @set_command
    def _roll() -> str:
        numbers: list = find_ints_in_string(user_command)
        numbers_len: int = len(numbers)

        default_first: int = 1
        default_second: int = 6

        def get_roll_results_message(minimum: int, maximum: int) -> str:
            return f"A random number from {minimum} to {maximum} is " \
                   f"{randint(minimum, maximum)}"

        return '\n'.join([get_roll_results_message(numbers[i] or default_first,
                                                   numbers[i+1:i+2] or default_second)
                          for i in range(numbers_len[::2])])

    @set_command
    def _account_ages_leaderboard() -> str:
        all_members: list = [[member.id, member.created_at.timestamp()]
                             for member in message.guild.members]

        all_members.sort(key=itemgetter(1))

        lines: list = []

        for i, member in enumerate(all_members):
            timestamp: int = floor(member[1] + 0.5)
            lines.append(f"{i}. Member: <@{member[-1]}>, "
                         f"Relative Time: <t:{timestamp}:R>, "
                         f"Long Date: <t:{timestamp}:F>, "
                         f"Raw Timestamp: {timestamp}")

        head: str = "A list of all members sorted by their account creation timestamp:"

        return '\n'.join([head, *lines])

    for command_name, action in commands:
        command_name_len: int = len(command_name)
        user_command_slice: str = user_command[:command_name_len]

        if command_name == user_command_slice or \
                command_name == remove_non_letters_in_string(user_command_slice):
            return action()
