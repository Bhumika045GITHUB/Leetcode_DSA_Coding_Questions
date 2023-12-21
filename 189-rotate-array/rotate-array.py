
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # Calculate the number of steps we actually need to take
        k = k % len(nums)
    
        # Reverse the entire array
        nums.reverse()
    
        # Reverse the first k elements
        nums[:k] = reversed(nums[:k])
    
        # Reverse the remaining elements
        nums[k:] = reversed(nums[k:])

  