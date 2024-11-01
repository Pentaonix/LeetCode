class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if self._check_order(s):
            return True
        return False
    
    def _check_order(self, s):
        stack = []
        open_bracket = ["(", "[", "{"]
        close_bracket = [")", "]", "}"]

        if len(s) == 0 or s in close_bracket:
            return False

        for bracket in s:
            if bracket in open_bracket:
                stack.append(bracket)
            elif bracket == ")":
                if not stack or stack[-1] != "(":
                    return False
                else:
                    stack.pop()
            elif bracket == "]":
                if not stack or stack[-1] != "[":
                    return False
                else:
                    stack.pop()
            elif bracket == "}":
                if not stack or stack[-1] != "{":
                    return False
                else:
                    stack.pop()
        if len(stack) != 0:
            return False
        return True
