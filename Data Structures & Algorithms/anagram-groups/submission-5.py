class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Create a defaultdict where each key's value is an empty list by default
        # This dictionary will map each "letter count signature" (a tuple) to a list of words (anagrams)
        res = defaultdict(list)

        # Loop through every word in the input list
        for s in strs:
            # Create a list of 26 zeros to count the frequency of each letter (a to z)
            count = [0] * 26

            # For each character in the current word, increase its count
            # ord(c) - ord('a') converts the letter to an index between 0 and 25
            for c in s:
                count[ord(c) - ord('a')] += 1

            # Convert the list of counts to a tuple because tuples can be used as dictionary keys
            # This tuple acts as a unique "signature" for the group of anagrams
            key = tuple(count)

            # Append the original word to the list corresponding to this signature in the dictionary
            res[key].append(s)

        # Return all the grouped anagram lists (the dictionary values) as a list of lists
        return list(res.values())
