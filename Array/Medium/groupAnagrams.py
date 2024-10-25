class Solution(object):
    """
    Using Array to Solve
    """
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        def _check_anagram(s, t):
            s_sort = sorted(s)
            t_sort = sorted(t)
            return s_sort == t_sort

        tmp = []
        res = []
        seen = set()
        for i in range(len(strs)-1):
            if strs[i] not in seen:
                tmp.append(strs[i])
                for j in range(i+1, len(strs)):
                    if strs[j] not in seen:
                        if _check_anagram(strs[i], strs[j]):
                            tmp.append(strs[j])
                for word in tmp:
                    seen.add(word)
                res.append(tmp)
                tmp = []
        if strs[-1] not in seen:
            res.append([strs[-1]])
        return res
