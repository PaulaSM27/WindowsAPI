'''
T1135 - Network Share Discovery
'''

import win32net
import win32api

resume_handle = 0 
shares = []
    
while True:
    # server None for local host; level 2 - name, type, permissions, password, number of connections or we can do level 502 - which includes level 2 plus other pertinent information; 
    results, total, resume_handle = win32net.NetShareEnum(None, 2)
    shares.extend(results)
    if resume_handle == 0:
        break

for share in shares:
    print(share)

