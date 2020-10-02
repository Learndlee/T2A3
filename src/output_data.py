from api import data_frame #type: ignore
import mypy #type: ignore

data_frame.tail(1).to_json("raw_stock_data.json")