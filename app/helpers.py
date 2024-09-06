from datetime import datetime


def convert_date(input_string: str):
    try:
        dt = datetime.strptime(input_string, "%Y-%m-%d %H:%M:%S.%f%z")
    except ValueError:
        try:
            dt = datetime.strptime(input_string, "%Y-%m-%d %H:%M:%S%z")
        except ValueError:
            raise ValueError("Formato de data e hora não reconhecido")

    if "." in input_string:
        output = dt.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]
    else:
        output = dt.strftime("%Y-%m-%dT%H:%M:%S.000")

    return output
