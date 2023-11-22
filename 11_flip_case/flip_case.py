def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    respons = ""
    
    for char in phrase:
        if to_swap.isupper():
            if char == to_swap:
                respons += char.lower()
            elif char.upper() == to_swap:
                respons += char.upper()
            else:
                respons += char

        elif to_swap.islower():
            if char == to_swap:
                respons += char.upper()
            elif char.lower() == to_swap:
                respons += char.lower()
            else:
                respons += char
                
    print(phrase)
    return respons

print(flip_case('Aaaahhh', 'h'))