GRADES = [
    "5.8",
    "5.9",
    *[f"5.{i}{a}" for i in range(10,13) for a in "abcd"]
]
# returns a point value after keying in a grade
GRADE_MAP = {k:v for (k,v) in zip(GRADES,range(0,len(GRADES) * 2,2))}

# returns a grade value after keying in a point
POINT_MAP = {k:v for (v,k) in zip(GRADES,range(0,len(GRADES) * 2,2))}