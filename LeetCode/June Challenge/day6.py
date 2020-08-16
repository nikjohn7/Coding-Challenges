class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        result = []
        people.sort(key = lambda a: (-a[0], a[1]))
        for x in people: result.insert(x[1], x);
        return result