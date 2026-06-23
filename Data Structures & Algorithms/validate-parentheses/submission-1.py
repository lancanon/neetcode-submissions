class Solution:
    def isValid(self, s: str) -> bool:
        # Stack to keep track of open brackets
        stack = []

        # Dictionary to match closing brackets to their corresponding opening brackets
        closeToOpen = {")": "(", "]": "[", "}": "{"}

        # Iterate over each character in the string
        for c in s:
            # If it's a closing bracket (like ')', ']', '}')
            if c in closeToOpen:
                # Check if the stack is not empty and top of stack matches the opening bracket
                if stack and stack[-1] == closeToOpen[c]:
                    # If it matches, pop it from the stack (they cancel each other)
                    stack.pop()
                else:
                    # Mismatch or stack is empty → invalid
                    return False
            else:
                # If it's an opening bracket (like '(', '[', '{') → push onto stack
                stack.append(c)

        # After the loop, the stack should be empty if all brackets matched
        return not stack
