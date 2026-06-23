class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Create an empty stack to keep track of numbers and intermediate results
        stack = []

        # Loop through each token in the input list
        for c in tokens:

            # If the token is a plus sign, it's an operator
            if c == "+":
                # Pop the top two numbers from the stack and add them
                # Order matters for subtraction and division, but not addition
                stack.append(stack.pop() + stack.pop())

            # If the token is a minus sign
            elif c == "-":
                # Pop the last two numbers, be careful with the order
                a, b = stack.pop(), stack.pop()
                # Since subtraction is not commutative, we do (b - a)
                stack.append(b - a)

            # If the token is a multiplication sign
            elif c == "*":
                # Pop two numbers and multiply them
                stack.append(stack.pop() * stack.pop())

            # If the token is a division sign
            elif c == "/":
                # Pop the last two numbers (careful with order!)
                a, b = stack.pop(), stack.pop()
                # In Python, integer division between negatives can be tricky,
                # so we convert to float and then back to int to truncate toward zero
                stack.append(int(float(b) / a))

            # If the token is a number (operand), convert it from string to int and push it to the stack
            else:
                stack.append(int(c))

        # At the end, the stack will have one item left — the final result
        return stack[0]
