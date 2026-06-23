class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []             # Final result
        q = deque()             # Stores indices in decreasing value order
        l = r = 0               # Left and right pointers for window

        while r < len(nums):
            # Remove smaller numbers from the back of deque
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # Remove the leftmost index if it's outside the window
            if l > q[0]:
                q.popleft()

            # If window size == k, add max (at front of deque) to output
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1          # Move window forward
            r += 1              # Always move right pointer

        return output
