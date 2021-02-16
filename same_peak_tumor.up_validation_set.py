# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 09:54:30 2020

@author: BigB
"""

sample_name=[]

with open('./tumor_up_recordnum.txt') as f1:
    for i1 in f1:
        i1=i1.replace('\n', '')
        sample_name.append(i1)

sample_name_num=[]

with open('./validation_set_recordnum.txt') as f2:
    for i2 in f2:
        i2=i2.replace('\n', '')
        i2=i2.split(' ')
        sample_name_num.append(i2)
        

list=[]
for sample in sample_name:
    for sample_num in sample_name_num:
        if sample == sample_num[0]: 
            list.append(sample_num[1])

f = open ('./records.num.tumor.txt','w')

print('1,',end='',file=f)
for i in list:
    print('{},'.format(i),end='',file=f)

print('\n',file=f)
f.close()
