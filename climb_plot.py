import matplotlib.pyplot as plt
from grade_constants import GRADES,GRADE_MAP,POINT_MAP
from session import Session


class ClimbPlot(object):
    def __init__(self, session_list):
        self.session_list = session_list

    def overlay_days(self):
        # y axis is climb grade
        # x axis is climb number
        fig,ax = plt.subplots()
        flashed = []
        incomplete = []
        for session in self.session_list:
            y = session.climb_points()
            x = list(range(1,len(y) + 1))
            ax.plot(x,y,label=session.date_no_seconds())

            flashed += [(c.ord,c.points) for c in session.climb_objs(climb_type="flashed")]
            incomplete += [(c.ord,c.points) for c in session.climb_objs(climb_type="incomplete")]

        fl_leg = ax.scatter(*zip(*flashed),marker="s",label="Flashed",color="green")
        inc_leg = ax.scatter(*zip(*incomplete),marker="x",label="Incomplete",color="red")

        ytp,ytl = self.grade_range()
        ax.set_yticks(ytp)
        ax.set_yticklabels(ytl)


        plt.title(f"{self.session_list[0].climber_name.capitalize()}'s Climbing Sessions")
        plt.ylabel("Climbing Grades")
        plt.xlabel("Climb Number")

        date_legend = plt.legend(loc="upper left")
        plt.gca().add_artist(date_legend)
        # plt.legend(handles=flashed)
        # plt.legend(handles=inc_legend)
        plt.show()

    def average_over_time(self,climb_type=None):
        x = [s.date_no_seconds() for s in self.session_list]
        y = [s.central_tend(tend_type="mean",climb_type=climb_type) for s in self.session_list]
        ytp,ytl = self.grade_range(min(y),max(y))
        fig,ax = plt.subplots()
        ax.plot(x,y)
        ax.set_yticks(ytp)
        ax.set_yticklabels(ytl)
        # print([[c for c in s.climb_grades(climb_type='flashed')] for s in self.session_list])
        plt.title(f"{self.session_list[0].climber_name.capitalize()}'s Average{'' if not climb_type else ' ' + climb_type.capitalize()} Climb per Session")
        plt.ylabel("Climbing Grades")
        plt.xlabel("Date")

        plt.show()


    def grade_range(self,min_sessions=None,max_sessions=None):
        min_of_sessions = min_sessions or min(map(lambda session: session.min_grade(as_points=True),self.session_list))
        max_of_sessions = max_sessions or max(map(lambda session: session.max_grade(as_points=True),self.session_list))
        labels = [g for g in GRADES if GRADE_MAP[g] >= min_of_sessions - 2 and GRADE_MAP[g] <= max_of_sessions + 2]
        points = [GRADE_MAP[l] for l in labels]
        return (points,labels)



