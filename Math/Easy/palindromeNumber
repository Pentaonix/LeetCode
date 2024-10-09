class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_string = str(x)
        for i in range(0, int(len(x_string)/2)):
            if x_string[i] != x_string[0-i-1]:
                return False
        return True
