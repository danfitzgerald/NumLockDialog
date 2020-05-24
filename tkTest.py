from tkinter import *
from threading import Thread


class NumLockTk(Tk):
    def __init__(self, toggleState, parent=None):
        '''
        run() method must be called to initialize and run mainloop.

        :param toggleState: specifies state of num lock key.
        :param parent: parent window [None] if parent window does not exist
        '''

        self._parent = parent
        self._toggleState = toggleState
        self._close_requested = False

        self.width = 900
        self.height = 640

    def _initialize(self):
        Tk.__init__(self, self._parent)
        self.overrideredirect(True)
        self.geometry("+250+250")
        self.lift()
        self.wm_attributes("-topmost", True)
        self.wm_attributes("-disabled", True)
        self.wm_attributes("-transparentcolor", "white")

        state = "off"
        if self._toggleState:
            state = "on"
        self.label = Label(self, text="Num Lock %s" % state, bg="white")
        self.label.pack()

        self.after(1000, self.destroy)

    def run(self):
        '''
        Run method to be used as target for thread.

        :return: None
        '''
        self._initialize()
        self.mainloop()

    def destroy(self):
        super().destroy()


def show_num_lock_diag(toggle_state):
    tk = NumLockTk(toggle_state)
    tk_thread = Thread(target=tk.run)
    tk_thread.start()

'''
References:

https://docs.python.org/3.7/library/tkinter.html
https://stackoverflow.com/questions/19080499/transparent-background-in-a-tkinter-window
https://stackoverflow.com/questions/18394597/is-there-a-way-to-create-transparent-windows-with-tkinter
'''
