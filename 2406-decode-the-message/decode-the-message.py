class Solution(object):
    def decodeMessage(self, key, message):
        mapping = {' ': ' '}
        i = 0
        res = ''
        letters = 'abcdefghijklmnopqrstuvwxyz'
        
        #key = "the quick brown fox jumps over the lazy dog"
        #message = "vkbs bs t suepuv"
        for char in key:
            if char not in mapping:
                mapping[char] = letters[i]
                i += 1
        
        # res - "the five boxing wizards jump quickly"
        for char in message:
            res += mapping[char]
                
        return res
    
    