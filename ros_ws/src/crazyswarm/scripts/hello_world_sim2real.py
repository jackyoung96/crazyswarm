"""Takeoff-hover-land for one CF. Useful to validate hardware config."""

from pycrazyswarm import Crazyswarm
import numpy as np
import time
import pandas as pd

TAKEOFF_DURATION = 3.0
HOVER_DURATION = 2.0

df = pd.DataFrame()

def main():
    global df
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    cf = swarm.allcfs.crazyflies[0]


    # cf.goTo([0,0,1.5], 0, TAKEOFF_DURATION, True)
    # timeHelper.sleep(TAKEOFF_DURATION)

    cf.takeoff(targetHeight=1.5, duration=TAKEOFF_DURATION)
    timeHelper.sleep(TAKEOFF_DURATION)

    cf.goTo([1.25,0,0], 0, HOVER_DURATION, True)
    timeHelper.sleep(HOVER_DURATION)

    cf.goTo([0,1.25,0], 0, HOVER_DURATION, True)
    timeHelper.sleep(HOVER_DURATION)

    cf.goTo([-1.250,0.0,0], 0, HOVER_DURATION, True)
    timeHelper.sleep(HOVER_DURATION)

    cf.goTo([0,-1.25,0], 0, HOVER_DURATION, True)
    timeHelper.sleep(HOVER_DURATION)

    cf.goTo([0,-1.25,0], 0, HOVER_DURATION, True)
    timeHelper.sleep(HOVER_DURATION)

    cf.goTo([-1.25,0,0], 0, HOVER_DURATION, True)
    timeHelper.sleep(HOVER_DURATION)

    cf.goTo([0,1.25,0], 0, HOVER_DURATION, True)
    timeHelper.sleep(HOVER_DURATION)

    cf.goTo([1.25,0,0], 0, HOVER_DURATION, True)
    timeHelper.sleep(HOVER_DURATION)

    cf.land(targetHeight=0.04, duration=TAKEOFF_DURATION)

    # start = time.time()

    # while time.time()-start < TAKEOFF_DURATION:
    #     pos = cf.position()
    #     df = df.append({
    #         "t": time.time()-start,
    #         "x": pos[0],
    #         "y": pos[1],
    #         "z": pos[2],
    #     }, ignore_index=True)
    #     timeHelper.sleep(0.01)

    # # print(cf.getParam('kalman/resetEstimation'))
    # cf.setParam('kalman/resetEstimation', 1)
    # timeHelper.sleep(0.5)
    # cf.setParam('kalman/resetEstimation', 0)
    # timeHelper.sleep(0.5)

    # # cf.goTo([0.5,0,0], 0, 2.0, True)
    # # timeHelper.sleep(2.0+HOVER_DURATION)
    # # # swarm.input.waitUntilButtonPressed()

    # # cf.goTo([-0.5,0,0], 0, 2.0, True)
    # # timeHelper.sleep(2.0+HOVER_DURATION)
    # # swarm.input.waitUntilButtonPressed()

    # # while X < 1:
    # #     pos = initial_pos + np.array([X, 0, 0])
    # #     cf.cmdPosition(pos)
    # #     timeHelper.sleep(0.1)
    # #     X += 0.05

    # # while X > 0:
    # #     pos = initial_pos + np.array([X, 0, 0])
    # #     cf.cmdPosition(pos)
    # #     timeHelper.sleep(0.1)
    # #     X -= 0.05

    # # cf.land(targetHeight=0.04, duration=2.5)




if __name__ == "__main__":
    try:
        main()
        df.to_csv('~/pos.csv')
    except:
        df.to_csv('~/pos.csv')
