class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # The binary start with 0b
        return bin(int(a, 2) + int(b, 2))[2:]
