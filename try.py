# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 12:04:52 2019

@author: Evan
"""

import csv
import os


work_dir = os.getcwd()
pdf_dir = os.path.join(work_dir, 'pdf')
txt_dir = os.path.join(work_dir, 'txtDir')

RESULT = ['apple','cherry','orange','pineapple','strawberry']
with open('output.csv','w', encoding="big5") as result_file:
    wr = csv.writer(result_file, dialect='excel')
    try:
        wr.writerow(content)
    except UnicodeEncodeError as e:
        pass