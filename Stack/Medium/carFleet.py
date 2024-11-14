class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        res = cur = 0
        time = [float((target-pos)/speed) for pos, speed in sorted(zip(position, speed))]
        for t in time[::-1]:
            if t > cur:
                cur = t
                res += 1
        return res
