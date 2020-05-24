# NumLockWatchdogUI
This project was created as a solution for users whose 
keyboards do not have a light indicating whether Num&nbsp;Lock,
Caps&nbsp;Lock or Scroll&nbsp;Lock etc. are toggled. The following
project written in Python&nbsp;3.7 gives the user a visual
dialogue displaying when the state of the above keys are toggled.

Currently NumLockWatchdogUI only supports Windows operating systems.

## How it works ##
NumLockWatchdogUI uses the [Win32 API](https://docs.microsoft.com/en-us/windows/win32/)
via the python module ctypes to watch when a user presses the
`Num Lock` key.
