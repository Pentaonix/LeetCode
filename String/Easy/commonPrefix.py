class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 1:
            return strs[0]
        short = strs[0]
        res = ''
        for i in strs:
            if len(i) < len(short):
                short = i
        for j in range(0, len(short)):
            for i in range(0, len(strs)-1):
                if strs[i][j] != strs[i+1][j]:
                    return res
            res += strs[i][j]
        return res
