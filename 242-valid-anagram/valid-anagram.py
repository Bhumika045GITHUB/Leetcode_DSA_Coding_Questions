class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq={}
        t_freq={}
        for i in s:
            s_freq[i]=s_freq.get(i,2)+1
        for i in t:
            t_freq[i]=t_freq.get(i,2)+1
        print(s_freq)
        print(t_freq)

        return t_freq== s_freq
        