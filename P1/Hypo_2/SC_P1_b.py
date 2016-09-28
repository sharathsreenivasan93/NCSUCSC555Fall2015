# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 17:19:44 2015

@author: sreenivasanh
"""

from decimal import *
import collections
import pandas as pd

def degree_of_intersection():
    global indi_circle_list
    global circle_names
    global degree_of_inter
    f = open('686.circles','r')
    indi_circle_dict={}
    indi_degree_of_intersection_list=[]
    for line in f:
        line2 = line.split()
        indi_circle_set=set()
        for node in line2[1:]:
            indi_circle_set.add(node)
        indi_circle_list.append(indi_circle_set)
        indi_circle_dict[line2[0]]=0
    for i in indi_circle_list:
        ratio = 0
        for j in indi_circle_list:
            if i!=j:
                ratio = ratio + Decimal(Decimal(len(set.intersection(i,j))+ Decimal(1))/Decimal(len(set.union(i,j)) + Decimal(1)))
        indi_degree_of_intersection_list.append(ratio)
    degree_of_inter = collections.OrderedDict(sorted(indi_circle_dict.items()))
    circle_names = degree_of_inter
    j=0
    for i in degree_of_inter.keys():
        degree_of_inter[i]=indi_degree_of_intersection_list[j]
        j = j + 1
    return degree_of_inter

def density():
    global indi_circle_list
    global circle_names
    global density_dict
    max_edges_in_circle_list=[]
    for i in indi_circle_list:
        max_edges_in_circle_list.append(len(i)*(len(i)-1)/2)
    present_edges_in_circle = []
    for i in range(0,len(max_edges_in_circle_list)):
        present_edges_in_circle.append(0)  
    for i in range(0,len(max_edges_in_circle_list)):
        f = open ('686.edges','r')
        for line in f:
            line2 = line.split()
            count = 0
            for node in line2:
                if str(node) in indi_circle_list[i]:
                    count = count + 1
            if count == 2:
                present_edges_in_circle[i] = present_edges_in_circle[i] + 1
    density_dict = circle_names
    k = 0   
    for i in density_dict.keys():
        density_dict[i] = Decimal(Decimal(present_edges_in_circle[k])/Decimal(max_edges_in_circle_list[k]))
        k = k + 1
    return density_dict

def input_to_csv():
    deg = degree_of_intersection()
    degree_of_inters = pd.Series(deg)
    df1 = pd.DataFrame(degree_of_inters, columns=['Degree of intersection'])
    density_of_each_circle = density()
    density_of_each_cir = pd.Series(density_of_each_circle)
    df2 = pd.DataFrame(density_of_each_cir, columns=['Density of each circle'])
    df = pd.concat([df1,df2], join='outer', axis='1')
    df2 = df.sort(columns = 'Density of each circle', ascending=False)
    df2.index.name="Node ID"
    df2.to_csv('hypo2.csv')

indi_circle_list = []
circle_names = collections.OrderedDict()
density_dict = collections.OrderedDict()
degree_of_inter = collections.OrderedDict()
    
if __name__ == '__main__':
    input_to_csv()