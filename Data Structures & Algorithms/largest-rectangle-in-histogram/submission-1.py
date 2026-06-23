class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []  # This will store pairs of (index, height)

        for i, h in enumerate(heights):
            start = i  # Start index of the current bar

            # Pop bars from the stack if the current bar is LOWER
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                # Calculate area: width = i - index
                maxArea = max(maxArea, height * (i - index))
                # Update start to the popped index for later use
                start = index

            # Push the current bar (with updated start index) onto the stack
            stack.append((start, h))

        # Handle any bars left in the stack (which reached the end)
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea
