class Solution:
    def reverseWords(self, s: str) -> str:
        #inplace
        return (" ".join(s.split()[::-1]))
     

        
        