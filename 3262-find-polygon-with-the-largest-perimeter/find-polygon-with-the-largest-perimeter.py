class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        total = sum(nums)
        current_sum = 0
        
        for i in reversed(range(len(nums))):
            current_sum += nums[i]
            rem = total-current_sum
            
            if rem > nums[i]:
                return rem + nums[i]
        return -1