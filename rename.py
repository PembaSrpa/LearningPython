# filepath: /home/nirashanichang/Desktop/Python Projects/Learnings/rename.py
# Demonstrates renaming files in a directory

import os

os.chdir('')  # Set working directory (specify path)

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)         # Split file name and extension
    f_title, f_course, f_num = f_name.split('-')# Split name into parts
    f_title = f_title.strip()
    f_course = f_course.strip()
    f_num = f_num.strip()[1:].zfill(2)          # Format number with leading zeros

    new_name = '{}-{}{}'.format(f_num, f_title, f_ext)  # New file name
    os.rename(f, new_name)                      # Rename file
