class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
          return False

        count = {}

        for char in s:
            count[char] = count.get(char, 0) + 1
        
        for char in t:
            if char not in count:
                return False
            count[char] -= 1
            if count[char] < 0:
                return False

        return True


# --- Testing ---
sol = Solution()
test_cases = [
    ("anagram", "nagaram", True),
    ("rat", "car", False),
    ("a", "ab", False),
    ("ab", "ba", True),
    ("", "", True),
]

for s, t, expected in test_cases:
    result = sol.isAnagram(s, t)
    print(f"isAnagram({s}, {t}) ➝ {result}  {'✅' if result == expected else '❌'}")
