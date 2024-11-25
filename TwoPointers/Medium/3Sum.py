class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            l_pos = i+1
            r_pos = len(nums) - 1
            while l_pos < r_pos:
                if nums[l_pos] + nums[r_pos] < target:
                    l_pos += 1
                elif nums[l_pos] + nums[r_pos] > target:
                    r_pos -= 1
                else:
                    res.append([nums[i],nums[l_pos],nums[r_pos]])
                    # Find next triplets by decrease r_pos (can use increase l_pos)
                    r_pos -= 1
                    while nums[r_pos] == nums[r_pos+1] and r_pos > l_pos:
                        r_pos -= 1
        return res
