"""Takeoff-hover-land for one CF. Useful to validate hardware config."""

from pycrazyswarm import Crazyswarm


TAKEOFF_DURATION = 2.5 # 2.5
HOVER_DURATION = 3.0 # 5.0


def main():
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    cf = swarm.allcfs.crazyflies[0]


    # cf.goTo()
    cf.takeoff(targetHeight=1.0, duration=TAKEOFF_DURATION)
    timeHelper.sleep(TAKEOFF_DURATION + HOVER_DURATION)
    cf.land(targetHeight=0.02, duration=TAKEOFF_DURATION)
    timeHelper.sleep(TAKEOFF_DURATION)


if __name__ == "__main__":
    main()
