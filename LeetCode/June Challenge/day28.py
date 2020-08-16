class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graphs = collections.defaultdict(list)
        for source, dest in tickets:
            graphs[source].append(dest)

        for source in graphs:
            graphs[source].sort(reverse = True)

        stack = ['JFK']
        result = []

        while stack:

            while graphs[stack[-1]]:
                stack.append(graphs[stack[-1]].pop())
            else:
                result.append(stack.pop())

        return result[::-1]