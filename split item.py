import pandas as pd
import numpy as np
import os
import glob
from setting import *

outdir = 'C:/Users/hhng/Desktop/HKtvmall/split item'
location = 'C:/Users/hhng/Desktop/HKtvmall/'
A1 = 'HKTV_(A1)Supermarket'
A2 = 'HKTV_(A2)PersonalCareAndHealth'
A3 = 'HKTV_(A3)SkincareAndMakeup'
A4 = 'HKTV_(A4)MotherAndBaby'
A5 = 'HKTV_(A5)Pets'
A6 = 'HKTV_(A6)ElectricalAppliances'
A7 = 'HKTV_(A7)Housewares'
A9 = 'HKTV_(A9)SportsAndTravel'
A10 = 'HKTV_(A10)ToysAndBooks'
A11 = 'HKTV_(A11)Fashion'
A14 = 'HKTV_(A14)ThirteenLandmarks'

def splite_data(date, type):
    num = str(date)
    os.chdir(location + type)
    extension = 'xlsx'
    files = glob.glob('*.{}'.format(extension))
    files_xls = [f for f in files if f[-18:-12] == num]

    df = pd.DataFrame()
    for f in files_xls:
        data = pd.read_excel(f, index_col=0, engine='openpyxl')
        data['salesnumber'] = data['salesnumber'].astype(str).str.replace(',', '').astype(np.float64)
        data['category'] = data['category'].str.replace("/", "")
        df = df.append(data)

    category = df['category'].unique()

    for i in category:
        outfilename = i + num + '.csv'
        path = os.path.join(outdir, outfilename)
        df[df['category'] == i].to_csv(path, encoding='utf-8-sig')
        print(f"{outfilename} output finish.")
    print('=========================20'+ num + ' finish=========================')

def splite_all_files(type):
    splite_data(202107, type)
    splite_data(202108, type)
    splite_data(202109, type)

splite_all_files(A1)
splite_all_files(A2)
splite_all_files(A3)
splite_all_files(A4)
splite_all_files(A5)
splite_all_files(A6)
splite_all_files(A7)
splite_all_files(A9)
splite_all_files(A10)
splite_all_files(A11)
splite_all_files(A14)