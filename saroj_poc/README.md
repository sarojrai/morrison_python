 -----------------*****************  for csv to json conversion  *****************
install python >3.6
save saroj_poc to your location
go to saroj_poc folder
run poc.py using python3 poc.py      // for poc.csv
Note: run poc.py using python3 csv_to_json.py  // for data.csv

-----------------*****************  for pytest  *****************
mkdir pytest_project
cd pytest_project
 python3 -m venv pytest-env
source pytest-env/bin/activate
(run pip install -r requirements.txt) // if pytest is not installed
pytest


---------------------*****************-------------
sample O/p should be

{
    "name": "POC",
    "children": [
        {
            "name": "Team C",
            "children": [
                {
                    "name": "Processing",
                    "children": [
                        {
                            "name": "US",
                            "children": [
                                {
                                    "name": "67",
                                    "size": "34"
                                }
                            ],
                            "test": {
                                "ID": "67",
                                "ID2": "34"
                            }
                        }
                    ],
                    "test": "Task"
                },
                {
                    "name": "Review",
                    "children": [
                        {
                            "name": "US",
                            "children": [
                                {
                                    "name": "734",
                                    "size": "56"
                                }
                            ],
                            "test": {
                                "ID": "734",
                                "ID2": "56"
                            }
                        }
                    ],
                    "test": "Task"
                },
                {
                    "name": "Support",
                    "children": [
                        {
                            "name": "US",
                            "children": [
                                {
                                    "name": "34",
                                    "size": "43"
                                }
                            ],
                            "test": {
                                "ID": "34",
                                "ID2": "43"
                            }
                        }
                    ],
                    "test": "Task"
                }
            ],
            "test": "TEAM"
        },
        {
            "name": "Team B",
            "children": [
                {
                    "name": "Support",
                    "children": [
                        {
                            "name": "US",
                            "children": [
                                {
                                    "name": "31",
                                    "size": "43"
                                }
                            ],
                            "test": {
                                "ID": "31",
                                "ID2": "43"
                            }
                        }
                    ],
                    "test": "Task"
                },
                {
                    "name": "Support1",
                    "children": [
                        {
                            "name": "Uk",
                            "children": [
                                {
                                    "name": "31",
                                    "size": "43"
                                }
                            ],
                            "test": {
                                "ID": "31",
                                "ID2": "43"
                            }
                        }
                    ],
                    "test": "Task"
                }
            ],
            "test": "TEAM"
        }
    ]
}

