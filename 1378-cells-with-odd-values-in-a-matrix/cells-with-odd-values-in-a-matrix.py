class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        count=0
        row=[0]*n
        col=[0]*m
        for x,y in indices:
            row[x]+=1
            col[y]+=1
        for i in range(n):
            for j in range(m):
                if (row[i]+col[j])%2==1:
                    count+=1
        return count
            