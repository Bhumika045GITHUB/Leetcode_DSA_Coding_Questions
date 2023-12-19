class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

    #this time compldepends on whoch sort algo we r using
     #   return sorted(t)== sorted(s)
        
        return Counter(t)== Counter(s)