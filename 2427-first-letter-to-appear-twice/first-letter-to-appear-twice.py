class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        set1=set()
        for i in s:
            if i not in set1:
                set1.add(i)
            else:
                return i