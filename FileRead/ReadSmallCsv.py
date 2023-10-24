# -*- coding: utf-8 -*-
import csv
import os
import igraph
import chardet as chardet
# import pygraph.classes.directed_graph
import networkx as nx
import matplotlib.pyplot as plt
from FileRead.MyFliter import publicationDate_Fliter, paperID_Fliter
# import cugraph
# import cudf
from collections import OrderedDict
path = "C:\\Users\\Ac\\PycharmProjects\\BUAA_Course_DataMining\\data\\small"
save_path="C:\\Users\\Ac\\PycharmProjects\\BUAA_Course_DataMining\\data\\"
dirs = os.listdir(path)
rows = []
filenamelist = []
for file in dirs:
    print(file)
file = "papers_small.csv"
#
#
# # paperID	title	publicationDate	referenceCount	citationCount	conferenceID	journalID
def get_encoding(file):
    # 二进制方式读取，获取字节数据，检测类型
    with open(file, 'rb') as f:
        return chardet.detect(f.read())['encoding']
        # -->MacRoman
# print(get_encoding(path + "\\" + file))
def recentfind(s,r):
    for i in range(0,len(r)):
        if r[i][0]==s:
            return i
    return -1
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
#
f = open(save_path+'AS1result.txt','w',encoding='MacRoman')
for i in rows:
    string=''.join(i)+'\n'
    f.write(string)
f.close()
#
citefile='paperReference_small.csv'
edge=[]
with open(path + "\\" + citefile, encoding='MacRoman') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        edge.append((row['citingPaperID'],row['citedPaperID']))
print(edge)

G=nx.DiGraph()
# 创建有向图
# g=igraph.TupleList(edge, directed=False, vertex_name_attr='name', edge_attrs=None, weights=False)
# G = igraph.DiGraph()
# 设置有向图的边集合
# edges = [("A", "B"), ("A", "C"), ("A", "D"), ("B", "A"), ("B", "D"), ("C", "A"), ("D", "B"), ("D", "C")]
# 在有向图G中添加边集合

# G.add_edge(edge[0][0], edge[0][1])
# G.add_edge(edge[1][0], edge[1][1])

for i in edge:
    G.add_edge(i[0], i[1])
# # 有向图可视化
# layout = nx.spring_layout(G)
# # layout = nx.circular_layout(G)
#
# # layout = nx.shell_layout(G)
# # # nx.draw(G, pos=layout, with_labels=True, hold=False)
# nx.draw(G, pos=layout, with_labels=True)
# plt.show()
# #
# # # 计算简化模型的PR值
# pr = nx.pagerank(G, alpha=1)
# print("简化模型的PR值：", pr)
# #
# # # 计算随机模型的PR值
pr = nx.pagerank(G, alpha=0.85,max_iter=1000)
print("随机模型的PR值：", pr)

rank=sorted(pr.items(), key=lambda k: k[1], reverse=True)
NUM=0
i=0
ans=[]
while 1:
    x=recentfind(rank[i][0],rows)
    if not x==-1:
        print(rows[x])
        print(x)
        ans.append(rows[x])
        NUM+=1
    if NUM==10:
        break
    i+=1
# import DaPy as dp
# from DaPy.methods import PageRank
# from numpy.random import random
# shape = 10000
# mat = random((shape, shape))
# mat /= mat.sum(axis=0)
# pg = PageRank(engine='numpy', random_walk_rate=0.85)
# node_weight = pg.transform(edge)

# pg = g.pagerank()
# pg = g.pagerank(vertices=None, directed=True, damping=0.85,
#                 weights=weights, arpack_options=None,
#                 implementation='prpack',
#                 niter=1000, eps=0.001)
# pgvs = []
# for p in zip(g.vs, pg):
#     pgvs.append({"name": p[0]["name"], "pg": p[1]})
# # print pgvs
# sorted(pgvs, key=lambda k: k['pg'], reverse=True)[:10]
f1 = open(save_path+'result.txt','w',encoding='MacRoman')
for i in ans:
    string=' '.join(i)+'\n'
    f1.write(string)
f1.close()