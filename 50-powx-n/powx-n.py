class Solution:
    @cache
    def myPow(self, x: float, n: int) -> float:
        #tc - O(n)
     #   return x**n
        #tc - O(logn) - by divide n conquer approach
        if(n==0):
            return 1
        elif(n==1):
            return x
        elif(n<0):
            return self.myPow(1/x,-n)
        elif(n%2==0):
            return self.myPow(x,n/2) * self.myPow(x,n/2)
        else:
            return x*self.myPow(x,n-1)

