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

for dirpath, dirnames, filenames in os.walk('/home/nirashanichang/Desktop/Python Projects/'):
    pprint(('Current Path:', dirpath))
    pprint(('Directories:', dirnames))
    pprint(('Files:', filenames))
    pprint('')

q = os.environ.get('HOME')
pprint(q)

file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
pprint(file_path)

pprint(os.path.basename('tmp/test.txt'))
pprint(os.path.split('tmp/test.txt'))
pprint(os.path.exists('tmp/test.txt'))
pprint(os.path.isdir('tmp/test.txt'))
pprint(os.path.isfile('tmp/test.txt'))
pprint(os.path.splitext('tmp/test.txt'))
