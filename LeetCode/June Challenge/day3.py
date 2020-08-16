class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        l=len(costs) >> 1
        print(l)
        return (sum([x for x,y in costs]) + sum(sorted([y-x for x,y in costs])[:l]))