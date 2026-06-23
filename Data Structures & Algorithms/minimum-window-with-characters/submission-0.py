class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        # Step 1: Build frequency map for string t
        countT = {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        window = {}            # Frequency map for current window
        have, need = 0, len(countT)  # Number of chars matched vs. needed
        res, resLen = [-1, -1], float("infinity")  # Store result window
        l = 0                  # Left pointer of sliding window

        # Step 2: Expand window with right pointer r
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            # If current char matches required frequency in t
            if c in countT and window[c] == countT[c]:
                have += 1

            # Step 3: Shrink the window when all required chars are matched
            while have == need:
                # Update result if it's the smallest valid window so far
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                # Shrink from the left
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:r + 1] if resLen != float("infinity") else ""
