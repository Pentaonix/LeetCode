class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        # 2 or more 0 in array
        if nums.count(0) >= 2:
            return [0] * len(nums)
        total_product = 1
        for i in range(len(nums)):
            if nums[i] != 0:
                total_product *= nums[i]
        # No 0 in array
        if 0 not in nums:
            return [int(total_product/num) for num in nums]
        # Only one 0 in array
        else:
            return [0 if num != 0 else total_product for num in nums]
