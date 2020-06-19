#!/usr/bin/python

import os
import csv
import json

CSV_FILE = "data.csv"
INDEX_MAP, JSON_DATA = {}, []


fp = open(CSV_FILE, 'r')
for each_row in csv.reader(fp):
    
    if len(each_row) < 9:
        continue
    name1, id1, url1 = each_row[ : 3]
    index1 = INDEX_MAP.get(id1, -1)
    
    if index1 == -1:
        JSON_DATA.append({"id": id1, "link": url1, "name": name1, "children": []})
        index1 = INDEX_MAP[id1] = len(JSON_DATA) - 1
    name2, id2, url2 = each_row[3 : 6]
    index2 = INDEX_MAP.get(id2, -1)
    if index2 == -1:
        JSON_DATA[index1]["children"].append({"id": id2, "link": url2, "name": name2, "children": []})
        index2 = INDEX_MAP[id2] = len(JSON_DATA[index1]["children"]) - 1
    name3, id3, url3 = each_row[6 : 9]
    JSON_DATA[index1]["children"][index2]["children"].append({"id": id3, "link": url3, "name": name3, "children": []})
fp.close()
try: 
    json_data=json.dumps(JSON_DATA[1 : ], indent=4)
    json_object = json.loads(json_data)
    # print(json_data)   
except ValueError as e: 
    print ("Is valid json? false")
# print(json.dumps(JSON_DATA[1 : ], indent=4))
# print(JSON_DATA[1 : ])

