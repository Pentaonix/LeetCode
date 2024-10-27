from collections import defaultdict

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        mp = defaultdict(int)
        for num in nums:
            mp[num] += 1
        key_list = list(mp.keys())
        value_list = list(mp.values())
        for i in range(len(value_list)-1):
            for j in range(i+1, len(value_list)):
                if value_list[i] < value_list[j]:
                    key_list[i], key_list[j] = key_list[j], key_list[i]
                    value_list[i], value_list[j] = value_list[j], value_list[i]
        return key_list[:k]
