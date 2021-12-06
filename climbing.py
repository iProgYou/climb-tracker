import json
from climb import Climb
from session import Session
import sys
from climb_plot import ClimbPlot

"""
    - Histogram of flashes per session
    - Average completed grade per session
    - Max grade completed per session
    - average incomplete grade per session
    - average completed per session over number of routes attempted
    - and overlay of each climb of each session
"""

fp = open(sys.argv[1])

data = json.load(fp)
names = data.keys()
name = sys.argv[2]
if name not in names:
    raise "Name is not in names list"

name_data = data[name]
sessions_list = sorted([Session(date,climbs,name) for date,climbs in name_data.items()],key=lambda s: s.date)

plotter = ClimbPlot(sessions_list)
plotter.overlay_days()
# if __name__ == "__main__":
#     for s in sessions_list:
#         print(s.recap())