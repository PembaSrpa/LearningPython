# Demonstrates file operations: reading, writing, copying, and working with binary files

f = open('test.txt', 'r')  # Open file for reading
print(f.name)              # Print file name
print(f.mode)              # Print file mode
f.close()                  # Always close file

# Using context manager to handle files (auto-close)
with open('test.txt', 'r') as g:
    size_to_read = 100
    g_contents1 = g.read(size_to_read)  # Read 100 characters
    while len(g_contents1) > 0:
        print(g_contents1, end='')
        g_contents1 = g.read(size_to_read)
    print(g.tell())  # Current file position

    # Other reading methods (commented out)
    # g_contents2 = g.readlines()
    # g_contents3 = g.readline()
    # f.seek(0)  # Go to beginning
    # for line in g:
    #     print(line, end='')

# Writing to a file (overwrites existing content)
with open('test.txt', 'w') as i:
    i.write('Test')
    i.write('Test')  # Overwrites again

# Copying contents from one file to another
with open('test.txt', 'r') as rf:
    with open('test2.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

# Copying binary files (commented out)
# with open('test.jpg', 'rb') as rf:
#     with open('test2.jpg', 'wb') as wf:
#         for line in rf:
#             wf.write(line)

# Copying binary files in chunks (commented out)
# with open('test.jpg', 'rb') as rf:
#     with open('test2.jpg', 'wb') as wf:
#         chunk_size = 4096
#         rf_chunk = rf.read(chunk_size)
#         while len(rf_chunk) > 0:
#             wf.write(rf_chunk)
#             rf_chunk = rf.read(chunk_size)

print(g.closed)  # Check if file is closed
