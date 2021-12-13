from grade_constants import GRADE_MAP

class Climb():
    """
        A Climb() is an attempt at a route.
    """
    def __init__(self, date, climb_data,ord):
        climb_data = climb_data.lower()
        self.completed = None
        self.flashed = None
        self.is_lap = None
        self.ord = ord
        self.date = date
        self.write_attributes(climb_data)
        self.points = GRADE_MAP[self.grade]

    def write_attributes(self,climb_data):
        if ':' in climb_data:
            # 'i' means incomplete climb 
            # 'f' means flashed climb 
            self.grade,info = climb_data.split(':')
            if 'f' in info:
                self.completed = True
                self.flashed = True
            elif 'i' in info:
                self.completed = False
            
            if 'l' in  info:
                self.is_lap = True
        else:
            self.grade = climb_data
            self.completed = True
            self.flashed = False

