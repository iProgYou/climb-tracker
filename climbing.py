import json
from session import Session
import sys

"""
    - Histogram of flashes per session
    - Average completed grade per session
    - Max grade completed per session
    - average incomplete grade per session
"""

fp = open(sys.argv[1])

data = json.load(fp)
names = data.keys()
inp = input(f"Type a name from the list: [{','.join(names)}] ").lower()
name = None
if inp not in names:
    raise "Name is not in names list"
else: 
    name = inp

name_data = data[name]
sessions_list = sorted([Session(date,climbs) for date,climbs in name_data.items()],key=lambda s: s.date)

if __name__ == "__main__":
    print(sessions_list)