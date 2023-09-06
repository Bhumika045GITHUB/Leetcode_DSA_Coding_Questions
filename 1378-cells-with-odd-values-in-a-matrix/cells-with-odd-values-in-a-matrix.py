class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        count=0
        row=[0]*m
        col=[0]*n
        for x,y in indices:
            row[x]+=1
            col[y]+=1
        for i in range(m):
            for j in range(n):
                if (row[i]+col[j])%2==1:
                    count+=1
        return count
            