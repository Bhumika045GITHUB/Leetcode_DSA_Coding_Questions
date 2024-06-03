class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        arr = []
        for i in range(len(words)):
            for letter in words[i]:
                if letter == x:
                    arr.append(i)
                    break
        return arr