# NumLockDialog
This project was created as a solution for keyboards without a
light indicating whether Num&nbsp;Lock is toggled. The following
project written in Python&nbsp;3.7 gives the user a visual 
dialog indicating the state of Num Lock when the Num&nbsp;Lock
key is pressed.

NumLockDialog only supports Windows operating systems.

## How it works ##
NumLockDialog interfaces with [Win32 API](https://docs.microsoft.com/en-us/windows/win32/)
via the Python module [`ctypes`](https://docs.python.org/3/library/ctypes.html)
to watch when a user presses the `Num Lock` key.
