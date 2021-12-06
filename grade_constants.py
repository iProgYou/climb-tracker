GRADES = [
    "5.8",
    "5.9",
    *[f"5.{i}{a}" for i in range(10,13) for a in "abcd"]
]

GRADE_MAP = {k:v for (k,v) in zip(GRADES,range(0,len(GRADES) * 2,2))}
POINT_MAP = {k:v for (v,k) in zip(GRADES,range(0,len(GRADES) * 2,2))}