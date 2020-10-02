import mypy #type: ignore
import datetime as dt #type: ignore
from api import data_frame #type: ignore

class Analysis:
    def __init__(self, o_price: int, c_price: int):
        self.open_price = o_price
        self.close_price = c_price
        self.advice_date = dt.date.today()
        
    def buy_or_sell(self):
        if self.open_price > self.close_price:
            return """    __.-._
    '-._"7'
     /'.-c
     |  /T
    _)_/LI
mmMMmmmm...Value may be had - BUY, you should!"""
        if self.open_price < self.close_price:
            return "mmMMmmmm...dark side is strong - SELL, i fear!"
            
    @staticmethod
    def current_date():
        now = dt.datetime.today()
        return now
            
o_price = data_frame["Open"][-1]
c_price = data_frame["Adj Close"][-1]

buy = Analysis(o_price, c_price)
