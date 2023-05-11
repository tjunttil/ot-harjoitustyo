import functools
from datetime import datetime
import csv
from config import POINTSPATH

open_csv = functools.partial(open, encoding = "utf-8")

class PointRepository:
    """A class for saving and loading to and from a high-score list of points

    Attributes:
        file_path (String): the path of the points file
        points (list): a list of tuples containing the current contents
        of the points file in a (username,points, time) format

    """
    def __init__(self):
        """A constructor for the class
        """
        self.file_path = POINTSPATH
        self.__points = self.__read()

    def __read(self):
        points = []
        try:
            with open_csv(self.file_path, "r", newline = '') as points_file:
                reader = csv.reader(points_file, delimiter = ";")
                for row in reader:
                    points.append((row[0],int(row[1]),row[2]))
        except FileNotFoundError:
            pass
        return points

    def __write(self):
        with open_csv(self.file_path, "w", newline = '') as points_file:
            writer = csv.writer(points_file, delimiter = ";")
            for user, points, time in self.__points:
                writer.writerow([user, points, time])

    def add(self, username, points):
        """A method for adding a point entry, in the form
        username;points;date

        Args:
            username (String): the username of the player
            points (tuple): the points gained
        """
        if not isinstance(username, str) or not isinstance(points, int):
            raise ValueError("There has been an error in point entry input")
        if username != "":
            self.__points.append((username, points, datetime.now().strftime("%d.%m.%Y")))
            self.__points.sort(key = lambda x: x[1], reverse = True)
            self.__write()

    def __filter_dates(self, points_list, days):
        now = datetime.now()
        def strip(entry):
            return datetime.strptime(entry[2], "%d.%m.%Y")
        return list(filter(lambda x: (strip(x) - now).days <= days, points_list))

    def points_list(self, time = "all time"):
        """A method that returns a list of the ten highest
        points-entries, sorted in decreasing order

        Returns:
            [tuple]: a list of tuples of form (username, points, date)
        """
        points = self.__points
        if time == "last week":
            points = self.__filter_dates(points, 7)
        if time == "last month":
            points = self.__filter_dates(points, 30)
        return points[:10]
