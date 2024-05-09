class Solution:
    def wordPattern(self, pattern, str):
        words=str.split(" ")
        chartoword={}
        wordtochar={}

        if len(pattern) != len(words):
            return False
        for c,w in zip(pattern, words):
            if c in chartoword and chartoword[c]!=w:
                return False
            if w in wordtochar and wordtochar[w]!=c:
                return False
            chartoword[c]=w
            wordtochar[w]=c
        return True