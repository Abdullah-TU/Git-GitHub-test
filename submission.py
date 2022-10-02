"""
How Many abbas?
Implement the function count_abbas, 
which returns the number of abbas (meaning the string "abba") that 
the parameter string contains.
"""

def count_abbas(bla):
    """
    Initialize 'abba' and using for loop to find out how many 'abba' in the parameter.
    Finally stored in a list and count how many abbas are in the list.

    :param strnings: str,  string analyzed.
    :return: int, how many abbas are in the list.
    """
       
    cnt = 0
    idx = 0
    while True:
        idx = bla.find('abba', idx)
        if idx >= 0:
            cnt += 1
            idx += 1
        else:
            break
    return cnt      
 
count_abbas('barbapapa')