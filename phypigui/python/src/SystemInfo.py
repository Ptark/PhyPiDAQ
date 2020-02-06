import sys
import math

from PyQt5 import QtWidgets


class SystemInfo:
    FL_MIN: float = sys.float_info.min
    FL_MAX: float = sys.float_info.max
    FL_MAX_DECIMALS: int = math.fabs(sys.float_info.min_10_exp)

    SCREEN_WIDTH: int
    SCREEN_HEIGHT: int

    RESOURCES: str = 'phypigui/python/resources/'

    @staticmethod
    def init():
        SystemInfo.SCREEN_WIDTH = QtWidgets.QDesktopWidget().screenGeometry(-1).width()
        SystemInfo.SCREEN_HEIGHT = QtWidgets.QDesktopWidget().screenGeometry(-1).height()

    @staticmethod
    def h():
        print(SystemInfo.SCREEN_WIDTH)
        print(SystemInfo.SCREEN_HEIGHT)
