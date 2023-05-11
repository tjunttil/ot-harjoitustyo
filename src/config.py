import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path = os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

POINTSFILE = os.getenv("POINTSFILE") or "points.csv"
POINTSPATH = os.path.join(dirname, "..", "data", POINTSFILE)
