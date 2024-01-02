class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        if len(ransomNote)>len(magazine):
            return False
        
        mag_chars = {}
        for char in magazine:
            if char in mag_chars:
                mag_chars[char] += 1
            else:
                mag_chars[char] = 1

        for char in ransomNote:
            if char in mag_chars and mag_chars[char] >0:
                mag_chars[char] -= 1
            else:
                return False
        return True