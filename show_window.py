'''
T1564.003 - Hide Artifacts: Hidden Window
'''

import ctypes 

user32 = ctypes.windll.user32

#first find window to get a handle; params: class name null - finds any window whose title matches window name param, window name
window_handle = user32.FindWindowW(None, "Command Prompt")
#print(window_handle)

#prams: handle, 0 - hides the window
#returns nonzero if window was previously visible, zero if it was hidden
hide_window = user32.ShowWindow(window_handle, 0)
#print(hide_window)
user32.CloseHandle(window_handle)