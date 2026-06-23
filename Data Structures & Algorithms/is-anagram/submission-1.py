class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       
       #Rule: check length of strings
        if len(s) != len(t):
            return False
        
        countS = {}
        countT = {}

        for char in s:
            countS[char] = countS.get(char, 0) + 1
        
        for char in t:
            countT[char] = countT.get(char, 0) + 1
        
        # Step 3: Compare character counts
        return countS == countT
