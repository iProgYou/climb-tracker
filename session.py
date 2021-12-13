from climb import Climb
from statistics import mean,median,mode
from datetime import datetime
from grade_constants import GRADES,GRADE_MAP,POINT_MAP

class Session():

    def __init__(self, date,climbs,climber_name,include_laps=False):
        self.date = datetime.strptime(date,"%m/%d/%y")
        self.climber_name = climber_name

        # climbs are in the array based on the order they were climbed
        self.climbs = [Climb(self.date,climbs[i],i + 1) for i in range(len(climbs))]
        if not include_laps:
            self.climbs = list(filter(lambda x: not x.is_lap,self.climbs))


    def date_no_seconds(self):
        return self.date.strftime("%m/%d/%y")

    def central_tend(self,tend_type,climb_type=None,as_grade=False):
        tend_type = tend_type.lower()

        climbs = self.climb_points(climb_type)
        if len(climbs) == 0:
            return None

        if tend_type == "mean":
            res = mean(climbs)
        elif tend_type == "mode":
            try:
                res = mode(climbs)
            except:
                return None
        elif tend_type == "median":
            res = median(climbs)
        else:
            raise "Invalid tend type passed"

        if as_grade:
            return self.get_grade_from_points(round(res))
        else:
            return res
        

    def get_grade_from_points(self,total_points):
        if total_points in POINT_MAP:
            return POINT_MAP[total_points]
        else:
            # odd number point grade
            lower_grade = POINT_MAP[total_points - 1]
            if lower_grade.endswith('d'):
                # 5.11d/12a
                lower_grade_int = int(lower_grade[2:-1])
                return '5.' + str(lower_grade_int) + 'd'  + "/" + str(lower_grade_int + 1) + 'a'
            else:
                # 5.11a/b

                higher_grade = POINT_MAP[total_points + 1]
                return lower_grade + '/' + higher_grade[-1]


    def climb_points(self,climb_type=None):
        return [GRADE_MAP[c] for c in self.climb_grades(climb_type)]

    def climb_objs(self,climb_type=None):
        if not climb_type:
            return self.climbs
        elif climb_type == "completed":
            return [c for c in self.climbs if c.completed]
        elif climb_type == "flashed":
            return [c for c in self.climbs if c.flashed]
        elif climb_type == "incomplete":
            return [c for c in self.climbs if not c.completed]
        else:
            raise "Invalid climb type input"

    def climb_grades(self,climb_type=None):
        return [c.grade for c in self.climb_objs(climb_type)] 


    def max_grade(self,climb_type=None,as_points=False):
        climbs = self.climb_points(climb_type)
        if len(climbs) == 0:
            return None
        max_climb = max(climbs)
        if as_points:
            return max_climb
        else:
            return POINT_MAP[max_climb]


    def min_grade(self,climb_type=None,as_points=False):
        climbs = self.climb_points(climb_type)
        if len(climbs) == 0:
            return None
        min_climb = min(climbs)
        if as_points:
            return min_climb
        else:
            return POINT_MAP[min_climb]


    def num_climbs(self,climb_type=None,grade_number=None,):
        # grade number would be the 10 in "5.10a" etc
        if not grade_number:
            return len(self.climb_grades(climb_type))
        
        if grade_number not in range(8,13):
            raise "Invalid grade error passed"

        return len([c for c in self.climb_grades(climb_type) if str(grade_number) in c])


    def climb_ratio(self,numerator_climb_type=None,denom_climb_type=None):
        return self.num_climbs(climb_type=numerator_climb_type) / self.num_climbs(climb_type=denom_climb_type)


    def __repr__(self):
        return f"Session date: {self.date}"


    def recap(self):
        for i in range(8,13):
            print(f"Num 5.{i}'s climbed: {self.num_climbs(grade_number=i)}")

        print("____________________________________")
        types = [None,"completed","flashed","incomplete"]
        tend_types = ["mean","median","mode"]
        for t in types:
            if not t:
                print(f"ALL CLIMBS : {self.num_climbs(t)}")
            else:
                print(t.capitalize(),f": {self.num_climbs(t)}")

            for tend in tend_types:
                print(f"{tend}: ",self.central_tend(tend,climb_type=t))
                # print(f"{tend} as points: ",self.central_tend(tend,climb_type=t,as_grade=False))
            print("Max",self.max_grade(climb_type=t))
            print("Min",self.min_grade(climb_type=t))
            print("_________________")



if __name__ == "__main__":
    s = Session("11/28/21",[
        "5.10a:F",
        "5.11a",
        "5.10c:f",
        "5.10d:-",
        "5.10c",
        "5.10c:f",
        "5.12d"
    ],"Alf")
    print(s.date)
    print(s.central_tend("mean"))
    # print(s.recap())
