class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
    
        non_zero_indexes = [i for i,val in enumerate(nums) if val!=0]
        
        ctr = 0
        if len(nums) !=0 and len(nums) !=1:
            for i in range(0, len(non_zero_indexes)):
                nums[i] = nums[non_zero_indexes[ctr]]
                ctr = ctr + 1

            for i in range(len(non_zero_indexes), len(nums)):
                nums[i] = 0
        
                