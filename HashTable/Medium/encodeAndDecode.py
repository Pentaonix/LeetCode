class Solution:

    def encode(self, strs):
        if not strs:
            return chr(258)
        # Use a unique delimiter
        delimiter = chr(257)
        s = delimiter.join(strs)
        new_s = ''
        for letter in s:
            new_s += chr(ord(letter) + 1)
        return new_s

    def decode(self, s):
        if s == chr(258):
            return []
        delimiter = chr(257)
        res = ''
        for letter in s:
            res += chr(ord(letter) - 1)
        return res.split(delimiter)
