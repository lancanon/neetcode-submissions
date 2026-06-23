class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dict = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for char in s:
                count[ord(char) - ord('a')]+= 1

            key = tuple(count)
            dict[key].append(s)
            
        return list(dict.values())
        