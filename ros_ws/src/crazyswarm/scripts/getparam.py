"""Takeoff-hover-land for one CF. Useful to validate hardware config."""

from pycrazyswarm import Crazyswarm
import numpy as np
import time
import pandas as pd

TAKEOFF_DURATION = 1.5
HOVER_DURATION = 1.0

df = pd.DataFrame()

def main():
    global df
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    cf = swarm.allcfs.crazyflies[0]

    while True:
        a = input()
        if a == 'exit':
            break
        print(cf.getParam(a))


if __name__ == "__main__":
    main()