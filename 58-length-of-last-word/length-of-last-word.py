class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        wordlist = s.split()
        if wordlist!=0:
            return len(wordlist[-1])
        return 0