# Copyright (C) 2020 Daniel Fitzgerald
# TODO: Pick a project name and update README.md to include project name.

import ctypes
from ctypes import wintypes
from win32con import VK_NUMLOCK
import win32con
import logging
import tkTest

byref = ctypes.byref
user32 = ctypes.windll.user32
MSG_ID_NUM_LOCK = 1


def main():
    # Register Num Lock as hot key.
    # Reference: http://timgolden.me.uk/python/win32_how_do_i/catch_system_wide_hotkeys.html
    logging.log(logging.DEBUG, "Registering num lock as hot key.")
    user32.RegisterHotKey(None, MSG_ID_NUM_LOCK, None, VK_NUMLOCK)

    try:
        msg = wintypes.MSG()
        while user32.GetMessageA(byref(msg), None, 0, 0) != 0:
            if msg.message == win32con.WM_HOTKEY:
                if msg.wParam == MSG_ID_NUM_LOCK:
                    tkTest.show_num_lock_diag(is_num_lock_on())

    finally:
        pass


def is_num_lock_on():
    # https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getkeystate?redirectedfrom=MSDN
    return bool(user32.GetKeyState(VK_NUMLOCK) & 1)  # Least significant bit represents toggle state.


if __name__ == '__main__':
    main()
