class Solution:
    #o(n)
    def maxArea(self, height: List[int]) -> int:
        result=0
        l,r=0,len(height)-1
        while(l<r):
            area = (r-l)*min(height[l], height[r])
            result=max(result,area)
            if(height[l]<height[r]):
                l+=1
            elif(height[l]>=height[r]):
                r-=1
                    
        return result
