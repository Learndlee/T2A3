from ticker_codes import asx_codes


# Ask user to enter stock ticker code
# if the code doesn't exist in ticket_codes.py, prompt user again.
def user_stock():
    stock_query: str = input("Enter stock code to analyse (e.g. CBA): ")

    if stock_query.upper() in asx_codes:
        return stock_query

    elif stock_query.upper() not in asx_codes:

        print("No stock with that code found")
        return user_stock()
