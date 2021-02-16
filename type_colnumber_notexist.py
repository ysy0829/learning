# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 09:54:30 2020

@author: BigB
"""

sample_name=[]

with open('./sample_type.txt') as f1:
    for i1 in f1:
        i1=i1.replace('\n', '')
        i1=i1.split('\t')
        sample_name.append(i1[0])

sample_name_num=[]

with open('./title_number.txt') as f2:
    for i2 in f2:
        i2x=i2.replace('\n', '')
        i2xx=i2x.replace(' ', '')
        i2xx=i2xx.split('\t')
        sample_name_num.append(i2xx)
        

exist_list=[]
total_list=[]
for sample in sample_name:
    for sample_num in sample_name_num:
        if sample == sample_num[1]: 
            exist_list.append(sample_num[0])
for sample_num in sample_name_num:
    total_list.append(sample_num[0])
            

not_exist_list=[item for item in total_list if not item in exist_list]
for i in not_exist_list:
    print('{},'.format(i),end='')

print()

