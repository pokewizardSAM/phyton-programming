class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        list2= set(nums2)-set(nums1)
        list1= set(nums1)-set(nums2)
        return [list1,list2]

sol = Solution()
print(sol.findDifference( [1,2,3],[2,4,6]))