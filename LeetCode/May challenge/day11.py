class Solution:
    def _init_(self):
        self.oldColor=0
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        self.oldColor=image[sr][sc]
        self.DFS(image, sr, sc, newColor)
        return image
    
    def DFS(self, image: List[List[int]], row: int, col: int, newColor: int):
        if row < 0 or row >= len(image) or col < 0 or col >= len(image[0]) or image[row][col] == newColor:
            return 
        if(image[row][col] == self.oldColor):
            image[row][col] = newColor
            self.DFS(image, row + 1, col, newColor)
            self.DFS(image, row - 1, col, newColor)
            self.DFS(image, row, col + 1, newColor)
            self.DFS(image, row, col - 1, newColor)
                