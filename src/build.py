import os

dirname = os.path.dirname(__file__)
file_path = os.path.join(dirname,"..", "data", "points.csv")

def build():
    try:
        os.remove(file_path)
    except FileNotFoundError:
        pass
    with open(file_path, "w", encoding = "utf-8"):
        pass
