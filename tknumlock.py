# Copyright (C) 2020 Daniel Fitzgerald
from tkinter import *
from tkinter import PhotoImage

NUM_LOCK_ON_PATH = 'images/NumLockOn.png'
NUM_LOCK_OFF_PATH = 'images/NumLockOff.png'


class NumLockTk(Tk):
    def __init__(self, toggleState=True):
        """
        :param toggleState: specifies state of num lock key.
        """
        Tk.__init__(self)

        self._toggle_state = toggleState
        self._hide_calls = 0

        self.overrideredirect(True)
        self.lift()
        self.wm_attributes("-topmost", False)
        self.wm_attributes("-disabled", True)
        self.wm_attributes("-transparentcolor", "#c200c2")  # Fuscia
        self.wm_attributes("-alpha", 0.75)
        self['bg'] = '#c200c2'

        self._img_on = PhotoImage(file=NUM_LOCK_ON_PATH)
        self._img_off = PhotoImage(file=NUM_LOCK_OFF_PATH)
        # Scale images down by a factor of 2.
        self._img_on = self._img_on.subsample(2, 2)
        self._img_off = self._img_off.subsample(2, 2)
        self._label = Label(self, bg="#c200c2", image=self._img_on)
        self._label.pack()

        # Center
        # Screen dimensions
        screen_width, screen_height = self.winfo_screenwidth(), self.winfo_screenheight()
        # Window dimensions
        self.width, self.height = self._img_on.width(), self._img_on.height()
        x, y = (screen_width // 2) - (self.width // 2), (screen_height // 2) - (self.height // 2)
        self.geometry('{}x{}+{}+{}'.format(self.width, self.height, x, y))  # Set position

        self.hide()  # We do not want window to be visible until user toggles num lock.

    def request_hide(self):
        """Prevent odd behaviour when Num Lock is toggled in rapid sequence."""
        self._hide_calls -= 1
        if self._hide_calls < 1:
            self.hide()

    def hide(self):
        """Hide window from user."""
        self.withdraw()

    def show(self, toggle_state):
        """Show window to user.

        :param toggle_state: State of num lock key.
        """
        self._toggle_state = toggle_state
        if toggle_state:
            self._label['image'] = self._img_on
        else:
            self._label['image'] = self._img_off
        self.deiconify()

        self._hide_calls += 1
        self.after(1000, self.request_hide)


'''
References:

https://docs.python.org/3.7/library/tkinter.html
https://stackoverflow.com/questions/19080499/transparent-background-in-a-tkinter-window
https://stackoverflow.com/questions/18394597/is-there-a-way-to-create-transparent-windows-with-tkinter
'''
