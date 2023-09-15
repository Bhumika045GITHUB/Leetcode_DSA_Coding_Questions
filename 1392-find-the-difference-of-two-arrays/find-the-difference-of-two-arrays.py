class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        x=[]
        a=[]
        a=set(nums1) - set(nums2)
        b=[]
        b=set(nums2) - set(nums1)
        x.append(a)
        x.append(b)
        return x
        