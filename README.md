#T2A3 Assessment
##Mark Lee

This virtualised application will pull stock data from the internet and suggest an investing approach.

API call.
Using Pandas_datareader to handle the api call to yahoo finance, the get request will pull the High, Low, Open, Close , Volume, and Adjusted Close prices from begining of financial year 2020 and assign it to the variable "df".

Data export.
data with today's(current date) date will be exported to file "stock_data.json".

Class instances and methods
A base class "Analysis" will have the following default attributes:
    AUD currency
    50 trust_level
    5 days to execute
    $10000 to invest

it will instantiate itself with mandatory parameters o_price (Open price), c_price (close price)

cidi document
workflow

mypy