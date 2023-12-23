class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        #using 1 variable only tc=o(n), sc=
        for i in range(len(nums)-2,0,-1):
            if(nums[i]==nums[i-1] and nums[i]==nums[i+1]):
                nums.pop(i+1)
        return len(nums)


      