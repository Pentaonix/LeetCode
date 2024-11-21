class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l_pos = 0
        r_pos = -1
        for i in range(len(numbers)):
            if numbers[l_pos] + numbers[r_pos] < target:
                l_pos += 1
            elif numbers[l_pos] + numbers[r_pos] > target:
                r_pos -= 1
            else:
                return [l_pos+1, r_pos+len(numbers)+1]
        return []
