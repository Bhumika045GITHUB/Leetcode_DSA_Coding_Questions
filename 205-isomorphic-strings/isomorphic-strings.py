class Solution(object):
    def isIsomorphic(self, s, t):
        map1 = {}
        map2 = {}
        
        for idx, char in enumerate(s):
            map1[char] = map1.get(char, []) + [idx]

        for idx, char in enumerate(t):
            map2[char] = map2.get(char, []) + [idx]

        return list(map1.values()) == list(map2.values())
