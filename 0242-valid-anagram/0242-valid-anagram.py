class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
#         if len(s) != len(t):
#             return False
#         for char in s:
#             if char in t:
#                 t = t.replace(char, '', 1)
#             else:
#                 return False
        
#         return True
        
        countS = {}
        countT = {}
        
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
            
        for char in countS:
            if countS[char] != countT.get(char, 0):
                return False
        
        return True
            