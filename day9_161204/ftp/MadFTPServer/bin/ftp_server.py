import os
import sys

Base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(Base_dir)

from core import main

if __name__ == "__main__":
    main.ArgvHandler()
