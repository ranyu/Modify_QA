#!/usr/bin/env python
# coding=utf-8

split_symbol = ' +++$+++ '
flag = 0 

with open('./sample1_deepqa_3M_lines.txt','w') as fw:
    with open('../../../sample1_30M_utf_8.txt','r') as f:
        for data in f:
            fw.write('L'+str(flag)+split_symbol+'u0'+split_symbol+'m0'+split_symbol+'RANYU'+split_symbol)
            for ele in data.strip().split()[:4]:
                fw.write(ele+' ')
            fw.write('\n')
            flag += 1
            fw.write('L'+str(flag)+split_symbol+'u0'+split_symbol+'m0'+split_symbol+'KOBE'+split_symbol)
            for ele in data.strip().split()[4:]:
                fw.write(ele+' ')
            fw.write('\n')
            flag += 1
