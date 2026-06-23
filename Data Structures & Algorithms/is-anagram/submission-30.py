class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #check if strings are same length if not return False
        if len(s) != len(t):
            return False
        
        #create empty dictionary for s and t to store char
        countS, countT = {},{}

        for char in s:
            countS[char] = countS.get(char, 0) + 1
        
        for char in t:
            countT[char] = countT.get(char, 0) + 1
        
        return countS ==  countT
        