class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0,len(nums)):
            if target - nums[i] in nums:
                n = nums.index(target - nums[i])
                if n != i:
                    return [i,n]
        return []
