class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        longer_string = s if len(s) > len(t) else t
        smaller_string = t if len(t) < len(s) else s
        for char in longer_string:
            if char in smaller_string:
                smaller_string = smaller_string.replace(char, '', 1)
            else:
                return False
        
        return True