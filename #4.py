# Copy
def  get_count(sentence):
    """
    Count the number of vowels (a, e, i, o, u) in a given string.

    Args:
        string (str): The input string to count vowels in.

    Returns:
        int: The number of vowels in the input string.
    """
    vowels = "aeiou"
    count = 0

    for char in string:
        if char in vowels:
            count += 1

    return count