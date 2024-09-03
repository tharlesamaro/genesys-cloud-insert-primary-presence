from datetime import datetime

def convert_date(input_string: str):
    dt = datetime.strptime(input_string, "%Y-%m-%d %H:%M:%S.%f%z")
    return dt.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]