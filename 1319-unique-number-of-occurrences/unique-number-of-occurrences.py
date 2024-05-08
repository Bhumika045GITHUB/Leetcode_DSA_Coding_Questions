class Solution(object):
    def uniqueOccurrences(self, arr):
        
        #print(Counter(arr).values())
        return len(set(Counter(arr).values())) == len(Counter(arr).values())


        