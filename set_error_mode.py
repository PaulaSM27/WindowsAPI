'''
T1562.006 - Impair Defenses: Indicator Blocking
'''

import win32api

last_error = win32api.GetLastError()

error_mode = win32api.SetErrorMode(0)
if last_error == 0:
    print(f"Success! The Error Mode is: {error_mode}")
elif last_error == 126:
    print("Error Mode Not Found!")
else:
    print(f"Error Mode Failed! Last error code: {last_error}")