from ticker_codes import asx_codes


# Ask user to enter stock ticker code
def user_stock():
    stock_query: str = input("Enter stock code to analyse (e.g. CBA): ")

    # Input sanitisation & validation
    if stock_query.upper() in asx_codes:
        return stock_query

    # if the code doesn't exist in ticket_codes.py, prompt user again.
    elif stock_query.upper() not in asx_codes:

        print("No stock with that code found")
        return user_stock()
