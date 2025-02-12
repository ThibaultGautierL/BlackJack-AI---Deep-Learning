class Card :
    def __init__(self, value, symbol, number, state):
        self.value = value
        self.symbol = symbol
        self.number = number
        self.state = state

    def show(self):
        print(f"{self.number} {self.symbol}. Value : {self.value}")
