class Solution:
    def majorityElement(self, nums: List[int]) -> int:
            n = len(nums)
            counts = {}

            for element in nums:
                if element in counts:
                    counts[element] += 1
                else:
                    counts[element] = 1

            for element, count in counts.items():
                if count > n // 2:
                    return element

            return -1
