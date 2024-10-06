class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if self._check_number(s) and self._check_order(s):
            return True
        return False

    def _check_number(self, s):
        if (s.count("(") != s.count(")") or
            s.count("[") != s.count("]") or
            s.count("{") != s.count("}")):
                return False
        return True
    
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
                if not stack or stack.pop() != "(":
                    return False
            elif bracket == "]":
                if not stack or stack.pop() != "[":
                    return False
            else:
                if not stack or stack.pop() != "{":
                    return False
        if len(stack) != 0:
            return False
        return True
