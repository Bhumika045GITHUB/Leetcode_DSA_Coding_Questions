class Solution:
    def reverseWords(self, s: str) -> str:
        #inplace - splitted s.split() string to list ------> then ----> reversed list then joind iwth spave in string
        
        return (" ".join(s.split()[::-1]))
     

        
        