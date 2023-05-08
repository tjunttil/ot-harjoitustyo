import os
import functools
from datetime import datetime
import csv

open_csv = functools.partial(open, encoding = "utf-8")

class PointRepository:
    """A class for handling saving and loading points

    Attributes:
        file_path (String): the path of the points file
        points (dict): a dictionary containing the current contents
        of the points file in a username:(points, time) format

    """
    def __init__(self):
        """A constructor for the class
        """
        dirname = os.path.dirname(__file__)
        self.file_path = os.path.join(dirname, "..", "..", "data/points.csv")
        self.__points = self.__read()

    def __read(self):
        points = {}
        with open_csv(self.file_path, "r", newline = '') as points_file:
            reader = csv.reader(points_file, delimiter = ";")
            for row in reader:
                points[row[0]] = (row[1],row[2])
        return points

    def __write(self):
        with open_csv(self.file_path, "w", newline = '') as points_file:
            writer = csv.writer(points_file, delimiter = ";")
            for user, entry in self.__points.items():
                writer.writerow([user, entry[0], entry[1]])

    def add(self, username, points):
        """A method for adding a point entry, in the form
        'username;points;date

        Args:
            username (String): the username of the player
            points (tuple): the points gained
        """
        self.__points[username] = (points, datetime.now().strftime("%d.%m.%Y"))
        self.__write()

    def points_list(self):
        points = list(self.__points.items())
        return sorted(points, key = lambda x: x[1], reverse = True)
