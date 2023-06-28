r"""
This function should be run before committing this project using GIT.

If clears the following files:
    - '.\Assets\Token.txt'
"""

from os import chdir, getcwd, remove
from shutil import rmtree


def main():
    """This is the main functionality of this script."""

    chdir(r'.\..')
    current_working_directory = getcwd()
    print(f'\nCurrent Working Directory: {current_working_directory}'
          '\n\nPreparing for the commit...')

    files_to_clear: list = [
        r'.\Assets\Token.txt'
    ]

    files_to_delete: list = [

    ]

    folders_to_delete: list = [
        r'.\Assets\__pycache__'
    ]

    def shared_ignored_exception_message(exception):
        print(f'\n ! Ignored exception: {exception}')

    for file_to_clear in files_to_clear:

        try:
            with open(file_to_clear, 'wt', encoding='utf-8') as file_write_mode:
                file_write_mode.write('')
            print(f'\n - Cleared {file_to_clear}')

        except Exception as my_exception:
            shared_ignored_exception_message(my_exception)

    for file_to_delete in files_to_delete:

        try:
            remove(file_to_delete)
            print(f'\n - Deleted file: {file_to_delete}')

        except Exception as my_exception:
            shared_ignored_exception_message(my_exception)

    for folder_to_delete in folders_to_delete:

        try:
            rmtree(rf'{current_working_directory}{folder_to_delete[1:]}')
            print(f'\n - Deleted folder: {folder_to_delete}')

        except Exception as my_exception:
            shared_ignored_exception_message(my_exception)

    print("\nFinished preparing for the commit!")


if __name__ == '__main__':
    main()
