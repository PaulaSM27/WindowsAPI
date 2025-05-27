from ctypes import *
from ctypes import wintypes as w

#structure 
class WIN32_FIND_DATAA(Structure):
    _fields_= [('dwFileAttributes', w.DWORD),
               ('ftCreationTime', w._FILETIME),
               ('ftLastAccessTime', w._FILETIME),
               ('ftLastWriteTime', w._FILETIME),
               ('nFileSizeHigh', w.DWORD),
               ('nFileSizeLow', w.DWORD),
               ('dwReserved0', w.DWORD),
               ('dwReserved1', w.DWORD),
               ('cFileName', w.CHAR * 260),
               ('cAlternateFileName', w.CHAR * 14)
              ]

#dll
kernel32 = windll.kernel32
FindFirstFileW = kernel32.FindFirstFileW

#args
FindFirstFileW.argtypes = (w.LPCWSTR, POINTER(WIN32_FIND_DATAA))

#return value
FindFirstFileW.restype = w.HANDLE

#params
lpFileName = 'C:\\Windows\\*'
lpFindFileData = WIN32_FIND_DATAA()
handle = FindFirstFileW(lpFileName, byref(lpFindFileData))

error = GetLastError()

if error:
    print("Error!")
    print(WinError(error))

#check
print(handle)
print(lpFindFileData.cFileName)
print(lpFindFileData.dwFileAttributes)

