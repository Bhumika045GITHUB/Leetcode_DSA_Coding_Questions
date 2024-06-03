class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        answer = []
        for i in range(len(words)):
            for letter in words[i]:
                if letter == x:
                    answer.append(i)
                    break
        return answer