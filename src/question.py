from ticker_codes import asx_codes

#Ask the user to enter a stock ticker code, if the code does NOT correlate to an entry in ticket_codes.py, prompt user and ask again.
def user_stock():
    stock_query: str = input("Enter stock code to analyse (e.g. CBA): ")
   
    if stock_query.upper() in asx_codes:
        return stock_query
   
    elif stock_query.upper() not in asx_codes:
        
        print("No stock with that code found")
        return user_stock()
