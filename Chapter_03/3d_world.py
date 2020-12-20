# coding = <utf-8>

import sys
import os 
import os.path as osp 
import logging 
from math import sqrt, log
import argparse
from pathlib import Path
sys.path.insert(0, osp.abspath(__file__))


import coloredlogs
import numpy as np 
from scipy import stats
import matplotlib.pyplot as plt


coloredlogs.install(level="INFO", fmt="%(asctime)s %(filename)s %(levelname)s %(message)s")

savePath = osp.join(os.getcwd(), "outputs")
SAVE_DIR = Path(savePath)
SAVE_DIR.mkdir(parents=True, exist_ok=True)



def main():
    print("he")



if __name__ == "__main__":

    main()