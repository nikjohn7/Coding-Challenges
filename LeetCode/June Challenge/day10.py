class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        mid=(l+r)//2
        if target in nums:
            while(True):
                
                if nums[mid]==target:
                    return mid
                elif nums[mid]>target:
                    r=mid-1
                elif nums[mid]<target:
                    l=mid+1
                mid=(l+r)//2
        else:
            if target<nums[0]:
                return 0
            elif target>nums[r]:
                return r+1
            while(l<=r):
                mid=(l+r)//2
                if nums[mid]<=target:
                    l=mid+1
                else:
                    t=mid
                    r=mid-1
            
            return t