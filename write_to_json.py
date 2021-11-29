import json
import re
from collections import defaultdict

data = {}

def read_data(file):
    file = file.read()
    lines = file.splitlines()
    print(lines)
    file_data = defaultdict(list)
    matcher = re.compile('\d+\/\d+\/\d+')

    current_date = None
    for line in lines:
        if matcher.match(line):
            current_date = line
        else:
            file_data[current_date].append(line)        

    return file_data

with open('peter_climbing_data.txt') as peter, open('zack_climbing_data.txt') as zack:
    data['peter'] = read_data(peter)
    data['zack'] = read_data(zack)


with open('climbing_data.json','w') as outfile:
    json.dump(data,outfile,indent=4)