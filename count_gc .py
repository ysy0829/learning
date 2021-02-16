#!/bin/python3
# -*- coding: utf-8 -*-

"""
Created on Feb 10 2021

@author: BigB
"""

from optparse import OptionParser


def count_gc(file):

    with open(file, 'r') as file:

        total_g, total_c, total, label1, label2 = 0, 0, 0, 0, 1
        for line in file:

            if line[0] == '>':
                label1 += 1
                if label1 != label2:
                    print('{}{:.4f}%'.format(tag, ((total_g + total_c) / total) * 100))
                    label2, total_g, total_c, total = label1, 0, 0, 0
                tag = line
            else:
                line = line.upper()
                g = line.count('G')
                c = line.count('C')
                line = line.replace('N', '')
                linenum = len(line)
                total_g, total_c, total = total_g+g, total_c+c, total+linenum
                
        print('{}{:.4f}%'.format(tag, ((total_g + total_c) / total) * 100))

    return


parser = OptionParser()
parser.add_option('-f', action='store', type='string', dest='filename')
(options, args) = parser.parse_args()
filename = options.filename
count_gc(filename)







