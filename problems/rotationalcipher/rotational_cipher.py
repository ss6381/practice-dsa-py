def rotational_cipher(input_str, rotation_factor):
    result = []
    for char in input_str:
        curr_char = char
        if char.isalpha():
            # Handle letters - rotate within their case
            if char.isupper():
                # Uppercase letters: A-Z (65-90)
                curr_char = chr(
                    (ord(char) - ord("A") + rotation_factor) % 26 + ord("A")
                )
            else:
                # Lowercase letters: a-z (97-122)
                curr_char = chr(
                    (ord(char) - ord("a") + rotation_factor) % 26 + ord("a")
                )
        elif char.isnumeric():
            # Handle numbers - rotate within 0-9
            curr_char = chr((ord(char) - ord("0") + rotation_factor) % 10 + ord("0"))
        # Non-alphanumeric characters remain unchanged
        result.append(curr_char)
    return "".join(result)
