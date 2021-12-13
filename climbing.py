import json
from climb import Climb
from session import Session
import sys
from climb_plot import ClimbPlot

"""
    - Histogram of flashes per session
    - Max grade completed per session
    - Average incomplete grade per session
    - Average completed per session over number of routes attempted
    
    - Line graph of each climb per session on top of eachother
    - Average completed grade per session
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
plotter.average_over_time(climb_type="flashed")
