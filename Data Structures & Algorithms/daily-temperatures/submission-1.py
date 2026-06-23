class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)  # Initialize result array with 0s
        stack = []  # Will store pairs: [temperature, index]

        # Loop through each temperature and its index
        for i, t in enumerate(temperatures):
            # While stack is NOT empty and current temp is GREATER than stack top
            while stack and t > stack[-1][0]:
                # Found a warmer day for the top of stack
                stackT, stackInd = stack.pop()  # Pop off colder temperature
                res[stackInd] = i - stackInd    # Calculate how many days it took
            # Push current day onto the stack to wait for a warmer day
            stack.append((t, i))

        return res
