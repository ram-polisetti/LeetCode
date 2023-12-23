class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        string = ("".join([char for char in s if char.isalnum()])).lower()
        # print(string)
        left = 0
        right = len(string)-1
        while left<right:
            if string[left] != string[right]:
                print('entered')
                return False
                break
            left += 1
            right -= 1
        return True