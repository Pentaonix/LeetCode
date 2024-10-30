class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        max_len = 1
        max_len_tmp = 1
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                max_len_tmp += 1
            elif nums[i] - nums[i - 1] == 0:
                continue
            else:
                max_len_tmp = 1
            if max_len_tmp > max_len:
                max_len = max_len_tmp
        return max_len
