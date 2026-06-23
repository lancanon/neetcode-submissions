from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)  # Create a hash map to group anagrams
        
        for word in strs:  
            # Step 1: Create a frequency array to count characters
            freq = [0] * 26  # Array of 26 zeros for 'a' to 'z'
            for char in word:
                freq[ord(char) - ord('a')] += 1  # Count each character
            
            # Step 2: Use the frequency array (converted to a tuple) as the key
            key = tuple(freq)
            
            # Step 3: Append the word to the corresponding group in the hash map
            anagrams[key].append(word)
        
        # Step 4: Return all grouped anagrams as a list of lists
        return list(anagrams.values())
