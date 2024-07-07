def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.

    Args:
        list_of_integers (list): List of integers to search for a peak.
        
    Returns:
        int: A peak element from the list. Returns None if the list is empty.
    """
    if not list_of_integers:
        return None
    
    left, right = 0, len(list_of_integers) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # Check if mid is a peak
        if (mid == 0 or list_of_integers[mid] >= list_of_integers[mid - 1]) and \
           (mid == len(list_of_integers) - 1 or list_of_integers[mid] >= list_of_integers[mid + 1]):
            return list_of_integers[mid]
        
        # If the left neighbor is greater, search left
        elif mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
            right = mid - 1
        
        # Otherwise, search right
        else:
            left = mid + 1
    
    return None
