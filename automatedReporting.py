import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

excel_file_1 = './sample_data/shift-data.xlsx'
excel_file_2 = './sample_data/third-shift-data.xlsx'

dataFrame_first_shift = pd.read_excel(excel_file_1, sheet_name='first')
dataFrame_second_shift = pd.read_excel(excel_file_1, sheet_name='second')
dataFrame_third_shift = pd.read_excel(excel_file_2)

dataFrame_all = pd.concat([dataFrame_first_shift, dataFrame_second_shift, dataFrame_third_shift])

pivot = dataFrame_all.groupby(['Shift']).mean()
shift_productivity = pivot.loc[:,"Production Run Time (Min)":"Products Produced (Units)"]
# print(shift_productivity)

# shift_productivity.plot(kind='bar')
# plt.show()

dataFrame_all.to_excel("automated-report.xlsx")
