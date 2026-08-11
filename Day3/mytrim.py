def my_trim(s):
    """
    Removes leading and trailing whitespace from the input string s.

    Args:
        s (str): The input string to be trimmed.

    Returns:
        str: The trimmed string.

    I find the first and last non-space positions, and then use slicing to extract the substring between them.
    """
    start = 0
    end = len(s)

    while start < end and s[start] == " ":
        start += 1

    while end > start and s[end - 1] == " ":
        end -= 1

    return s[start:end]


print(my_trim("   Hello, World!   "))  # Output: "Hello, World!"
print(my_trim(""))
print(my_trim("   "))
print(my_trim("Hello, World!   s"))
