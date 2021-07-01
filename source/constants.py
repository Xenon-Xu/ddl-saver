from PyQt5.QtGui import QColor, QTextCharFormat
from functions import *

SHOW_WIN10_NOTIFICATION = True  # if you want to show toast notification on Win10 system, set it to True, else False

IS_WIN10_SYS = is_win10()

IMPORTANCE_PRIORITY = 0
TIME_REMAIN_PRIORITY = 1

QCOLOR_RED = QColor(0xd0, 0x62, 0x62)
QCOLOR_ORANGE = QColor(0xf9, 0xc7, 0x4f)
QCOLOR_LIGHTORANGE = QColor(0xf7, 0xc5, 0x9f)
QCOLOR_BLUEGREEN = QColor(0x43, 0xaa, 0x8b)
QCOLOR_YELLOWGREEN = QColor(0x83, 0xeb, 0x70)
QCOLOR_LIGHTGREEN = QColor(0xb5, 0xdd, 0xa4)
QCOLOR_FAINTBLUE = QColor(0x81, 0xa5, 0xc5)
QCOLOR_GREY = QCOLOR_GRAY = QColor(0xad, 0xb5, 0xbd)
QCOLOR_YELLOW = QColor(0xff, 0xea, 0x70)
QCOLOR_WHITE = QColor(0xff, 0xff, 0xff)

NULL_TEXTCHARFORMAT = QTextCharFormat()

CLOSE_ACTION = 0
MINIMIZE_ACTION = 1

ALL_DAY_TUPLE = (-1, -1, -1, -1)
