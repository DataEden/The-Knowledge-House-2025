"""
This module contains functions for calculating basic statistical metrics.

The functions in this module are used to calculate the average, maximum, variance,
and standard deviation of a list of numbers. These functions are used in the
hr_monitoring_data_processing module to analyze heart rate data.

Functions:
    average(data: list) -> float:
    maximum(data: list) -> int:
    variance(data: list) -> float:
    standard_deviation(data: list) -> float:

"""

def average(data: list) -> float: # Define function header for average() function.
    """
    Calculate average value of a list of numbers from scratch.

    Function computes arithmetic mean of a list of integers or floats
    without using built-in functions like sum() or len(). If list is empty,
    it returns [] to avoid division by zero errors.

    Args:
        data (list[int | float]): A list of integers or floats representing numerical data.

    Returns:
        float: Average value of list as a floating-point number.

    Example and use:
        >>> average([1, 2, 3, 4, 5])
        3.0
        >>> average([])
        0.0
    """
    # Return empty list if no data in data list
    if not data:
        return []

    # Calculate sum of population in list
    sum_pop = 0
    for data_val in data: # Iterate over each element in list
        sum_pop += data_val # Add each element to sum

    # Calculate number of population in list
    num_pop = 0
    for data_val in data: # Iterate over each element in list
        num_pop += 1
    sample_mean = sum_pop / num_pop # Calculate average of list
    
    return sample_mean  


def maximum(data: list) -> float: # Define function header for maximum() function.
    """
    Calculate maximum value in a list of numbers.

    Args:
        data (list): A list of numbers (ints or floats).

    Returns:
        float: Maximum value in list.
    None: If list is empty.    
    """
    if not data:
        return [] # Return empty list if no data in data list
         
    max_value = data[0] # Initialize max_value to first element in list
    for value in data:
        if value > max_value: # Compare each element with max_value
            max_value = value # Update max_value if value is greater
    return max_value # Return the maximum value to calling function(s)


def variance(data: list) -> float: # Define function header for variance() function.
    """
    Computes the population variance of a list of numbers using basic syntax.

    Args:
        data (list): A list of numbers.

    Returns:
        float: The variance, or 0 if the list is empty.
    """
    if not data:
        return []  # Return empty list[].

    n = len(data)  # Get the number of elements.

    # Manually compute mean value.
    mean = 0
    for value in data:
        mean += value
    mean /= n  # Divide by n to get the mean.

    # Manually Compute variance.
    sum_sq_diff = 0
    for value in data:
        sum_sq_diff += (value - mean) ** 2  # Squaring each difference.

    variance = sum_sq_diff / n  # Divide to obtain population variance.

    return variance # Return calculated variance to calling function(s).


def standard_deviation(data: list) -> float:  # Define function header for standard_deviation() function.
    """
    Calculates the population standard deviation using variance function.

    Args:
        data (list): A list of numbers.

    Returns:
        float: The standard deviation.
    """
    if not data:
        return [] # Return empty list if no data in data list.
    
    return variance(data)**0.5  # Return square root of variance / Standard deviation.
    