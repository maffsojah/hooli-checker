# -*- coding: utf-8 -*-
#! /usr/bin/env python
"""
Created on Thu May  9 23:52:24 2019

@author: tmafura
"""
import csv
import pandas as pd

# reads the csv files, takes only the hooliId columns.
sam_accts=pd.read_csv("sam-accounts.csv", index_col=False, header=None)[0] 
exist_accts=pd.read_csv("existing-accounts.csv", index_col=False, header=None)[1]


sam_list=[]
exist_list=[]

for row in sam_accts:
    sam_list.append(row)
    
# take only the first 15 characters of the existing accounts hooliId
for row_2 in exist_accts:
    exist_list.append(row_2[:15])

# lists the set-difference of sam_accounts and existing_accounts and write to csv
data = list(set(sam_list)-set(exist_list))

with open('set-difference.csv', 'w', newline='\n') as csvFile:
    writer = csv.writer(csvFile)
    for info in data:
        writer.writerow([info])