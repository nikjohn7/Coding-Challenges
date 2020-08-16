class StockSpanner:

    def __init__(self):
        self.arr = []

    def next(self, price: int) -> int:
        count =  1
        
        while self.arr and self.arr[-1][0] <= price:
            count+=self.arr.pop()[1]
        self.arr.append((price, count))
        return count