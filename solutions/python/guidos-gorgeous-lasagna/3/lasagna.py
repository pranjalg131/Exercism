"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME=40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time: int):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers: int):
    """Calculate the preparation time for layers in lasagna.

    :param number_of_layers: int - number of layers in the lasagna.
    :return: int - preparation time for all layers (in minutes) derived from 'PREPARATION_TIME'.

    Function that takes the number of layers in lasagna as
    an argument and returns how many minutes will it take to prepare those layers
    based on the `PREPARATION_TIME`.
    """
    
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int):
    """Calculate the total time spent in making lasagna.

    :param number_of_layers: int - number of layers in the lasagna.
    :param elapsed_bake_time: int - time the lasagna has been in the oven (in minutes)
    :return: int - total time that is spent in making the lasagna.

    Function that takes the number of layers in lasagna and the time elapsed in the oven already as
    an argument and returns how many minutes have been spent in making the lasagna
    based on the `PREPARATION_TIME`.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time