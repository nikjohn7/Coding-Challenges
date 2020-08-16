class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        next_pos_0 = 0
        next_pos_2 = len(nums) - 1

        front_index = 0

        while front_index <= next_pos_2:
            if nums[front_index] == 0:
                nums[front_index] = nums[next_pos_0]
                nums[next_pos_0] = 0
                next_pos_0 += 1
                front_index += 1
            elif nums[front_index] == 2:           
                nums[front_index] = nums[next_pos_2] 
                nums[next_pos_2] = 2
                next_pos_2 -= 1
            else:
                front_index += 1