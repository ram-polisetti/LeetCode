class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # freq = Counter(nums)
        # print(freq)
        # max = 0
        # maj_ele = 0
        # for num in freq:
        #     if freq[num] > max and freq[num] > len(nums)//2:
        #         max = freq[num]
        #         maj_ele = num 
        
        # return maj_ele


        nums.sort()
        n = len(nums)//2
        return nums[n]