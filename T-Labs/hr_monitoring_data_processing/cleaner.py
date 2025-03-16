# define function header for filter_nondigits() function.
def filter_nondigits(data: list) -> list:
    """
    filter_nondigits() takes in a list of strings and filters
    out all strings that include non-integer elements.

    Args:    
        data (list): A list of strings elements.

    Returns:
        list: A list of strings of type int elements.          
    """    
    
    clean_list = []  # Initialize empty list to store permissible elements.
    for element in data:  # Iterate over list of strings.
        # remove any \n, \t, " ", etc.., from string(s).
        clean_element = element.strip()
        # Check if element is a digit.        
        if clean_element.isdigit():  
            clean_list.append(int(element))  # Convert string to permissible element and append to list.
    return clean_list  # Return list of permissible elements.


