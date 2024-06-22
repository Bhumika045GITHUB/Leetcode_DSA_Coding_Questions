class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if(len(nums) ==1): return 0
        left_sum,tot_sum=0,sum(nums)
        
        for i in range(len(nums)):
            tot_sum = tot_sum-nums[i]
            if (tot_sum==left_sum):
                return i

            left_sum=left_sum+nums[i]

        return -1
        