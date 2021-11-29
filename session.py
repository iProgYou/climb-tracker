from climb import Climb

class Session():

    GRADES = [
        "5.8",
        "5.9",
        "5.10a", 
        "5.10b", 
        "5.10c", 
        "5.10d",
        "5.11a", 
        "5.11b", 
        "5.11c", 
        "5.11d",
        "5.12a", 
        "5.12b", 
        "5.12c", 
        "5.12d",
    ]
    GRADE_MAP = {k:v for (k,v) in zip(GRADES,range(0,len(GRADES) * 2,2))}
    POINT_MAP = {k:v for (v,k) in zip(GRADES,range(0,len(GRADES) * 2,2))}

    def __init__(self, date,climbs):
        self.date = date
        self.climbs = [Climb(self.date,climb) for climb in climbs]


    def average_grade(self,climb_type=None):

        climbs = self.climb_points(climb_type)

        if not climbs:
            return None

        total_points = round(sum(climbs) / len(climbs))

        return self.get_grade_from_total_points(total_points)

        

    def get_grade_from_total_points(self,total_points):
        if total_points in self.POINT_MAP:
            return self.POINT_MAP[total_points]
        else:
            # odd number point grade
            lower_grade = self.POINT_MAP[total_points - 1]
            if lower_grade.endswith('d'):
                # 5.11d/12a
                lower_grade_int = int(lower_grade[2:-1])
                return '5.' + str(lower_grade_int) + 'd' + str(lower_grade_int + 1) + 'a'
            else:
                # 5.11a/b

                higher_grade = self.POINT_MAP[total_points + 1]
                return lower_grade + '/' + higher_grade[-1]

    def climb_points(self,climb_type):
        if not climb_type:
            # max of all climbs
            return [self.GRADE_MAP[c.grade] for c in self.climbs]
        elif climb_type == "completed":
            return [self.GRADE_MAP[c.grade] for c in self.climbs if c.completed]
        elif climb_type == "flashed":
            return [self.GRADE_MAP[c.grade] for c in self.climbs if c.flashed]
        elif climb_type == "incomplete":
            return [self.GRADE_MAP[c.grade] for c in self.climbs if not c.completed]
        else:
            raise "Invalid type input"

    def max_grade(self,climb_type=None):
        climbs = self.climb_points(climb_type)
        max_climb = max(climbs)
        return self.POINT_MAP[max_climb]

    def min_grade(self,climb_type=None):
        climbs = self.climb_points(climb_type)
        min_climb = min(climbs)
        return self.POINT_MAP[min_climb]

    def num_climbs(self,climb_type=None):
        return len(self.climb_points(climb_type))

    def climb_ratio(self,numerator_climb_type,denom_climb_type):
        return self.num_climbs(climb_type=numerator_climb_type) / self.num_climbs(climb_type=denom_climb_type)


if __name__ == "__main__":
    s = Session("11/28/2021",[
        "5.10a:F",
        "5.10a",
        "5.10c:f",
        "5.10d:-",
        "5.10c",
        "5.10c:f",
        "5.10d"
    ])
    types = [None,"completed","incomplete","flashed"]

    for t in types:
        if not t:
            print("ALL CLIMBS")
        else:
            print(t)
        print("Average: ",s.average_grade(climb_type=t))
        print("Max",s.max_grade(climb_type=t))
        print("_________________")



