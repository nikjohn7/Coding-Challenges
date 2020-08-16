class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x1,y1 = coordinates[0][0], coordinates[0][1]
        x2,y2 = coordinates[1][0], coordinates[1][1]
        if x2==x1:
            m='inf'
        else:
            m = abs((y2-y1)/(x2-x1))
        if len(coordinates)==2:
            return True
        for i in range(2,len(coordinates)):
            xi, yi = coordinates[i][0],coordinates[i][1]     
            if x2==xi:
                if m=='inf':
                    return True 
                else:
                    return False
            if abs((y2-yi)/(x2-xi)) == m:
                return True
            else:
                return False