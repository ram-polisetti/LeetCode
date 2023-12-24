class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # nums_len = len(set(nums))
        # if len(nums) != nums_len:
        #     return True
        # else:
        #     return False
        
        hashset = set()
        for ele in nums:
            if ele in hashset:
                return True
            hashset.add(ele)
        return False
            