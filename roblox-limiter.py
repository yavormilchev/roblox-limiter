import time
from datetime import datetime

# Change this to match your hosts file location
hostsPath = "D:\Windows\System32\drivers\etc\hosts"

# Change the block and unblock hours as needed
unblockAt = 15
blockAt = 21

roblox = "\n0.0.0.0 roblox.com\n"
wwwRoblox = "\n0.0.0.0 www.roblox.com\n"

fileModified = False
now = datetime.now()
shouldUnblock = unblockAt <= now.hour < blockAt
shouldBlock = not shouldUnblock
print("Should unblock" if shouldUnblock else "Should block")

with open(hostsPath, 'r') as f:
    data = f.read()
    if shouldBlock and (roblox not in data):
        print('Blocking...')
        data = data + roblox + wwwRoblox
        fileModified = True
    elif shouldBlock :
        print('Already blocked')

    if shouldUnblock and (roblox in data):
        print('Unblocking...')
        data = data.replace(roblox, "")
        data = data.replace(wwwRoblox, "")
        fileModified = True
    elif shouldUnblock :
        print('Already unblocked')

if fileModified :
    with open(hostsPath, 'w') as f:
        f.write(data)
        print('Done writing!')

time.sleep(2)