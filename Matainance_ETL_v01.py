import pandas as pd
import os
from datetime import datetime


target_directory = "C:/Users/USER/Desktop/Data/Target/"
source_folder = "C:/Users/USER/Desktop/Data/"


def extraction():
    file = "{directory}MaintenanceReportMonthly.xlsx".format(directory=source_folder)
    df = pd.read_excel(file,engine="openpyxl")
    print("Completed extract file")
    return df

def transform(df):
    for i, column in enumerate(df.columns):
        if i >= 4:
            for j in df.index:
                if df.iloc[j,i] == "0":
                    df.iloc[j,i] = 0
                else:
                    df.iloc[j,i] = 1
    return df

def load(df):
    DT = datetime.now()
    dt = DT.strftime("%m%d%y%H%M%S")
    output_filename = input("Please input the file name:\n")
    output_filename = output_filename+"@"+dt
    targetfile = "{path}{filename}.xlsx".format(path=target_directory,filename=output_filename)
    if os.path.exists(targetfile):
        print("The file exists")
    else:
        df.to_excel(targetfile,sheet_name="MaintenanceReportMonthly")

data = extraction()
transformed = transform(data)
load(transformed)
print("Completed!")

