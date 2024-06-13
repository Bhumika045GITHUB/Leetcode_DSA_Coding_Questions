class Solution:
    def reverseVowels(self, s: str) -> str:
        import re
#re.findall make string to list
        vowels = re.findall('[aeiouAEIOU]', s) 

#re.findall make string to list
        return re.sub('[aeiouAEIOU]', lambda m: vowels.pop(), s)
        