class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():

                left += 1
            while left < right and not s[right].isalnum():

                right -= 1

            print(f"Comparing {s[left]} (left index {left}) and {s[right]} (right index {right})")
            print(f"Equal? {s[left].lower() == s[right].lower()}")
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True

        