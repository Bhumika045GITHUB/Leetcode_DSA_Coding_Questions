class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        c= s.count(s[0])
        for i in s:
            if s.count(i)!=c:
                return False
        return True
        