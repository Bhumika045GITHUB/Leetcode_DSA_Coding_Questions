class Solution(object):
    def bestHand(self, ranks, suits):
        #ranks = [13,2,3,1,9], suits = ["a","a","a","a","a"]
        counter = Counter(ranks)
        if len(set(suits)) == 1:
            return "Flush"
        elif max(counter.values()) >= 3:
            return "Three of a Kind"
        elif max(counter.values()) == 2:
            return "Pair"
        else:
            return "High Card"
        