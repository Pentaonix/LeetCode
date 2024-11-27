class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l_pos = 0
        r_pos = len(height) - 1
        res = 0
        while l_pos < r_pos:
            area = min(height[l_pos], height[r_pos])*(r_pos-l_pos)
            if res < area:
                res = area
            if height[l_pos] < height[r_pos]:
                l_pos += 1
            else:
                r_pos -= 1
        return res
