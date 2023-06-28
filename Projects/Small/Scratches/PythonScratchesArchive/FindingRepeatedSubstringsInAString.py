"""
----------------------------------------------------------------------------------------
  OVERVIEW


  Date created: 18.06.2023
  This is a simple script I made for a StackOverflow answer. It finds all repeated \
  substrings of the passed string with the passed size and minimum repeats count.


----------------------------------------------------------------------------------------
"""


from collections import Counter


def main():

    def find_unique_repeat_substrings(my_string: str, min_size: int = 2,
                                      min_repeats: int = 2) -> list:
        r"""
        This function gets all substrings of a string and returns a list with all \
        unique substrings that got repeated at least min_repeats times.
        :param my_string:(str) String to make all substrings from.
        :param min_size:(int) Minimum size of a substring
        :param min_repeats:(int) The minimum amount of repeats of a substring for it \
        to be counted as a unique substring
        :return:(list) All unique substrings of a string that occurred more than \
        min_repeats times.
        """
        substrings = []
        my_string_len = len(my_string)

        # Generating all possible sizes of a string. In example, from 'str' it'd \
        # be 1, 2 and 3 if min_size was 1. If min_size was 2 it'd be 2 and 3.
        for size in range(min_size, my_string_len + 1):  # If You don't want to count \
            # the entire string as a substring, just remove the '+1'
            # Generate all possible slices of that string with the passed size.
            for index in range(my_string_len + 1 - size):
                substrings.append(my_string[index:index + size])

        # Filtering the substrings that don't comply to min_repeats.
        return [substring for substring, count in Counter(substrings).items()
                if count >= min_repeats]

    my_lorem_ipsum = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Praesent tristique magna sit amet purus gravida quis blandit. Imperdiet sed euismod nisi porta lorem. Vel quam elementum pulvinar etiam non quam. Proin nibh nisl condimentum id. Mi eget mauris pharetra et ultrices. In vitae turpis massa sed. Elementum sagittis vitae et leo duis. Feugiat in ante metus dictum at tempor commodo ullamcorper a. Tortor aliquam nulla facilisi cras. Dui nunc mattis enim ut tellus. Congue mauris rhoncus aenean vel elit scelerisque mauris pellentesque. Morbi tincidunt augue interdum velit euismod.Ut tellus elementum sagittis vitae et leo duis ut diam. Sollicitudin tempor id eu nisl nunc. In ante metus dictum at tempor commodo. Ultrices vitae auctor eu augue ut lectus arcu. Turpis in eu mi bibendum. In egestas erat imperdiet sed euismod. Accumsan sit amet nulla facilisi morbi tempus iaculis. Nisi lacus sed viverra tellus in. Velit egestas duid ornare. Cras pulvinar mattis nunc sed blandit libero volutpat sed cras. Varius vel pharetra vel turpis. Tristique senectus et netus et malesuada.'
    print(find_unique_repeat_substrings(my_lorem_ipsum, 4, 4))


if __name__ == '__main__':
    main()
