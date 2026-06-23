class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}      # Dictionary to store last seen index of each character
        l = 0        # Left side of the sliding window
        res = 0      # Result: length of longest valid substring

        for r in range(len(s)):  # r is the right side of the sliding window
            if s[r] in mp:
                # If character was seen before, move left pointer past its last index
                l = max(mp[s[r]] + 1, l)

            # Update the last seen index of the current character
            mp[s[r]] = r

            # Update the result with the current window size
            res = max(res, r - l + 1)

        return res
