import pandas as pd
from tkinter import filedialog


# select data using file picker

def get_symbols_from_csv():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        # consume csv/excel and generate a dataframe
        comp_raw = pd.read_csv(file_path)
        series = comp_raw[['Symbol', 'Security Name']]
        # print(series)
        symbol_tuples = list(zip(series['Symbol'], series['Security Name']))
        # print(symbol_tuples)
        output = "./stock_symbols.py"

        with open(output, "w") as file:
            file.write("stock_symbols = [\n")  # changed here
            for row in symbol_tuples:
                line = f'("{row[0]}", "{row[1]}"),\n'
                file.write(line)
            file.write("]\n")  # change here?

    else:
        print("File not found")

#  taken from chat gpt: read and understand and modify


def read_symbols_from_file():
    tuple_list = []
    with open("./stock_symbols.py") as file:
        # Skip the first line containing "stock_symbols = ["
        next(file)
        for line in file:
            # Stop when reaching the line containing "]"
            if "]" in line:
                break
            tuple_list.append(eval(line.strip()))

    return tuple_list
