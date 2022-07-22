"""Takeoff-hover-land for one CF. Useful to validate hardware config."""

from pycrazyswarm import Crazyswarm


TAKEOFF_DURATION = 2.5 # 2.5
HOVER_DURATION = 3.0 # 5.0


def main():
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    cf = swarm.allcfs.crazyflies[0]

    input()

    cf.setParam('stabilizer.stop', 1)
    timeHelper.sleep(TAKEOFF_DURATION)

if __name__ == "__main__":
    main()
