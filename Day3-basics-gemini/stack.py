def is_valid(s: str ) -> bool:
    """
    Checks if a string of parentheses is valid using a stack.
    """
    # Use a list to act as our stack
    stack = []
    
    # A mapping of closing brackets to their matching opening ones
    matching_bracket = {")": "(", "}": "{", "]": "["}

    # Iterate through each character in the string
    for char in s:
        # If the character is a closing bracket
        if char in matching_bracket:
            # Check if the stack is not empty AND if the top of the stack
            # is the matching opening bracket.
            if stack and stack[-1] == matching_bracket[char]:
                stack.pop()
            else:
                # Mismatched bracket or closing bracket with no opener
                return False
        else:
            # It's an opening bracket, so push it onto the stack
            stack.append(char)

    # After the loop, the string is valid only if the stack is empty
    return not stack
# print(is_valid("({[]})"))

















def is_val(s):
    stck = []
    
    matchin_bracket = {")":"(", "}":"{","]":"["}
    
    for i in s:
        if i in matchin_bracket:
            if stck  and stck[-1] == matchin_bracket[i]:
                stck.pop()
            else:
                return False
        else:
            stck.append(i)
    return not stck
print(is_val("({[]})"))