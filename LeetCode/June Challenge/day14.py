from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graphs=defaultdict(list)
        hq=[]
        for u,v,w in flights:
            graphs[u].append((w,v))

        heapq.heappush(hq,(0, K+1, src))
        while hq:
            price, stops, city = heapq.heappop(hq)
            if city is dst: 
                return price
            if stops>0:
                for price_to_nei, nei in graphs[city]:
                    heapq.heappush(hq, (price+price_to_nei, stops-1, nei))

        return -1