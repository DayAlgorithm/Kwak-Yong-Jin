class StockSpanner:
    def __init__(self):
        self.stack = []
        self.prev = 0
    def next(self, price: int) -> int:
        if not self.stack:
            self.stack.append([price, 1])
        else:
            if price >= self.stack[-1][0]:
                while True:
                    if self.stack and price >= self.stack[-1][0]:
                        self.prev += self.stack[-1][1]
                        self.stack.pop()
                    else:
                        break
                self.stack.append([price, self.prev + 1])
            else:
                self.stack.append([price, 1])
        self.prev = 0
        return self.stack[-1][1]
