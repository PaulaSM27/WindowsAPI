'''
T1082 - System Information Discovery
'''
import win32api
import ctypes 

drives = (drive for drive in win32api.GetLogicalDriveStrings().split("\000") if drive)

# results: 0 - DRIVE_UNKNOWN, 1 - DRIVE_NO_ROOT_DIR, 2 - DRIVE_REMOVABLE, 3 - DRIVE_FIXED, 4 - DRIVE_REMOTE, 5 - DRIVE_CDROM, 6 - DRIVE_RAMDISK 

for drive in drives:
    drive_type = ctypes.windll.kernel32.GetDriveTypeW(drive)
    print(f"Drive: {drive}, Type: {drive_type}")

    

