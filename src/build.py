import os
from config import POINTSFILE

dirname = os.path.dirname(__file__)
file_path = os.path.join(dirname,"..", "data", POINTSFILE)

def build():
    with open(file_path, "w", encoding = "utf-8") as points_file:
        points_file.write("")

if __name__ == "__main__":
    build()
