class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        counter = 0
        capacity_now = capacity
        for i in range(len(plants)):
            if(capacity_now>=plants[i]):
                capacity_now-=plants[i]
                counter +=1
            else:
                counter +=(2*i)+1
                capacity_now = capacity - plants[i]
        return counter
            