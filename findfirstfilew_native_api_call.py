from ctypes import *
from ctypes import wintypes as w

#structures
class IO_STATUS_BLOCK(Structure):
    class _Status(Union):
        _fields_ = [('Status', w.ULONG),
                    ('Pointer', w.LPVOID)]
    _anonymous_ = ('u', )
    _fields_ = [('u', _Status),
                ('Information', w.ULONG)]

class OBJECT_ATTRIBUTES(Structure):
    _fields_ = [()]

class FILE_INFORMATION(Structure):
    _fields_ = [()]

class UNICODE_STRING(Structure):
    _fields_ = [()]

NTSTATUS = w.DWORD
nt = windll.ntdll

#NtOpenFile needs to be run first to get a handle on the nt level 

#constants for access mask
#https://learn.microsoft.com/en-us/windows/win32/fileio/file-access-rights-constants
FILE_LIST_DIRECTORY = 0X001
FILE_SHARE_READ = 0x00000001
FILE_READ_DATA = 0x00000001
FILE_SHARE_WRITE = 0x00000002


#dll
NtOpenFile = nt.NtOpenFile
#args
NtOpenFile.argtypes = (POINTER(w.HANDLE), w.ULONG, POINTER(OBJECT_ATTRIBUTES), POINTER(IO_STATUS_BLOCK), w.ULONG, w.ULONG)
#return value 
NtOpenFile.restype = NTSTATUS
#params
FileHandle = ''
DesiredAccess = ''
ObjectAttributes = OBJECT_ATTRIBUTES()
IoStatusBlock = IO_STATUS_BLOCK()
ShareAccess =''
OpenOptions = ''


#dll
NtQueryDirectoryFile = nt.NtQueryDirectoryFile

#args
NtQueryDirectoryFile.argtypes = (w.HANDLE, w.HANDLE, w.LPVOID, w.LPVOID, POINTER(IO_STATUS_BLOCK), w.LPVOID, w.ULONG, w.ULONG, w.BOOL, POINTER(UNICODE_STRING), w.BOOL)
#return value
NtQueryDirectoryFile.restype = NTSTATUS

#params
#file handle returned by NtOpenFile 
FileHandle = ''
Event = ''
ApcRoutine = ''
ApcContext = ''
IoStatusBlock = IO_STATUS_BLOCK()
FileInformation = ''
Length = ''
FileInformationClass = 1
ReturnSingleEntry = ''
FileName = ''
RestartScan = ''


