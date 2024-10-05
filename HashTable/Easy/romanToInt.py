class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        maps1 = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        maps2 = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }
        sum = 0
        i = 0
        while i < len(s):
            if i+1 <= len(s) and s[i:i+2] in maps2:
                sum += maps2[s[i:i+2]]
                i += 2
            else:
                sum += maps1[s[i]]
                i += 1
        return sum
