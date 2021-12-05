import json
import re
import os
from collections import defaultdict
import sys

data_prefix = "climbing_data"

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

for path in sys.argv[1:]:
    filepath = os.path.join(data_prefix,path)
    name = path.split('.')[0]
    print(name)
    data[name] = read_data(open(filepath))

output_path = os.path.join(data_prefix,'climbing_data.json')

with open(output_path,'w') as outfile:
    json.dump(data,outfile,indent=4)