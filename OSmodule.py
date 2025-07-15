import os
from datetime import datetime
from pprint import pprint

pprint(dir(os))
pprint(os.getcwd())
# os.chdir('/home/nirashanichang/Desktop/Python Projects/') Change Directory
pprint(os.listdir()) #shows files and folders inside the directory

#to create new folder
# os.makedir('OS_demo')
# os.makedir('OS_demo/Sub_Dir') error
# os.makedirs('OS_demo') #few levels deep
# os.makedirs('OS_demo/Sub_Dir')

#to remove
# os.rmdir('OS_demo')
# os.removedirs('OS_demo/Sub_Dir')

#to rename
# os.rename('OS_demo', 'os_demo')

pprint(os.stat('0cooltxt.py'))
pprint(os.stat('0cooltxt.py').st_size)
mod_time = os.stat('0cooltxt.py').st_mtime
print(datetime.fromtimestamp(mod_time)) #human readable time
