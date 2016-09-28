# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 10:16:49 2015

@author: sreenivasanh
"""
import collections
import pandas as pd

def number_of_circles():
    my_dict_nodes_circles = {}
    f = open ('698.circles','r')
    my_set_nodes = set()
    for line in f:
        line2 = line.split()
        for node in line2[1:]:
            my_set_nodes.add(node)
    my_dict_nodes_circles = dict.fromkeys(my_set_nodes,0)
    f = open ('698.circles','r')
    for line in f:
        line2 = line.split()
        for node in line2[1:]:
            if node in my_dict_nodes_circles.keys():
                my_dict_nodes_circles[node]=my_dict_nodes_circles[node]+1
    return my_dict_nodes_circles

def number_of_common_features():
    f = open('698.egofeat','r')
    for line in f:
        ego_nodes = line.split()
    my_features_list = []
    my_features_names = collections.OrderedDict()
    f = open('698.feat','r')
    for line in f:
        line2=line.split()
        my_features_list.append(line2[1:])
        my_features_names[line2[0]]=0
    count_list = []
    for feature in my_features_list:
        count = 0
        for i in range(0,len(feature)):
            if feature[i] == ego_nodes[i] and int(feature[i]) == 1:
                count = count + 1
        count_list.append(count)
    k = 0
    for name in my_features_names.keys():
        my_features_names[name]=count_list[k]
        k = k+1
    return my_features_names

def input_to_csv():
    my_features_common = number_of_common_features()
    my_features = pd.Series(my_features_common)
    df1 = pd.DataFrame(my_features, columns=['Number of common features with ego nodes'])
    my_nodes_common = number_of_circles()
    my_nodes = pd.Series(my_nodes_common)
    df2 = pd.DataFrame(my_nodes, columns=['Number of common circles'])
    df = pd.concat([df1,df2], join='outer', axis='1')
    df2 = df.sort(columns = 'Number of common circles', ascending=False)
    df2.index.name="Node ID"
    df2.to_csv('hypo3.csv')
    

if __name__ == '__main__':
    input_to_csv()