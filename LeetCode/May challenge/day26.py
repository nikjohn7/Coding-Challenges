class Solution:
     def findMaxLength(self, nums: List[int]) -> int:
         count = 0
         result = 0
         d = {0: -1}
         for i in range(len(nums)):
             n = nums[i]
             if n == 0:
                 count -= 1
             if n == 1:
                 count += 1
                 
             if count in d:  
                 result = max(result, i-d[count]) 
             else:                    
                 d[count] = i  
                 
         return result