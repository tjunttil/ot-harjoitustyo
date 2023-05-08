import os

dirname = os.path.dirname(__file__)
file_path = os.path.join(dirname,"..", "data", "points.csv")

def build():
    with open(file_path, "w", encoding = "utf-8") as points_file:
        points_file.write("")
    print(f"created points file in {file_path}")

if __name__ == "__main__":
    build()
