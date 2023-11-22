def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """

    boolean = False

    if len(parens) % 2 == 1 or parens[0] == ")" or parens[-1] == "(":
        return False
    for char in parens:
        if char == "(":
            boolean += 1
        elif char == ")":
            boolean -= 1

    return boolean == 0
