import datetime as dt  # type: ignore
import pandas_datareader.data as web  # type: ignore
from question import user_stock  # type: ignore

# modify stock code to include country code and save as stock_query_ax
stock_query_ax: str = user_stock()+".ax"

print()
print("***>" + stock_query_ax.upper())

# only get data between these dates
start_date = dt.datetime(2020, 7, 1)
end_date = dt.datetime.today()

# Pandas_Datareader api to pull data from yahoo finance, based on user input
data_frame = web.DataReader(stock_query_ax, "yahoo", start_date, end_date)


print(data_frame.tail(5))
