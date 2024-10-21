class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        tmp = []
        for i in range(0, m):
            tmp.append(nums1[i])
        for j in range(len(nums2)):
            tmp.append(nums2[j])
        tmp.sort()
        for i in range(0, m+n):
            nums1[i] = tmp[i]
