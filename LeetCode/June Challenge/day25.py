class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        a=set(nums)
        for i in nums:
            if i in a:
                a.remove(i)
            else:
                return i