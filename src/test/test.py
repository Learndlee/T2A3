import unittest  # type: ignore
from classes import Analysis  # type: ignore


# test if open price is lower then close price == sell
class TestAnalysis(unittest.TestCase):
    def test_buy_sell(self):

        # test if open price is lower then close price == sell
        stock = Analysis(2, 6)
        self.assertEqual(stock.buy_or_sell(), 
        "mmMMmmmm...dark side is strong - SELL, i fear!")
        # test if open price is higher then close price == buy
        stock = Analysis(6, 2)
        self.assertEqual(stock.buy_or_sell(), """    __.-._
    '-._"7'
     /'.-c
     |  /T
    _)_/LI
mmMMmmmm...Value may be had - BUY, you should!""")
