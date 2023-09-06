class Solution:
    def averageValue(self, nums: List[int]) -> int:
        c=0
        x=[]
        for i in nums:
            if(i%3==0 and i%2==0):
                c+=1
                x.append(i)
            

        return round(sum(x)//c) if c>0 else 0