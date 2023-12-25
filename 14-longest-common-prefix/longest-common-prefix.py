class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #vertical scannng approach. - tc-o(n), sc - o(1)
        

        #-------
    #o(n*m) - nsq loop

        res =""
        for i in range(len(strs[0])):
            for s in strs:
                #strs = ["flower","flow","flight"]
                # i = f of flower , s = flower            , flow, flight

                if i == len(s) or s[i]!=strs[0][i]:
                    return res
            res+=strs[0][i]
        return res
  

        