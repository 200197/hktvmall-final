import os
import pandas as pd
import numpy as np
import sqlite3 as sql
import glob
from setting import *

def all_to_database(month):
    os.chdir(split_item_location)
    extension = 'csv'
    files = glob.glob('*.{}'.format(extension))
    files_csv = [f for f in files if f[-6:-4] == month]

    df = pd.DataFrame()
    for f in files_csv:
        data = pd.read_csv(f, index_col = 0)
        df = df.append(data)
        print(f)

    outdir = overview_view_location
    path = os.path.join(outdir, '2021'+month+'.csv')
    df.to_csv(path, encoding='utf-8-sig')
    print('=========================20' + month + '.csv output finish=========================')

os.chdir(overview_view_location)
'''
outdir = overview_view_location
outfilename = "all data.db"
df = pd.read_excel("full list.xlsx", index_col = 0, engine='openpyxl')
df7 = pd.read_csv("202107.csv", index_col = 0)
df8 = pd.read_csv("202108.csv", index_col = 0)
df9 = pd.read_csv("202109.csv", index_col = 0)
path = os.path.join(outdir, outfilename)
conn = sql.connect(path)
cur = conn.cursor()
df.to_sql('list', conn, if_exists='replace', index=True)
df7.to_sql('item2107', conn, if_exists='replace', index=True)
df8.to_sql('item2108', conn, if_exists='replace', index=True)
df9.to_sql('item2109', conn, if_exists='replace', index=True)
conn.commit()
conn.close()
print(outfilename + "output success")
'''
conn = sql.connect("all data.db")
db = conn.cursor()
query = """select list.CPICode, list.ProductID, list.ProductName, list.ProductDesc, list.PopularityRank, item2109.categorygrp, item2107.category as jul, item2108.category as aug, item2109.category as sep, list.status
            from list
            left join item2107 on item2107.productid = list.ProductID
            left join item2108 on item2108.productid = list.ProductID
            left join item2109 on item2109.productid = list.ProductID
            group by list.ProductID
            order by list.CPICode asc, list.PopularityRank asc"""

result = db.execute(query).fetchall()
list = [i[0] for i in db.description]
df = pd.DataFrame.from_records(result, columns=list)
df.to_excel("overview.xlsx", encoding='utf-8-sig', index=False)
print("overview output success")

#all_to_database('07')
#all_to_database('08')
#all_to_database('09')