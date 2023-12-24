# TODO: Overview

"""Simple script to get all combinations with repeats of an array."""

from math import ceil


def list_my_list(my_list: list) -> list:
    """If the input was [1,2,3], the output would be [[1], [2], [3]]"""
    my_listed_list: list = []

    for item in my_list:
        my_listed_list.append([item])

    return my_listed_list


def get_combinations(my_list: list, size: None | int = None) -> list:
    """
    :param my_list: The array to generate all combinations of selected size \
    for
    :param size: The size of generated combinations. (Default: the length of my_list) \
    The size cannot be bigger than len(my_list)!!!
    :return: All generated combinations according to the passed arguments. The length \
    of the returned combinations list should be: len(my_list) ** size
    """

    size: int = size or len(my_list)

    if size > len(my_list):
        raise ValueError("The value of size passed to the function cannot be greater "
                         "than the length of the passed list!")

    my_list: list = list_my_list(my_list)

    def add_one_combination_depth(current_combination: list) -> list:
        deeper_combinations: list = []

        for item_to_append in my_list:
            deeper_combinations.append(current_combination + item_to_append)
        return deeper_combinations

    def recursively_add_one_combination_depth(current_combinations: list) -> list:
        if len(current_combinations[0]) < size:

            new_combinations: list = []

            for combination in current_combinations:
                new_combinations += add_one_combination_depth(combination)

            return recursively_add_one_combination_depth(new_combinations)

        return current_combinations

    return recursively_add_one_combination_depth(my_list)


if __name__ != '__main__':
    my_size: int = 4
    my_array: list = [1, 2, 3, 4]

    my_combinations: list = get_combinations(my_array, size=my_size)

    print(f"My Array: {my_array}"
          f"\nThe size of each combination: {my_size}"
          f"\nCombinations:\n")

    for i in range(1, ceil((len(my_combinations)/my_size) + 1)):
        print(*my_combinations[my_size * (i - 1): my_size * i])

    print(f"\nEnd! - {len(my_combinations)} Combinations!")

else:
    print(*get_combinations(['North', 'East', 'West', 'South'], size=3), sep='\n')

p