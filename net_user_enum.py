'''
T1087.001 - Account Discovery: Local Account
'''

import win32net
import ctypes

resume_handle = 0
#results = []

# server None for local machine; level 3 - detailed info about user; filter 0 - normal user, trust data, and machine account; resume_handle 
# there are a lot of fields returned with level 3, so we can save it into results and then filter 
while True:
    users = win32net.NetUseEnum(None, 0, 0, resume_handle)
    print(users)
    #users.extend(results)
    if resume_handle == 0:
        break
error_code = ctypes.windll.kernel32.GetLastError()
print(error_code)

#filter 
#for user in results:
    #print(user['name'], user['passsword'], user['full_name'])

