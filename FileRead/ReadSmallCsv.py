# -*- coding: utf-8 -*-
import csv
import os

import chardet as chardet

from FileRead.MyFliter import publicationDate_Fliter, paperID_Fliter

path = "C:\\Users\\11858\\Documents\\大四上\\数据挖掘\\data\\A1Dataset\\small"
save_path="C:\\Users\\11858\\Documents\\大四上\\数据挖掘\\data\\"
dirs = os.listdir(path)
rows = []
filenamelist = []
for file in dirs:
    print(file)
file = "papers_small.csv"


# paperID	title	publicationDate	referenceCount	citationCount	conferenceID	journalID
def get_encoding(file):
    # 二进制方式读取，获取字节数据，检测类型
    with open(file, 'rb') as f:
        return chardet.detect(f.read())['encoding']
        # -->MacRoman
# print(get_encoding(path + "\\" + file))

print()
print("read "+file+" begin")
print()
with open(path + "\\" + file, encoding='MacRoman') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if  paperID_Fliter(row["paperID"])\
                and publicationDate_Fliter(row["paperID"],row["publicationDate"], 10):
            rows.append([
                row["paperID"],
                row["title"],
                row["publicationDate"],
                row["referenceCount"],  # not int
                row["citationCount"],  # not int
                row["conferenceID"],
                row["journalID"],
            ])
print()
print("read "+file+" end")

f = open(save_path+'AS1result.txt','w',encoding='MacRoman')
for i in rows:
    string=''.join(i)+'\n'
    f.write(string)
f.close()
