import pandas as pd
import numpy as np
import os
import glob
import openpyxl
import csv
from setting import *
import openpyxl
import xlsxwriter

os.chdir(result_location)
extension = 'xlsx'
files = glob.glob('*.{}'.format(extension))
files_xls = [f for f in files if f[-11:-5] == 'result']

df = pd.DataFrame()
def rank(number, df):
    number = str(number)
    try:
        rank = int(df[15:16][number + 'rank'])
        df1 = df[df[number + 'rank'] <= rank]
        try:
            top16_number = int(df1.CPICode.value_counts().sum())
        except:
            top16_number = int(max(df[number+'rank']))

    except:
        rank = df.shape[0]
        df1 = df[df[number + 'rank'] <= rank]
        top16_number = int(df1.CPICode.value_counts().sum())

    return top16_number

summary = []
for f in files_xls:
    df_top16 = pd.read_excel(f, sheet_name='top16',engine='openpyxl')
    df_aug = pd.read_excel(f, sheet_name='aug top16',engine='openpyxl')
    df_jul = pd.read_excel(f, sheet_name='jul top16', engine='openpyxl')
    df_item = pd.read_excel(f, sheet_name='item',engine='openpyxl')

    sep_number_item_in_top_16 = rank('09', df_top16)
    aug_number_item_in_top_16 = rank('08', df_aug)
    jul_number_item_in_top_16 = rank('07', df_jul)

    CPICode = int(df_item['CPICode'][0:1])
    Unavailable_item = df_item.loc[df_item.status == '商品已下架', 'status'].count()

    file_name = os.path.basename(f)
    file_name_without_extension = os.path.splitext(file_name)[0]
    file_number = os.path.splitext(file_name_without_extension)[0]

    CPICode_name = os.path.splitext(file_name_without_extension)[1]
    CPICode_name = CPICode_name[1:-7]
    CPICode_name = CPICode_name.replace('_',' ')

    number_of_item = len(df_item['ProductID'])

    sep_unavailable_item = df_item['09rank'].isna().sum()
    aug_unavailable_item = df_item['08rank'].isna().sum()
    jul_unavailable_item = df_item['07rank'].isna().sum()

    sep_available_item = number_of_item - sep_unavailable_item
    aug_available_item = number_of_item - aug_unavailable_item
    jul_available_item = number_of_item - jul_unavailable_item

    summary.append({'Number': file_number,
                    'CPICode_name': CPICode_name,
                    'CPICode': CPICode,
                    'number_of_item': number_of_item,
                    'sep_available_item': sep_available_item,
                    'sep_unavailable_item': sep_unavailable_item,
                    'sep_number_item_in_top_16': sep_number_item_in_top_16,
                    'aug_available_item': aug_available_item,
                    'aug_unavailable_item': aug_unavailable_item,
                    'aug_number_item_in_top_16': aug_number_item_in_top_16,
                    'jul_available_item': jul_available_item,
                    'jul_unavailable_item': jul_unavailable_item,
                    'jul_number_item_in_top_16': jul_number_item_in_top_16,})

    print(file_name, 'appended')

data = pd.DataFrame(summary)
data['Number'] = data['Number'].astype(np.float64)
data = data.sort_values(by='Number', ascending=True)

writer = pd.ExcelWriter('summary.xlsx', engine='openpyxl', mode="w")
data.to_excel(writer, sheet_name='summary', encoding='utf-8-sig', index=False)
writer.save()

wb = openpyxl.load_workbook('summary.xlsx')
wb.worksheets[0].column_dimensions['A'].width = 20
wb.worksheets[0].column_dimensions['B'].width = 30
wb.worksheets[0].column_dimensions['C'].width = 20
wb.freeze_panes = 'A2'
ws = wb.active
ws.auto_filter.ref = ws.dimensions
wb.save('summary.xlsx')



