class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magazine_list = list(magazine)

        avail_dict = {}

        for char_avail in magazine:
            avail_dict[char_avail] = avail_dict.get(char_avail, 0) + 1

        for char_find in ransomNote:
            if avail_dict.get(char_find, 0) == 0:
                return False
            else:
                avail_dict[char_find] -= 1
        return True 