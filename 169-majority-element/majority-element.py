class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #hashmap
        count={}
        res,maxcount=0,0

        for i in nums:
            count[i]=1+count.get(i,0)
            res=i if count[i]>maxcount else res
            maxcount =max(maxcount,count[i])
        return res