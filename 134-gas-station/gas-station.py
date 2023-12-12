class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        start=0
        tag=0
        for i in range(len(gas)):
            tag+=gas[i]-cost[i]
            if tag<0:
                start=i+1
                tag=0
        return start

            