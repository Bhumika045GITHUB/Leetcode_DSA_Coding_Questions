class Solution(object):
    def groupAnagrams(self, strs):
        dict={}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in dict:
                dict[sorted_word]=[word]
            else:
                dict[sorted_word].append(word)
    
        return dict.values()