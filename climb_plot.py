import matplotlib.pyplot as plt
from grade_constants import GRADES,GRADE_MAP,POINT_MAP


class ClimbPlot(object):
    def __init__(self, session_list):
        self.session_list = session_list

    def overlay_days(self):
        # y axis is climb grade
        # x axis is climb number
        
        fig,ax = plt.subplots()
        for session in self.session_list:
            y = session.climb_points()
            x = list(range(1,len(y) + 1))
            ax.plot(x,y,label=session.date_no_seconds())

        ytp,ytl = self.grade_range()
        ax.set_yticks(ytp)
        ax.set_yticklabels(ytl)

        plt.title(f"{self.session_list[0].climber_name.capitalize()}'s Climbing Sessions")
        plt.ylabel("Climbing Grades")
        plt.xlabel("Climb Number")

        plt.legend()
        plt.show()

    def grade_range(self):
        min_of_sessions = min(map(lambda session: session.min_grade(),self.session_list))
        max_of_sessions = min(map(lambda session: session.max_grade(),self.session_list))
        labels = [g for g in GRADES if g >= min_of_sessions and g <= max_of_sessions]
        points = [GRADE_MAP[l] for l in labels]
        return (points,labels)



