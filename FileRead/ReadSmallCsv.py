# -*- coding: utf-8 -*-
import csv
import os

import chardet as chardet
import networkx as nx
import matplotlib.pyplot as plt
from FileRead.MyFliter import publicationDate_Fliter, paperID_Fliter

path = "..\\data\\A1Dataset\\small"
save_path="..\\data\\"
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
    k=0
    for row in reader:
        if  paperID_Fliter(row["paperID"],k)\
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
        k += 1
print()
print("read "+file+" end")

f = open(save_path+'AS1result.txt','w',encoding='MacRoman')
for i in rows:
    string=''.join(i)+'\n'
    f.write(string)
f.close()

citefile='paperReference_small.csv'
edge=[]
with open(path + "\\" + citefile, encoding='MacRoman') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        edge.append((row['citingPaperID'],row['citedPaperID']))
print(edge)


# 创建有向图
G = nx.DiGraph()
# 设置有向图的边集合
# edges = [("A", "B"), ("A", "C"), ("A", "D"), ("B", "A"), ("B", "D"), ("C", "A"), ("D", "B"), ("D", "C")]
# 在有向图G中添加边集合
for i in edge:
    G.add_edge(i[0], i[1])

# 有向图可视化
# layout = nx.spring_layout(G)
# layout = nx.circular_layout(G)
layout = nx.shell_layout(G)
# nx.draw(G, pos=layout, with_labels=True, hold=False)
nx.draw(G, pos=layout, with_labels=True)
plt.show()

# 计算简化模型的PR值
pr = nx.pagerank(G, alpha=1)
print("简化模型的PR值：", pr)

# 计算随机模型的PR值
pr = nx.pagerank(G, alpha=0.85)
print("随机模型的PR值：", pr)
