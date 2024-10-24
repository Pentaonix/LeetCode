from collections import defaultdict

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Using list/array
        # sorted_s = sorted(s)
        # sorted_t = sorted(t)
        # return sorted_s == sorted_t

        # Using Hash
        # Create a default dict with values = 0
        my_dict = defaultdict(int)
        for letter in s:
            my_dict[letter] += 1
        
        for letter in t:
            my_dict[letter] -= 1

        for count in my_dict.values():
            if count != 0:
                return False
        return True
