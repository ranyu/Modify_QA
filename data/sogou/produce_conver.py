#!/usr/bin/env python
# coding=utf-8

split_symbol = ' +++$+++ '
flag = 0 

with open('./sample1_deepqa_3M_conversation.txt','w') as fw:
    while flag < 2000000:
        fw.write('u0'+split_symbol+'u1'+split_symbol+'m0'+split_symbol+'[\'L'+str(flag)+'\', \'L'+str(flag+1)+'\']'+'\n')
        flag += 2
