'''
T1057 - Process Discovery
'''

import ctypes 
from ctypes import wintypes as w 

#kernel
kernel32 = ctypes.windll.kernel32

#TH32CS_SNAPPROCESS - include all processes in the snapshot 
TH32CS_SNAPPROCESS = 0x00000002

#define PROCESSENTRY32W structure
class PROCESSENTRY32W(ctypes.Structure):
    _fields_ = [("dwSize", w.DWORD),
                ("cntUsage", w.DWORD),
                ("th32ProcessID", w.DWORD),
                ("th32DefaultHeapID", ctypes.POINTER(ctypes.c_ulong)),
                ("th32ModuleID", w.DWORD),
                ("cntThreads", w.DWORD),
                ("th32ParentProcessID", w.DWORD),
                ("pcPriClassBase", ctypes.c_long),
                ("dwFlags", w.DWORD),
                ("szExeFile", ctypes.c_wchar * 260)]

#terminate process 
PROCESS_TERMINATE = 0x0001

kill_processes = ["chrome.exe"]

#initilize process entry
process_entry = PROCESSENTRY32W()
process_entry.dwSize = ctypes.sizeof(PROCESSENTRY32W)

#create snapshot, process id=0 for current process
snapshot = kernel32.CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0)
if snapshot == -1: #invalid handle
    raise ctypes.WinError()

#get first process; search handle, pointer to PROCESSENTRY32W; if 0 is returned it failed 
while kernel32.Process32FirstW(snapshot, ctypes.byref(process_entry)) == 0:
    raise ctypes.WinError()

#print first process 
print(f"PID: {process_entry.th32ProcessID}, Name: {process_entry.szExeFile}")

#get all processes 
while kernel32.Process32NextW(snapshot, ctypes.byref(process_entry)) != 0:
    print(f"PID: {process_entry.th32ProcessID}, Name: {process_entry.szExeFile}")
    #if process in kill_processes list, terminate it 
    for process in kill_processes:
        if process_entry.szExeFile == process:
            #first open the handle to the process that needs to be terminated
            open_handle = kernel32.OpenProcess(PROCESS_TERMINATE, False, process_entry.th32ProcessID)
            if open_handle:
                kernel32.TerminateProcess(open_handle, 0)
                print(f"{process_entry.szExeFile} terminated")

kernel32.CloseHandle(snapshot)


