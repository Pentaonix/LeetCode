class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        def dfs(m, d, s):
            if m == n and d == n:
                res.append(s)
                return
            if m < n:
                dfs(m+1, d, s+'(')
            if d < m:
                dfs(m, d+1, s+')')

        dfs(0, 0, '')
        return res
