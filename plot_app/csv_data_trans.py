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
        output = "stock_symbols.txt"
        with open(output, "w") as file:
            for row in symbol_tuples:
                line = f"({row[0]}, {row[1]}),\n"
                file.write(line)
            file.close()

        return symbol_tuples
    else:
        print("File not found")

get_symbols_from_csv()
