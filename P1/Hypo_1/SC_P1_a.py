# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 00:54:57 2015

@author: sreenivasanh
"""
import pandas as pd

my_dict = {}
my_dict_nodes_circles = {}

def node_degree():
    global my_dict
    f = open ('348.circles','r')
    my_set_nodes=set()
    for line in f:
        line2 = line.split()
        for node in line2[1:]:
            my_set_nodes.add(node)
    my_dict = dict.fromkeys(my_set_nodes,0)
    f = open ('348.edges','r')
    for line in f:
        for node in line.split():
            if node in my_dict.keys():
                my_dict[node]=my_dict[node]+1

def node_circles():
    global my_dict_nodes_circles
    f = open ('348.circles','r')
    my_set_nodes = set()
    for line in f:
        line2 = line.split()
        for node in line2[1:]:
            my_set_nodes.add(node)
    my_dict_nodes_circles = dict.fromkeys(my_set_nodes,0)
    f = open ('348.circles','r')
    for line in f:
        line2 = line.split()
        for node in line2[1:]:
            if node in my_dict_nodes_circles.keys():
                my_dict_nodes_circles[node]=my_dict_nodes_circles[node]+1

def input_into_csv():
    global my_dict
    global my_dict_nodes_circles
    degree_of_each_node = pd.Series(my_dict)
    df1 = pd.DataFrame(degree_of_each_node, columns=['Degree of each node'])
    number_of_circles = pd.Series(my_dict_nodes_circles)
    df2 = pd.DataFrame(number_of_circles, columns=['Number of circles'])
    df = pd.concat([df1,df2], join='outer', axis='1')
    df2 = df.sort(columns = 'Number of circles', ascending=False)    
    df2.index.name="Node ID"
    df2.to_csv('hypo1.csv')
    
if __name__ == '__main__':
    node_degree()
    node_circles()
    input_into_csv()