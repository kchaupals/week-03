import textwrap
'''
Task 2 for 03 Week of Learning Python

### Utils in Python

The utils were looked up in task description and on website w3schools -> Python 
'''

def str_lower(text):
    '''
    Method that converts a string to lowercase

    Returns:
        str: The modified string with all letters lowercased

    Example: 
        >>> text = "Python"
        >>> result = str_lower(text)
        python
    '''
    return text.lower()

def str_isspace(text):
    '''
    Method that checks if the string consists only of whitespace

    Returns:
        bool: True if all characters in the string are whitespace characters and there is at least one character; False otherwise.
    
    Example: 
        >>> text = " "
        >>> result = str_isspace(text)
        True
    '''
    return text.isspace()

def capitalize(text):
    '''
    Method that capitalizes the first letter of a predefined string

    Returns:
        str: The string with the first letter capitalized

    Example: 
        >>> text = "python"
        >>> result = str_capitalize(text)
        Python
    '''
    return text.capitalize()

def truncate(text, width = 30, placeholder = '[...]'):
    '''
    Method that shortens a predefined string to fit a specified with.

    Required Parameters:
        text (str): The input string that needs to be shortened
        width (int): The maximum width for the shorteneed string (default is 30)
        placeholder (str): A string to append at the end of truncated text. (default is "[...]")

    Returns:
        str: A shortened version of the string, ending with placeholder if it exceeds the width.

    Example:
        >>> text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum id faucibus eros."
        >>> result = str_textwrap(text, width = 30, placeholder = "...")
        Lorem ipsum dolor sit amet,...
    '''
    return textwrap.shorten(text, width = width, placeholder = placeholder)

def str_count(text, value):
    '''
    Method that counts occurrences of a substring in a string

    Required parameters:
        text (str): The string to value to search for
        value (str): The substring which occurrences method counts

    Returns:
        int: The number of  occurrences of the specified substring in the string

    Example:
        >>> text = "ababab"
        >>> result = str_count(text,"ab")
        3
    '''
    count = 0
    start = 0

    while True:
        start = text.find(value, start)

        if start == -1:
            break

        count += 1
        start += len(value)
    
    return count

def str_ljust(text, width, char = '-'):
    '''
    Method that is used to left-align a string by padding it with spaces (or a specified character) to a certain width. This can be useful for formatting text output.

    Required parameters:
        text (str): The string from which padding will be set
        width (int): The total width of the resulting string after padding. If the original string is longer than this width, it will return the string as it is.
    
    Optional parameters:
        char (str): The character to use for padding. (Default is a space (' '))

    Returns:
        str: A left-aligned string with the specified width
    
    Example: 
        >>> text = "Hello"
        >>> result = str_ljust(text, 30, '-')
        Hello-----

    '''
    return text.ljust(width, char)

def str_formatMap(text, map):
    '''
    Method to format strings using a mapping (like a dictionary)

    Required parameters:
        text (str): String with placeholders where dictionary values will be placed
        map (dict): A mapping object containing the keys and values for the placeholders in the string

    Returns:
        str: A new string with the placeholders replaced by the corresponding values from the mapping.

    Example: 
        >>> text = "Hello, {name}! Your age is {age} years."
        >>> map = {'name': 'Bob', 'age': 18}
        >>> result = str_formatMap(text, map)
        Hello, Bob! Your age is 18 years.
    '''
    return text.format_map(map)

def str_replace(text, old, new, count = -1):
    '''
    Method to replace occurrences of a specified substring within a string with another substring.

    Required parameters:
        oldvalue (str): The substring you want to replace
        newvalue (str): The substring with which to replace the old substring
    
    Optional parameters:
        count (int): The maximum number of occurrences to replace. (Default - all occurrences will be replaced)

    Returns:
        str: A new string with the specified substring replaced

    Example: 
        >>> text = "Hello, world! This is world of Python."
        >>> result = text.replace("world", "universe")
        Hello, universe! This is universe of Python.
    '''
    return text.replace(old, new, count)


def count_words(text = None):
    '''
    Method to count only letters in passed string

    Required parameters:
        text (str): The string in which you desire to count how many letters are
    
    Returns:
        int: Returns integer of how many letters were counted in passed string
    
    Example:
        >>> text = "Hello world!"
        >>> result = count_words(text)
        10
    '''
    if text is None:
        raise ValueError("You need to pass a parameter - string to execute this command.")

    if not isinstance(text, str):
        raise ValueError("Input must be a string.")
    
    return len(list(filter(str.isalpha, text)))

