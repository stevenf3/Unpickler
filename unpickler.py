import pickle
import pandas as pd
import os
import csv
from tkinter import filedialog, messagebox
import tkinter as tk

tk.Tk().withdraw()
directory = filedialog.askopenfilename()
filename = open(directory, 'rb')
Data = pickle.load(filename)
filename.close()
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
saveas = filedialog.asksaveasfilename(initialdir='.', filetypes=[('CSV Files', '.csv')])
df_c.to_csv(saveas, index=False)
