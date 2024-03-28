class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        max_length = 0
        frequency_count = collections.Counter()
        left_pointer = 0

        for right_pointer, num in enumerate(nums):
            frequency_count[num] += 1

            while frequency_count[num] == k + 1:
                frequency_count[nums[left_pointer]] -= 1
                left_pointer += 1

            max_length = max(max_length, right_pointer - left_pointer + 1)

        return max_length

        