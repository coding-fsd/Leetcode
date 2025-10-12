class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        x = nums1[0:m]
        nums1[:] = x+nums2
        nums1.sort()