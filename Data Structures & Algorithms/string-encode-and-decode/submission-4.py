class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):  
            j = i      
            while s[j] != "#":
                j += 1
            length = int(s[i:j])  # length of the word
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length    # move i to the start of the next encoded word
        return res
