class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, e = 0,len(s)-1
        while(l<e):
            while(l<e and not s[l].isalnum()):
                l+=1
            while(l<e and not s[e].isalnum()):
                e-=1 
            if(s[l].lower() != s[e].lower()):
                return False
            l+=1
            e-=1
        return True  