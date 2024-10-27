from collections import defaultdict

class Solution(object):
    """
    Using Hash to Solve
    """
    def groupAnagrams(self, strs):
        anagram_map = defaultdict(list)
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)
        
        res = []
        for r in anagram_map.values():
            res.append(r)
        return res
