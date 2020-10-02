import datetime as dt  # type: ignore
from api import data_frame  # type: ignore


# Base class Analysis
class Analysis:
    def __init__(self, o_price: int, c_price: int):

        # two mandatory and one optional parameters
        self.open_price = o_price
        self.close_price = c_price
        self.advice_date = dt.date.today()

        # class method
    def buy_or_sell(self):

        # control if open price>close price, stock might be cheap - buy
        if self.open_price > self.close_price:
            return """    __.-._
    '-._"7'
     /'.-c
     |  /T
    _)_/LI
mmMMmmmm...Value may be had - BUY, you should!"""

        # control if price has gone up, stock might be over priced - sell
        elif self.open_price < self.close_price:
            return "mmMMmmmm...dark side is strong - SELL, i fear!"

    # method univerisally available, not tied to a class
    @staticmethod
    def current_date():
        now = dt.datetime.today()
        return now


# access exact index from data_frame pandas data frame created from api.py
o_price = data_frame["Open"][-1]
c_price = data_frame["Adj Close"][-1]

# call buy instance of Analysis, using arguments derived from lines 37 & 38
buy = Analysis(o_price, c_price)
