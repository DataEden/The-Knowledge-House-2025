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
    
    if not data:
        return []
  
    clean_list = []  # Initialize empty list to store permissible elements.
    for val in data:  # Iterate over list of strings.
        # remove newline characters from the string.
        clean_element = val.strip()
        # Check if element is a digit.        
        if clean_element.isdigit():  
            clean_list.append(int(val))  # Convert string to permissible element  and append list.
    return clean_list  # Return list of permissible elements.
    