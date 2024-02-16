class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = -1 
        
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                index = i
                break
        
        if index == -1:
            nums[:] = nums[::-1]
            return nums
        else:
            for i in range(len(nums)-1, index-1, -1):
                if nums[i] > nums[index]:
                    nums[i], nums[index] = nums[index], nums[i]
                    nums[index+1:]  = nums[:index:-1]
                    break