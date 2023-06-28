"""
This script is the main script of the Discord bot.
With the help of other python scripts, this script does the following things:
    1. Continues the setup process from RunBotPhase2.ps1
    2. Runs the Discord Bot and handles its actions.
"""

from os import path, getcwd, chdir
import discord
from setup_module import setup_token, handle_bot_login_failure, handle_bot_bad_intents
from printing_utils import print_message
from bot import setup_discord_bot_events


def main() -> None:
    """This is the main functionality of the script."""

    # Make sure the working directory is correct
    # This is for emergency situations when this file has been launched directly.

    override_retry_exit_code: int = 1001

    if path.basename(getcwd()) == 'Assets':
        chdir(r'.\..')

    token: str = setup_token()

    print_message(1, message=f"TOKEN: '{token}' will be used...",
                  new_boundary_character="=")

    my_intents = discord.Intents.default()
    my_intents.message_content = True
    my_intents.members = True

    client = discord.Client(intents=my_intents)
    discord_errors = discord.errors

    setup_discord_bot_events(client)

    try:
        print('')
        client.run(token)
    except discord_errors.LoginFailure:
        handle_bot_login_failure()
    except discord_errors.PrivilegedIntentsRequired as bad_intents_error:
        handle_bot_bad_intents(str(bad_intents_error), override_retry_exit_code)


if __name__ == "__main__":
    main()
