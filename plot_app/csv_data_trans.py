import pandas as pd
from tkinter import filedialog


# select data using file picker
def get_symbols_from_csv():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        # consume csv/excel and generate a dataframe
        comp_raw = pd.read_csv(file_path)
        print(comp_raw)

        comp_filter = comp_raw.itertuples(name=None)

        comp_filter = comp_raw.to_string(columns=['Symbol', 'Security Name'],
                                         # formatters={
                                         #     'Symbol': '('.format,
                                         #     'Security Name': ')'.format
                                         # },
                                         justify="left",  header=False, index=False)
        print(comp_filter)
        new_file = open("stock_symbols.txt", "w")
        print(comp_filter)
        new_file.write(comp_filter)
        new_file.close()
        f = open("All_Stocks.txt", "w")
        # return comp_filter
    else:
        print("File not found")


get_symbols_from_csv()
