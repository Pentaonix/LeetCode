class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        number = 0
        new_digits = []
        for i in range(len(digits)):
            number += digits[-i-1]*pow(10, i)
        number_str = str(number+1)
        for i in number_str:
            new_digits.append(int(i))
        return new_digits
