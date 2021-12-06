import sys
from subprocess import call

file_paths = ""

try:
    if sys.argv[1] != "dev":
        #run prod
        paths = [
            'peter.txt',
            'zack.txt'
        ]
        call(["python3","write_to_json.py",*paths])
        call(["python3","climbing.py","./climbing_data/climbing_data.json",sys.argv[1].lower()])
    elif sys.argv[1] == "dev":
        call(["python3","climbing.py","./climbing_data/dummy_climbing_data.json",sys.argv[2].lower()])
    else:
        raise f"No command for arg {sys.argv[1]}"

except IndexError:
    raise "No valid args passed"