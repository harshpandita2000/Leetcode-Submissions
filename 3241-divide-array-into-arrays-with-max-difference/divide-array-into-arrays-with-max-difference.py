class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        listt =[]
        nums.sort()
        for i in range(0,len(nums),3):
            a = nums[i]
            b = nums[i+1]
            c = nums[i+2]
            if c-a > k:
                return []
            else:
                listt.append((a,b,c))
        return listt