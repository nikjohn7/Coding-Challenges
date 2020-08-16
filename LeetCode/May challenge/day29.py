class Solution:
    def canFinish(self, numCourses, prerequisites):
        self.adj_dict = defaultdict(set)
        for i, j in prerequisites:
            self.adj_dict[i].add(j)

        self.Visited = [0] * numCourses
        self.FoundCycle = 0

        for i in range(numCourses):
            if self.FoundCycle == 1: break   # early stop if the loop is found
            if self.Visited[i] == 0:
                self.DFS(i)

        return self.FoundCycle == 0

    def DFS(self, start):
        if self.FoundCycle == 1:   return     # early stop if the loop is found    
        if self.Visited[start] == 1:
            self.FoundCycle = 1               # loop is found
        if self.Visited[start] == 0:           # node is not visited yet, visit it
            self.Visited[start] = 1             # color current node as gray
            for neib in self.adj_dict[start]:   # visit all its neibours
                self.DFS(neib)
            self.Visited[start] = 2