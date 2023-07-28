import pandas as pd
from tkinter import filedialog


# select data using file picker
def get_symbols_from_csv():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        # consume csv/excel and generate a dataframe
        comp_raw = pd.read_csv(file_path)
        print(comp_raw)
        comp_sym = comp_raw.loc[:, ['Symbol', 'Name']]
        print(comp_sym)
        return comp_sym
    else:
        print("File not found")

