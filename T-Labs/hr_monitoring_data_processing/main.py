"""
The main Python mpdule that combines cleaner and metrics functions in order to
perform comprehensive analysis
"""

from metrics import average, maximum, standard_deviation
from cleaner import filter_nondigits

import matplotlib.pyplot as plt


def run(filename: str) -> None:
    """
    Process heart rate data from the specified file, clean it, calculate metrics,
    and save visualizations.

    Args:
        filename (str): The path to the data file (e.g., 'data/phase0.txt').

    Returns:
        float, float, float: You will return the average, max, and standard deviation
    """ 
    data = []

    # open file using file I/O and read it into the `data` list
    ...

    # Use `filter_nondigits` to clean the data and remove invalid entries, save the output to a new variable
    ...

    # plot this data to explore changes in heart rate for this file, save this visualization to the "images" folder
    ...

    # calculate the average, maximum, and standard deviation of this file using the functions you've wrote
    avg_hr = ...
    max_hr = ...
    std_dev_hr = ...

    # return all 3 values
    return avg_hr, max_hr, std_dev_hr


if __name__ == "__main__":
    print(run("data/phase0.txt"))