def is_prime(num):
    '''
    Method checks if passed int number is prime or not

    Required parameters:
        num (int): Integer number that will be check if it passes as prime number
    
    Returns:
        bool: Returns either True or False regarding int being prime number
    
    Example:
        >>> num = 2
        >>> result = is_prime(num)
        True
    '''
    if num < 0:
        raise ValueError("Prime number can't be passed as negative integer")
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) +1):
        if num % i == 0:
            return False
    return True

def factorial(n):
    '''
    Method that denotes factorial passed as integer

    Required parameters: 
        n (int): Integer number that is non-negative
    
    Returns:
        int: Returns factorial of input number 

    Example:
        >>> num = 5
        >>> factorial(5)
        120
    '''
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range (2, n + 1):
        result *= i
    return result

def total(nlist):
    '''
    Method that returns sum of the all items passed in list

    Required parameters:
        nlist (list): List of numbers integers

    Returns:
        int: Total sum of list items

    Example:
        >>> nlist = [1, 2, 3]
        >>> total(nlist)
        6
    '''
    if not isinstance(nlist, list):
        raise ValueError("Input must be a list of numbers")
    total = 0
    for num in nlist:
        if not isinstance(num, (int, float)):
            raise ValueError("All elements in the passed list must be numbers")
        total += num
    return total 

def average(nlist):
    '''
    Method that returns average of the passed list

    Required parameters:
        nlist (list): List of number integers

    Returns:
        int: Average of list

    Example: 
        >>> nlist = [1, 2, 3]
        >>> average(nlist)
        2
    '''
    if not isinstance(nlist, list):
        raise ValueError("Input must be a list of numbers")
    if len(nlist) == 0:
        raise ValueError("The list cannot be empty")
    
    total = 0
    for num in nlist:
        if not isinstance(num, (int,float)):
            raise ValueError("All elements in the passed list must be numbers")
        total += num

    return total / len(nlist)

def clamp(num, low, high):
    '''
    Method that limits number in specific range

    Required parameters:
        num (int/float): Integer which will be limited
        low (int/float): Integer of min range
        high (int/float): Integer of max range

    Returns:
        int or float: limited value

    Example:
        >>> clamp(15, 0, 10)
        10
        >>> clamp(-5, 0, 10)
        0
    '''

    return max(low, min(num, high))
    

if __name__ == "__main__":
   print("*** Utils demo ***")
   print(f'PYTHON -> str_lower("PYTHON") => {str_lower("PYTHON")}')
   print(f'" " passed to str_isspace(" ") => {str_isspace(" ")}')
   print(f'"name" passed to str_capitalize("name") => {capitalize("name")}')
   print(f'text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum id faucibus eros." passed to truncate(text) => {truncate("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum id faucibus eros.")}')
   print(f'If we count pairs of "ab" in "ababab" with str_count("ababab", "ab") => {str_count("ababab", "ab")}')
   print(f'If we want to set padding left with symbols, like Hello+++ -> str_ljust("hello", 15, "+") => {str_ljust("hello", 8, "+")} ')
   print(f'Having placeholder filled from dict -> str_formatMap(text, map) => {str_formatMap("Hello, {name}! Your age is {age} years.", {'name': 'Bob', 'age': 18})}')
   print(f'Replacing substring in string with str_replace(text, old, new) => {str_replace("Hello world! This is wonderful world!", "world", "universe")}')
   print(f'Counting letters in passed string like - "Hello world!" -> count_words("Hello world!") => {count_words("Hello world!")}')
   print(f'Validating if passed number is prime - as example 15 -> is_prime(15) => {is_prime(15)}')
   print(f'Providing number and getting factorial result - for example 5! -> factorial(5) => {factorial(5)}')
   print(f'Calculating total for lists, like this one [1,2,3] -> total([1,2,3]) => {total([1,2,3])}')
   print(f'Also for same list we can get average with -> average([1,2,3]) => {average([1,2,3])}')
   print(f'Last of the sets - setting limit for range with clamp -> clamp(20, 10, 30) => {clamp(20,10,30)}')
