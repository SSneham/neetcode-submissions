class StockSpanner:

    def __init__(self):
        self.arr = []

    def next(self, price: int) -> int:
        count = 1
        for num in self.arr[::-1]:
            if num <= price:
                count += 1
            else:
                break
        self.arr.append(price)
        return count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)