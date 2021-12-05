import sys
from subprocess import call

file_paths = ""

try:
    #run dev
    if sys.argv[1] != "dev":
        raise f"No command for arg {sys.argv[1]}"

    call(["python3","climbing.py","./climbing_data/dummy_climbing_data.json",])
    
except IndexError:
    # run prod
    paths = [
        'peter.txt',
        'zack.txt'
    ]
    call(["python3","write_to_json.py",*paths])
    # if len(sys.argv == )
    call(["python3","climbing.py","./climbing_data/dummy_climbing_data.json",])

    

