class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False  # Impossible for s2 to contain permutation

        # Frequency counters for s1 and for current window in s2
        s1Count, s2Count = [0] * 26, [0] * 26

        # Count characters in s1 and the first window of s2
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        # Count how many characters match in both frequency arrays
        matches = 0
        for i in range(26):
            matches += 1 if s1Count[i] == s2Count[i] else 0

        # Start sliding the window across s2
        l = 0  # left pointer
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True  # All 26 character frequencies match

            # Add s2[r] to the window
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1  # It just went over, so no longer equal

            # Remove s2[l] from the window
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1  # It just dropped below, so no longer equal
            l += 1  # Move the window forward

        return matches == 26  # Final check after loop
