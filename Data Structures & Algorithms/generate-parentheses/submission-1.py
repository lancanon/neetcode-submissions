class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []  # Temporary list to build current combination of parentheses
        res = []    # Final list of valid parentheses combinations

        # Recursive backtracking function
        def backtrack(openN, closedN):
            # Base case: if we've used all open and close brackets, save the result
            if openN == closedN == n:
                res.append("".join(stack))  # Join stack into string and add to result
                return

            # If we can still add an open bracket, do it
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)  # Explore further with one more open
                stack.pop()  # Backtrack: remove the last added "("

            # If we can close a previously opened bracket, do it
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)  # Explore further with one more closed
                stack.pop()  # Backtrack: remove the last added ")"

        # Start with 0 open and 0 closed brackets
        backtrack(0, 0)
        return res
