"""
This module handles most of the bots' actions. It also uses responses.py to generate \
the bots' responses.
"""


import discord
from responses import get_response
from printing_utils import print_message


def setup_discord_bot_events(client: discord.Client) -> None:
    """
    :param client: This is the Discord client that will have its \
    events set-up.
    """

    def process_message(message_string: str) -> (int, str) or (None, None):
        """
        Prefix '!' — 'response_mode' 1 — the bot will respond where the user sent the \
        message.
        Prefix '?!' — 'response_mode' 2 — , the bot will respond in private to the \
        user who sent the message.
        :param message_string: The entire message string sent by the user.
        :return: The response_mode and command extracted \
        from the message, or None if the script couldn't extract them.
        """

        message_string_len = len(message_string)

        if message_string_len >= 2:

            if message_string[0] == '!':
                return 1, message_string[1:].lower()

            if message_string_len >= 3 and message_string[:2] == r'?!':
                return 2, message_string[2:].lower()

        return None, None

    client_user = client.user

    @client.event
    async def on_ready() -> None:
        """
        This function sends a debug message when the Discord Bot is running.
        """

        nonlocal client_user
        client_user = client.user

        print_message(1, message=f"{client_user} is now running!")
        print("\nLog:\n")

    @client.event
    async def on_message(message: discord.Message) -> None:
        """
        This function detects when a message has been sent
        """
        if message.author == client_user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said in {channel}: \"{user_message}\"")

        response_mode, command = process_message(user_message)

        if not response_mode or not command:
            return

        response: str or None = get_response(message, command)

        if not response:
            return

        if isinstance(response, str):

            print(f"\nResponding with:\n{' '.join(response.splitlines())}\n")

            if response_mode == 1:
                await message.channel.send(response)
            elif response_mode == 2:
                await message.author.send(response)
