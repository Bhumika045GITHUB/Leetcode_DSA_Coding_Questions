class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        a=[area,1]
        mn = float(inf)
        for width in range(1, int(area**0.5)+1):
            len=area/width
            if(len==int(len) and len>=width and (len-width)<mn):
                a[0]=int(len)
                a[1] = width
                mn=len-width
        return a