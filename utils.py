import textwrap
'''
Task 2 for 03 Week of Learning Python

### Utils in Python

The utils were looked up in task description and on website w3schools -> Python 
'''

def string_lower():
    '''
    Method that converts a tring to lowercase

    Returns:
        str: The modified string with all letters lowercased

    Example: 
        >>> text = "Python"
        >>> result = text.lower()
        >>> print(result)
        python
    '''
    text = "Python"
    return text.lower()

def string_isspace():
    '''
    Method that checks if the string consists only of whitespace

    Returns:
        bool: True if all characters in the string are whitespace characters and there is at least one character; False otherwise.
    
    Example: 
        >>> text = " "
        >>> result = text.isspace()
        >>> print(result)
        True
    '''
    text = " "
    return text.isspace()

def string_capitalize():
    '''
    Method that capitalizes the first letter of a predefined string

    Returns:
        str: The string with the first letter capitalized

    Example: 
        >>> text = "python"
        >>> result = text.capitalize()
        >>> print(result)
        Python
    '''
    text = "python"
    return text.capitalize()

def string_textwrap():
    '''
    Method that shortens a predefined string to fit a specified with.

    Required Parameters:
        text (str): The input string that needs to be shortened
        width (int): The maximum width for the shorteneed string (default is 30)

    Optional parameters:
        fix_sentence_endings (bool): When True, it ensures that the text ends with proper sentence ending. (default is False)
        break_long_words (bool): When True, long words will be broken to fit within the width. (default is True)
        break_on_hyphens (bool): When True, hyphenated words will be broken at the hyphen. (default is True)
        placeholder (str): A string to append at the end of truncated text. (default is "[...]")

    Returns:
        str: A shortened version of the string, ending with placeholder if it exceeds the width.

    Example:
        >>> text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum id faucibus eros."
        >>> result = textwrap.shorten(text, width = 30, placeholder = "...")
        >>> print(result)
        Lorem ipsum dolor sit amet,...
    '''
    text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum id faucibus eros." 
    return textwrap.shorten(text, width = 30, placeholder = "...")

def string_count():
    '''
    Method that counts occurrences of a substring in a string

    Required parameters:
        value (str): The string to value to search for

    Optional parameters:
        start (int): The position to start the search. (Default is 0)
        end (int): The position to end the search. (Default is the end of the string)

    Returns:
        int: The number of non-overlapping occurrences of the specified substring in the string

    Example:
        >>> text = "ababab"
        >>> result = text.count("ab")
        >>> print(result)
        2
    '''
    text = "Mia embarked on a journey of learning Python. With every lesson, her love for Python grew deeper. She solved puzzles and built projects, each one reinforcing her belief that Python held endless potential. Soon, Python became her favorite tool for creativity."
    return text.count("Python")

def string_ljust():
    '''
    Method that is used to left-align a string by padding it with spaces (or a specified character) to a certain width. This can be useful for formatting text output.

    Required parameters:
        width (int): The total width of the resulting string after padding. If the original string is longer than this width, it will return the string as it is.
    
    Optional parameters:
        character (str): The character to use for padding. (Default is a space (' '))

    Returns:
        str: A left-aligned string with the specified width
    
    Example: 
        >>> text = "Hello"
        >>> result = text.ljust(10, '-')
        >>> print(result)
        Hello-----
    '''
    text = "FITA"
    return text.ljust(10, '*')

def string_formatMap():
    '''
    Method to format strings using a mapping (like a dictionary)

    Required parameters:
        dictionary (dict): A mapping object containing the keys and values for the placeholders in the string

    Returns:
        str: A new string with the placeholders replaced by the corresponding values from the mapping.

    Example: 
        >>> text = "Hello, {name}! Your age is {age} years."
        >>> map = {'name': 'Bob', 'age': 18}
        >>> result = text.format_map(map)
        >>> print(result)
        Hello, Bob! Your age is 18 years.
    '''
    text = "We are working with {name} for past {age} years!"
    map = {"name" : "Python", "age" : 26}
    return text.format_map(map)

def string_replace():
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
        >>> print(result)
        Hello, universe! This is universe of Python.
    '''
    text = "We really enjoy learning Python"
    return text.replace("Python", "programming")


if __name__ == "__main__":
    print('** .lower() method')
    print(string_lower())
    print("\n")
    print('** .isspace() method')
    print(string_isspace())
    print("\n")
    print('** capitalize() method')
    print(string_capitalize())
    print("\n")
    print('** textwrap.shorten(args) method')
    print(string_textwrap())
    print("\n")
    print('** .count(args) method')
    print(string_count())
    print("\n")
    print('** .ljust(args) method')
    print(string_ljust())
    print("\n")
    print('** .format_map(dict) method')
    print(string_formatMap())
    print("\n")
    print('** .replace(args) method')
    print(string_replace())
    print("\n")
    
