import csv
import json

class Node(object):
    def __init__(self, name, size=None, extra=None):
        self.name = name
        self.children = []
        self.size = size
        self.extra = extra

    def child(self, cname, size=None, extra=None):
        child_found = [c for c in self.children if c.name == cname]
        if not child_found:
            _child = Node(cname, size, extra)
            self.children.append(_child)
        else:
            _child = child_found[0]
        return _child

    def as_dict(self):
        res = {'name': self.name}
        if self.size is None:
            res['children'] = [c.as_dict() for c in self.children]
        else:
            res['size'] = self.size

        if self.extra:
            res.update(self.extra)

        return res

root = Node('POC')

with open('poc.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)

    for row in reader:
        team, task, country, id, id2 = row
        root.child(team, extra={'test' : 'TEAM'}) \
            .child(task, extra={'test' : 'Task'}) \
            .child(country, extra={'test' : {'ID': id, 'ID2': id2}}) \
            .child(id, size=id2)
try: 
    json_data=json.dumps(root.as_dict(), indent=4)
    json_object = json.loads(json_data)
    print(json_data)   
except ValueError as e: 
    print ("Is valid json? false") 