# -*- coding: utf-8 -*-
import os
import pandas
import pprint as p
# return abs path of .py
_path = os.path.dirname(os.path.abspath(__file__))

""" .csv should in the same folder with this .py file
    :return test_data:  `list`
    Store data by raw format 
    
"""
def get_test_data(file_name=r'checklist.csv'):
    df = pandas.read_csv(os.path.join(_path,file_name))
    test_data=[]
    df = df.fillna(value="Skip")
    for i in df.index.values:
        row_data=df.loc[i,
        ['produc_name','os_platform','os_version','driver_type','driver_name','driver_link']
        ].to_dict()
        test_data.append(row_data)

    return test_data

# c = get_test_data()
# p.pprint(c)