class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        elif nums[-1]!=nums[-2]:
            return nums[-1]
        else:
            i=0
            while i<len(nums)-1:
                if nums[i]!=nums[i+1]:
                    return nums[i]
                i+=2