def paperwork(n, m):
    """
    Calculate the total number of blank pages needed to copy paperwork for a given number of classmates and pages.

    Args:
        n (int): The number of classmates to copy paperwork for.
        m (int): The number of pages to copy.

    Returns:
        int: The total number of blank pages needed to copy the paperwork, or 0 if n or m is negative.
    """
    if n < 0 or m < 0:
        return 0

    return n * m