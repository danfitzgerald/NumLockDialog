from msilib import type_key
from tkinter import *
from tkinter import PhotoImage

NUM_LOCK_ON_PATH = 'images/NumLockOn.png'
NUM_LOCK_OFF_PATH = 'images/NumLockOff.png'


class NumLockTk(Tk):
    def __init__(self, toggleState=True):
        """run() method must be called to initialize and run mainloop.

        :param toggleState: specifies state of num lock key.
        """

        self._toggle_state = toggleState
        self._close_requested = False

        self.width = 900
        self.height = 640

        self._hide_calls = 0

    # TODO: Move to __init__ method.
    def initialize(self):
        Tk.__init__(self)
        self.overrideredirect(True)
        self.geometry("263x263")  # Image dimensions TODO: un-hardcode
        self.lift()
        self.wm_attributes("-topmost", False)
        self.wm_attributes("-disabled", True)
        self.wm_attributes("-transparentcolor", "#c200c2")  # Fuscia
        self.wm_attributes("-alpha", 0.75)

        self['bg'] = '#c200c2'

        self._img_on = PhotoImage(file=NUM_LOCK_ON_PATH)
        self._img_off = PhotoImage(file=NUM_LOCK_OFF_PATH)

        self._label = Label(self, bg="#c200c2", image=self._img_on)
        self._label.pack()

        # Center
        # Screen dimensions
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Window dimensions
        width = self.winfo_width()
        height = self.winfo_height()

        x = (screen_width//2) - (width//2)
        y = (screen_height//2) - (height//2)

        self.geometry('+{}+{}'.format(x, y))  # Set position

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
        self.after(1500, self.request_hide)


def show_num_lock_diag(tk, toggle_state):
    tk.show(toggle_state)


'''
References:

https://docs.python.org/3.7/library/tkinter.html
https://stackoverflow.com/questions/19080499/transparent-background-in-a-tkinter-window
https://stackoverflow.com/questions/18394597/is-there-a-way-to-create-transparent-windows-with-tkinter
'''
