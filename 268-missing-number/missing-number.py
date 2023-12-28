class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        max_ele = max(nums)
        min_ele = min(nums)
        if min_ele !=0:
            return 0
        # print(max_ele, min_ele)
        for i in range(min_ele, max_ele+1):
            # print(i)
            if i not in nums:
                # print(i)
                return i
        return max_ele+1
                
