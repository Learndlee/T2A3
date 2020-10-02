from api import data_frame  # type: ignore
# import mypy #type: ignore

# output data from api input to json file
data_frame.tail(1).to_json("raw_stock_data.json")
