# Demonstrates various OS module operations

import os
from datetime import datetime
from pprint import pprint

pprint(dir(os))           # List all attributes of os module
pprint(os.getcwd())       # Current working directory
# os.chdir('/path/to/dir') # Change directory
pprint(os.listdir())      # List files and folders in current directory

# Creating directories
# os.mkdir('OS_demo')         # Create single directory
# os.makedirs('OS_demo/Sub_Dir') # Create nested directories

# Removing directories
# os.rmdir('OS_demo')         # Remove single directory
# os.removedirs('OS_demo/Sub_Dir') # Remove nested directories

# Renaming files or directories
# os.rename('OS_demo', 'os_demo')

# File statistics
pprint(os.stat('0cooltxt.py'))           # Get file stats
pprint(os.stat('0cooltxt.py').st_size)   # File size
mod_time = os.stat('0cooltxt.py').st_mtime
print(datetime.fromtimestamp(mod_time))  # Human-readable modification time

# Walking through directories
for dirpath, dirnames, filenames in os.walk('/home/nirashanichang/Desktop/Python Projects/'):
    pprint(('Current Path:', dirpath))
    pprint(('Directories:', dirnames))
    pprint(('Files:', filenames))
    pprint('')

# Environment variables
q = os.environ.get('HOME')
pprint(q)

# Path operations
file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
pprint(file_path)

pprint(os.path.basename('tmp/test.txt'))   # Get file name
pprint(os.path.split('tmp/test.txt'))      # Split path
pprint(os.path.exists('tmp/test.txt'))     # Check existence
pprint(os.path.isdir('tmp/test.txt'))      # Check if directory
pprint(os.path.isfile('tmp/test.txt'))     # Check if file
pprint(os.path.splitext('tmp/test.txt'))   # Split file extension
