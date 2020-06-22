#!/usr/bin/python

import os
import csv
import json
import logging


logging.basicConfig(filename='csv_to_json.log',format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

CSV_FILE = "data1.csv"
PARENT_MAP, JSON_DATA = {}, []

FIELDS = ["name", "id", "link"]
FIELD_LEN = len(FIELDS)


file_exist = True
try:
    fp = open(CSV_FILE, 'r')
except FileNotFoundError:
    file_exist = False
    logging.error(' File not found. Check the name of file')

if file_exist == True:

    for each_row in csv.reader(fp):
        column_length = len(each_row)
        if column_length < FIELD_LEN:
            continue
        i = FIELD_LEN
        parent_name, parent_id, parent_link = each_row[ : i]
        if not PARENT_MAP.__contains__(parent_id):
            children = []
            JSON_DATA.append({"id": parent_id, "name": parent_name, "link": parent_link, "children": children})
            PARENT_MAP[parent_id] = children
        
        
        while i < column_length:
            
            child_name, child_id, child_link = each_row[i : (i + FIELD_LEN)]
            if  all(each_row[i : (i + FIELD_LEN)]):
                children = []
                if not PARENT_MAP.__contains__(child_id):
                    PARENT_MAP[parent_id].append({"id": child_id, "name": child_name, "link": child_link, "children": children})
                    PARENT_MAP[child_id] = children
                

            parent_id, i = child_id, (i + FIELD_LEN)
        

        



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
    
