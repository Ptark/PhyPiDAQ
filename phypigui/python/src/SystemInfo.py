"""import sys
import math
from typing import final
from PyQt5 import QtWidgets


class SystemInfo:
    FL_MIN: final(float) = sys.float_info.min
    FL_MAX: final(float) = sys.float_info.max
    FL_MAX_DECIMALS: final(int) = math.fabs(sys.float_info.min_10_exp)

    SCREEN_WIDTH: final(int) = QtWidgets.QDesktopWidget().screenGeometry(-1).width()
    SCREEN_HEIGHT: final(int) = QtWidgets.QDesktopWidget().screenGeometry(-1).height()

    @staticmethod
    def h():
        print(SystemInfo.SCREEN_WIDTH)
        print(SystemInfo.SCREEN_HEIGHT)"""
