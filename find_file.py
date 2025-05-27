'''
T1083 - File and Directory Discovery
'''
from ctypes import *
from ctypes import wintypes as w

#set .argstypes and .restype for used functions
dll = WinDLL('kernel32')
dll.FindFirstFileW.argtypes = w.LPCWSTR, w.LPWIN32_FIND_DATAW
dll.FindFirstFileW.restype = w.HANDLE
dll.FindNextFileW.argtypes = w.HANDLE, w.LPWIN32_FIND_DATAW
dll.FindNextFileW.restype = w.BOOL
dll.FindClose.argtypes = w.HANDLE,
dll.FindClose.restype = w.BOOL

dir = "C:\\Windows\\*"

find_data = w.WIN32_FIND_DATAW()
search_handle = dll.FindFirstFileW(dir, byref(find_data))
print(find_data.cFileName)

while dll.FindNextFileW(search_handle, byref(find_data)):
    print(find_data.cFileName)
dll.FindClose(search_handle)