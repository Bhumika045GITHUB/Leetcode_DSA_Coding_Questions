class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        count=0
        count1=0
        c=0
        l=[]
        map1={}
        map2={}
        for i in words1:
            if i in map1:
                map1[i]+=1
            else:
                map1[i]=1
         
        
        for i in words2:
            if i in map2:
                map2[i]+=1
            else:
                map2[i]=1

        for i in map2:
            if i in map1 and map1[i]==1 and map2[i]==1:
                c+=1
        return c

        