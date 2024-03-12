class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        listt = sorted(nums1 + nums2)
        n = len(listt)
        if n % 2:
            return float(listt[n // 2])
        else:
            return float((listt[n // 2 - 1] + listt[n // 2]) / 2)