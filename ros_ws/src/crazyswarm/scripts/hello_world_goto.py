"""Takeoff-hover-land for one CF. Useful to validate hardware config."""

from pycrazyswarm import Crazyswarm
import numpy as np
from scipy.spatial.transform import Rotation as R


TAKEOFF_DURATION = 2.0 # 2.5
HOVER_DURATION = 3.0 # 5.0


def setPosition(cf, pos, yaw, duration, rate, timeHelper):
    start_time = timeHelper.time()
    while timeHelper.time() - start_time < duration:
        cf.cmdFullState(pos=pos,
                        vel=np.zeros((3,)),
                        acc=np.zeros((3,)),
                        yaw=yaw,
                        omega=np.zeros((3,)))
        timeHelper.sleepForRate(rate)

def main():
    swarm = Crazyswarm()
    
    cf = swarm.allcfs.crazyflies[0]
    timeHelper = swarm.timeHelper
    
    # cf.setParam('stabilizer/controller', 1)
    # timeHelper.sleep(0.1)
    # cf.goTo([0,0,1.5], 0, TAKEOFF_DURATION, True)
    # timeHelper.sleep(TAKEOFF_DURATION)
    # cf.setParam('ctrlNN/max_thrust', 0.8)
    # cf.setParam('ctrlNN/reset', 1)
    # cf.setParam('stabilizer/controller', 1)
    # timeHelper.sleep(1.0)
    # cf.land(targetHeight=0.02, duration=TAKEOFF_DURATION)
    # timeHelper.sleep(TAKEOFF_DURATION)

    timeHelper.sleep(0.1)
    cf.setParam('stabilizer/controller', 4)
    # cf.setParam('ctrlNN/max_thrust', 0.7)
    timeHelper.sleep(0.5)
    
    pos, quat = cf.position()
    print(cf.prefix)
    r = R.from_quat(quat)
    yaw=r.as_euler('zxy')[0]
    # cf.goTo([0,0,1.0],yaw, TAKEOFF_DURATION, True)
    setPosition(cf, pos=pos+np.array([0,0,1.5]),yaw=yaw, duration=TAKEOFF_DURATION, rate=30, timeHelper=timeHelper)
    # timeHelper.sleep(TAKEOFF_DURATION)
    input()

    # cf.goTo([0,0,-0.28], yaw, TAKEOFF_DURATION, True)
    setPosition(cf, pos=pos,yaw=yaw, duration=TAKEOFF_DURATION, rate=30, timeHelper=timeHelper)
    input()
    cf.cmdStop()
    cf.setParam('stabilizer/controller', 1)
    timeHelper.sleep(1.0)

    # timeHelper.sleep(0.1)
    # cf.goTo([0,0,1.5], 0, TAKEOFF_DURATION, True)
    # timeHelper.sleep(TAKEOFF_DURATION)
    # cf.cmdStop()
    # timeHelper.sleep(0.005)
    # cf.goTo([0,0,1.5], 0, TAKEOFF_DURATION, True)
    # timeHelper.sleep(TAKEOFF_DURATION)
    # cf.land(targetHeight=0.02, duration=TAKEOFF_DURATION)
    # timeHelper.sleep(TAKEOFF_DURATION)


if __name__ == "__main__":
    main()
