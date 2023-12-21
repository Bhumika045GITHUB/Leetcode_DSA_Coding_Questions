class Solution:
   def rotate(self, nums: List[int], k: int) -> None:
       k %= len(nums)

       nums.reverse()

       def inPlaceReverse(start, end):
           nonlocal nums
           while start < end:
               nums[start], nums[end] = nums[end], nums[start]
               start += 1
               end -= 1
       
       inPlaceReverse(0, k-1)
       inPlaceReverse(k, len(nums)-1)