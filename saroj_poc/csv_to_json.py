#!/usr/bin/python

""" convert csv to json  based on column value (parent-child, no of field in parent should be any)"""
import os
import csv
import json
import logging
logging.basicConfig(filename='csv_to_json.log',format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

class Node:
    def __init__(self, file_name, field_name):
        self.file_name = file_name
        self.field_name =field_name
    def csv_to_json(self):
        CSV_FILE = self.file_name
        FIELDS = self.field_name
        PARENT_MAP, JSON_DATA = {}, []
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
                
                i = FIELD_LEN
                # parent_name, parent_id, parent_link = each_row[ : i]
                
                parent_key_list = FIELDS.copy()
                parent_value_list =  each_row[ : i].copy()
                parent_id = parent_value_list[1]
                if not PARENT_MAP.__contains__(parent_id):
                    children = []
                    
                    parent_key_list.append("children")
                    parent_value_list.append(children)
                    parent_dict_to_be_appened = dict( zip(parent_key_list,parent_value_list ))
                    JSON_DATA.append(parent_dict_to_be_appened)
                    # JSON_DATA.append({ FIELDS[0]: parent_id, FIELDS[1]: parent_name, FIELDS[2]: parent_link, "children": children})
                    PARENT_MAP[parent_id] = children
                
                
                while i < column_length:
                    
                    # child_name, child_id, child_link = each_row[i : (i + FIELD_LEN)]
                    if  all(each_row[i : (i + FIELD_LEN)]):
                        children = []
                        
                        child_key_list = FIELDS.copy()
                        child_value_list =  each_row[i : (i + FIELD_LEN)].copy()
                        child_id = child_value_list[1]
                        if not PARENT_MAP.__contains__(child_id):

                            child_key_list.append("children")
                            child_value_list.append(children)
                            child_dict_to_be_appened = dict( zip(child_key_list,child_value_list ))
                            
                            PARENT_MAP[parent_id].append(child_dict_to_be_appened)
                            # PARENT_MAP[parent_id].append({ FIELDS[0]: child_id, FIELDS[1]: child_name, FIELDS[2]: child_link, "children": children})
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
        

p1 = Node("data.csv", ["name", "id", "link"])
p1.csv_to_json()
