import json
from session import Session
import sys

"""
    - Histogram of flashes per session
    - Average completed grade per session
    - Max grade completed per session
    - average incomplete grade per session
    - average completed per session over number of routes attempted
"""

fp = open(sys.argv[1])

data = json.load(fp)
names = data.keys()
name = sys.argv[2]
if name not in names:
    raise "Name is not in names list"

name_data = data[name]
sessions_list = sorted([Session(date,climbs) for date,climbs in name_data.items()],key=lambda s: s.date)

if __name__ == "__main__":
    for s in sessions_list:
        print(s.recap())
        print("_____________________")