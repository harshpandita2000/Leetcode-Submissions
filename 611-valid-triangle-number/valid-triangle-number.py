class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        count = 0
        nums.sort() 
        n = len(nums)
        for i in range(n - 2):
            k = i + 2
            for j in range(i + 1, n - 1):
                while k < n and nums[i] + nums[j] > nums[k]:
                    k += 1
                count += max(k - j - 1, 0) 
        return count