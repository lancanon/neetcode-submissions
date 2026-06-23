class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #if the length of s != length of t
        #return False because not anagram
        if len(s) != len(t):
            return False
        
        #create hashmap to store str
        countS, countT = {},{}

        for char in s:
            countS[char] = countS.get(char,0) + 1
        for char in t:
            countT[char] = countT.get(char,0) + 1
        
        return countS == countT
        