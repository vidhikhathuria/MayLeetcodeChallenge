# Problem Link : https://leetcode.com/problems/online-stock-span/


class StockSpanner:

    def __init__(self):
        self.st = []

    def next(self, price: int) -> int:
        span = 1
        if len(self.st) > 0:
            # print()
            # print(self.st, len(self.st), price)
            var = self.st[len(self.st) - 1]
            index = len(self.st) - 1
            while var[0] <= price and index > -1:
                # print(price, var, span, index)
                span += var[1]
                n = var[1]
                if index - n < 0:
                    break
                else:
                    var = self.st[index - n]
                    index = index - n

        self.st.append((price, span))
        return span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)