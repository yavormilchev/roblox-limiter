### Helps block and unblock Roblox on Windows automatically

This repo contains a python script which can be run using a scheduled task
in order to make changes to the Windows hosts file and automatically manage 
Roblox blocking.

Written using Python 3.8.

### Usage
1. Copy `runner.bat.example` into `runner.bat` and update
the python executable path and the `roblox-limiter.py` path.
2. Open `roblox-limiter.py` and modify the block and unblock times as needed.
 Currently set to unblock at 15:00 and block at 21:00. Modify the hosts file location as needed.
3. Open the Windows `Task Scheduler`.
4. `Create Task`.
    - Check `Run with highest priviledges`.
    - In Triggers, create three triggers, one for the unblock time, one for the block time, one on log in.
     For example, unblock at 3pm and block at 9pm.
    - In Actions, add a new action with type Start a program. Browse to locate and select the
     `runner.bat` file created in step 1.
    - In Conditions, make sure the task will run on both battery and plug in power.
    - Click through the rest of the tabs, change settings as needed.
 5. Run the new task to make sure it will update the `hosts` file as expected.
 
 ### Testing
 If you'd like to test the script before creating the scheduled task:
 1. Create a shortcut for `runner.bat`.
 2. Open the shortcut's Preferences.
 3. Click `Advanced`.
 4. Select `Run as administrator`.
 
 Now you can run this shortcut and the script should work as expected.
