class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a defaultdict of lists to hold the groups of anagrams.
        # Each key will be a tuple representing the count of each letter,
        # and the value will be a list of strings that are anagrams of each other.
        hashmap = defaultdict(list)
        
        # Iterate over each string in the input list.
        for s in strs:
            # Initialize a list of 26 zeros, one for each letter of the alphabet.
            count = [0] * 26
            
            # Count the frequency of each letter in the string.
            # 'ord(c) - ord('a')' calculates the index of the letter 'c' in the alphabet.
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            # Use the letter count list as a key in the hashmap.
            # Since lists can't be used as dictionary keys (they're mutable),
            # we convert it to a tuple (which is immutable) to use as a key.
            hashmap[tuple(count)].append(s)
        
        # Return the values of the hashmap, which are lists of anagram groups.
        return list(hashmap.values())

        # Time Complexity: O(N * L) where N is the number of strings and L is the average length of the strings.

        