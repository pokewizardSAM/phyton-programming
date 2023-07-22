class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        length = len(nums)
        counters= 0
        result = False
        for i in range(counters,length):
            for j in range(counters+1,length):
                if i <= j and nums[i] <= nums[j]:
                    result = True
                else:
                    result = False
        return result

