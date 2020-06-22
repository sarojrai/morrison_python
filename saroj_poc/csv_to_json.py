#!/usr/bin/python

import os
import csv
import json
import logging
import collections.abc

logging.basicConfig(filename='csv_to_json.log',format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

CSV_FILE = "data.csv"
INDEX_MAP, JSON_DATA = {}, []
filed_list = ["name","id","link"]
field_list_count = len(filed_list)


file_exist = True
try:
    fp = open(CSV_FILE, 'r')
    
    
except FileNotFoundError:
    
    file_exist = False
    logging.error(' File not found. Check the name of file')

if file_exist == True:

    for each_row in csv.reader(fp):
        column_length = len(each_row)
        no_of_branches = int(column_length / field_list_count)
        start_range = 0
        end_range = field_list_count
        index_list = []
        
        for i in range(0,no_of_branches):
            
            current_pos = i + int(1)
            if i == 0:
                name1, id1, url1 = each_row[start_range: end_range]
                index1 = INDEX_MAP.get(id1, -1)
                
                if index1 == -1:
                    JSON_DATA.append({"id": id1, "link": url1, "name": name1, "children": []})
                    index1 = INDEX_MAP[id1] = len(JSON_DATA) - 1
                    index_list.append([["index" + str(current_pos)],["children"]])
            elif i == no_of_branches - int(1):
                
                name3, id3, url3 = each_row[start_range : end_range]
                JSON_DATA[index1]["children"][index2]["children"].append({"id": id3, "link": url3, "name": name3, "children": []})
            else:
                
                name1, id1, url1 = each_row[start_range : end_range]
                index2 = INDEX_MAP.get(id1, -1)
                if index2 == -1:
                    JSON_DATA[index1]["children"].append({"id": id1, "link": url1, "name": name1, "children": []})
                    index2 = INDEX_MAP[id1] = len(JSON_DATA[index1]["children"]) - 1

            start_range += field_list_count
            end_range += field_list_count

        
       
    fp.close()
    try: 
        json_data=json.dumps(JSON_DATA[1 : ], indent=4)
        json_object = json.loads(json_data)
        with open("csv_to_json.json", "w") as outfile: 
            outfile.write(json_data) 
        print(json_data)   
    except ValueError as e: 
        print ("Is valid json? false")
else:
    print ("file does not exist")
    
