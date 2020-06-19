import json

def test_validjson():
    
    json_data='{"name": "POC", "children": [{"name": "Team C", "children": [{"name": "Processing", "children": [{"name": "US", "children": [{"name": "67", "size": "34"}], "test": {"ID": "67", "ID2": "34"}}], "test": "Task"}, {"name": "Review", "children": [{"name": "US", "children": [{"name": "734", "size": "56"}], "test": {"ID": "734", "ID2": "56"}}], "test": "Task"}, {"name": "Support", "children": [{"name": "US", "children": [{"name": "34", "size": "43"}], "test": {"ID": "34", "ID2": "43"}}], "test": "Task"}], "test": "TEAM"}, {"name": "Team B", "children": [{"name": "Support", "children": [{"name": "US", "children": [{"name": "31", "size": "43"}], "test": {"ID": "31", "ID2": "43"}}], "test": "Task"}, {"name": "Support1", "children": [{"name": "Uk", "children": [{"name": "31", "size": "43"}], "test": {"ID": "31", "ID2": "43"}}], "test": "Task"}], "test": "TEAM"}]}'


    assert json.dumps(json_data)
    
def test_Invalidjson():
   
    json_data1='"name": "POC", "children": {"name": "Team C", "children": [{"name": "Processing", "children": [{"name": "US", "children": [{"name": "67", "size": "34"}], "test": {"ID": "67", "ID2": "34"}}], "test": "Task"}, {"name": "Review", "children": [{"name": "US", "children": [{"name": "734", "size": "56"}], "test": {"ID": "734", "ID2": "56"}}], "test": "Task"}, {"name": "Support", "children": [{"name": "US", "children": [{"name": "34", "size": "43"}], "test": {"ID": "34", "ID2": "43"}}], "test": "Task"}], "test": "TEAM"}, {"name": "Team B", "children": [{"name": "Support", "children": [{"name": "US", "children": [{"name": "31", "size": "43"}], "test": {"ID": "31", "ID2": "43"}}], "test": "Task"}, {"name": "Support1", "children": [{"name": "Uk", "children": [{"name": "31", "size": "43"}], "test": {"ID": "31", "ID2": "43"}}], "test": "Task"}], "test": "TEAM"}]}'
    jsonvalid = True
    try: 
        json_data=json.dumps(json_data1, indent=4)
        json_object = json.loads(json_data)
        
    except ValueError as e: 
        jsonvalid = False

    assert jsonvalid

def check_key():
    # input_dict="{'name': 'POC', 'children': [{'name': 'Team C', 'children': [{'name': 'Processing', 'children': [{'name': 'US', 'children': [{'name': '67', 'size': '34'}], 'test': {'ID': '67', 'ID2': '34'}}], 'test': 'Task'}, {'name': 'Review', 'children': [{'name': 'US', 'children': [{'name': '734', 'size': '56'}], 'test': {'ID': '734', 'ID2': '56'}}], 'test': 'Task'}, {'name': 'Support', 'children': [{'name': 'US', 'children': [{'name': '34', 'size': '43'}], 'test': {'ID': '34', 'ID2': '43'}}], 'test': 'Task'}], 'test': 'TEAM'}, {'name': 'Team B', 'children': [{'name': 'Support', 'children': [{'name': 'US', 'children': [{'name': '31', 'size': '43'}], 'test': {'ID': '31', 'ID2': '43'}}], 'test': 'Task'}, {'name': 'Support1', 'children': [{'name': 'Uk', 'children': [{'name': '31', 'size': '43'}], 'test': {'ID': '31', 'ID2': '43'}}], 'test': 'Task'}], 'test': 'TEAM'}]}"
    json_data='{"name": "POC", "children": [{"name": "Team C", "children": [{"name": "Processing", "children": [{"name": "US", "children": [{"name": "67", "size": "34"}], "test": {"ID": "67", "ID2": "34"}}], "test": "Task"}, {"name": "Review", "children": [{"name": "US", "children": [{"name": "734", "size": "56"}], "test": {"ID": "734", "ID2": "56"}}], "test": "Task"}, {"name": "Support", "children": [{"name": "US", "children": [{"name": "34", "size": "43"}], "test": {"ID": "34", "ID2": "43"}}], "test": "Task"}], "test": "TEAM"}, {"name": "Team B", "children": [{"name": "Support", "children": [{"name": "US", "children": [{"name": "31", "size": "43"}], "test": {"ID": "31", "ID2": "43"}}], "test": "Task"}, {"name": "Support1", "children": [{"name": "Uk", "children": [{"name": "31", "size": "43"}], "test": {"ID": "31", "ID2": "43"}}], "test": "Task"}], "test": "TEAM"}]}'

    assert 'name' in json_data
    assert 'name' in json_data['children']


