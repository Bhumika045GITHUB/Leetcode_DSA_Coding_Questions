class Solution:

     def sortSentence(self, s: str) -> str:
  
        a=s[::-1].split();a.sort();r=[]  
        for word in a:
            r.append(word[1:][::-1])
        return " ".join(r)

