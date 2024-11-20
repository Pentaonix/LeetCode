class Solution:
    def isPalindrome(self, s):
        string = self._standalize(s)
        for i in range(len(string)//2):
            if string[i] != string[-i-1]:
                return False
        return True

    def _standalize(self, string):
        standard = "".join(char for char in string if char.isalnum())
        return standard.lower()
