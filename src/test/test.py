import unittest #type: ignore
import mypy #type: ignore
from classes import Analysis #type: ignore


class TestAnalysis(unittest.TestCase):
    def test_buy_sell(self):
        stock = Analysis(2,6)
        self.assertEqual(stock.buy_or_sell(),"mmMMmmmm...dark side is strong - SELL, i fear!")
        stock = Analysis(6,2)
        self.assertEqual(stock.buy_or_sell(),"""    __.-._
    '-._"7'
     /'.-c
     |  /T
    _)_/LI
mmMMmmmm...Value may be had - BUY, you should!""")
