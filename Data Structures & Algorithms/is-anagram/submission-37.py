class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #if length of s and t aren't equal then they aren't anagrams
        if len(s) != len(t):
            return False

        dictS = {}
        dictT = {}

        for c in s:
            dictS[c] = dictS.get(c,0) + 1
        for c in t:
            dictT[c] = dictT.get(c,0) + 1
        
        return dictS == dictT
