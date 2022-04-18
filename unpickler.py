import pickle
import pandas as pd
import os
import csv
from tkinter import filedialog, messagebox
import tkinter as tk

tk.Tk().withdraw()
pathname = filedialog.askopenfilename()
file_name = os.path.split(pathname)[-1]
nominal_file = os.path.splitext(file_name)[0]
print(nominal_file)
file = open(pathname, 'rb')
Data = pickle.load(file)
file.close()
print(Data)

data = {}
TCsList = []
for key in Data.keys():
    TCsList.append(key)

print(TCsList)
df1 = {}
df2 = {}
df3 = {}
df_list = [df1, df2, df3]

frame_list = []
for df, TC in zip(df_list, Data.keys()):
    df = pd.DataFrame.from_dict(Data[TC])
    df = df.rename(columns={'time':TC+' time', 'data':TC+' data'})
    frame_list.append(df)

df_c = frame_list[0].join(frame_list[1:])
saveas = filedialog.asksaveasfilename(initialdir='.', filetypes=[('CSV Files', '.csv')], initialfile=nominal_file+'.csv')
df_c.to_csv(saveas, index=False)
