class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        letter_freq = Counter(s)
        letter_count = list(letter_freq.values())

        palindrome_len = 0
        for count in range(len(letter_count)):
            if letter_count[count]%2==0:
                palindrome_len += letter_count[count]
            else:
                palindrome_len += letter_count[count] -1

        return palindrome_len if len(s)==palindrome_len else palindrome_len+1