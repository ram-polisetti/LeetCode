class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n= len(nums)
        sum_numbers = n*(n+1)/2
        sum = 0

        for ele in nums:
            sum += ele

        return sum_numbers - sum

