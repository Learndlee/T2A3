import datetime as dt #type: ignore
import pandas as pd #type: ignore
import pandas_datareader.data as web #type: ignore
import mypy #type: ignore
from question import user_stock  #type: ignore


stock_query_ax = user_stock()+".ax"
print()
print("***>" + stock_query_ax.upper())

start_date = dt.datetime(2020, 7, 1)
end_date = dt.datetime.today()


data_frame = web.DataReader(stock_query_ax, "yahoo", start_date, end_date)
print(data_frame.tail(5))
