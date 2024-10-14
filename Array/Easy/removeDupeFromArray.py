class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new = list(set(nums))
        new.sort()
        for i in range(0, len(new)):
            nums[i] = new[i]
        return len(new)
