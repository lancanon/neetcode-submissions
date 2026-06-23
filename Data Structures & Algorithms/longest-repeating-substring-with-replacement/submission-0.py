class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}       # Tracks frequency of characters in current window
        res = 0          # Tracks the length of longest valid substring
        l = 0            # Left pointer of sliding window
        maxf = 0         # Max frequency of a single character in the window

        for r in range(len(s)):  # r = right pointer
            # Update the count of current character
            count[s[r]] = 1 + count.get(s[r], 0)
            # Update the max frequency character seen so far
            maxf = max(maxf, count[s[r]])

            # If the window is invalid (too many characters to replace)
            if (r - l + 1) - maxf > k:
                count[s[l]] -= 1   # Shrink the window from the left
                l += 1

            # Update the result (max window size so far)
            res = max(res, r - l + 1)

        return res
