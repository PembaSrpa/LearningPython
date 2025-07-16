f = open('test.txt', 'r') # 'w', 'a', 'r+' write, append, read+write

print(f.name)
print(f.mode)

f.close() #must

with open('test.txt', 'r') as g: #automatically closes(context manager)
    # g_contents1 = g.read()
    # print(g_contents1)
    size_to_read = 100
    g_contents1 = g.read(size_to_read) #prints 100 characters
    # print(g_contents1)
    while len(g_contents1) > 0:
        print(g_contents1, end='')
        g_contents1 = g.read(size_to_read)

    print(g.tell())
    # g_contents2 = g.readlines()
    # print(g_contents2)
    # g_contents3 = g.readline()
    # print(g_contents3, end='')
    # f.seek(0) goes to beginning
    # g_contents3 = g.readline()
    # print(g_contents3, end='') # not good, takes too much memory
    # for line in g:
    #     print(line, end='') # not much control

# new to write
with open('test.txt', 'w') as i:
    i.write('Test')
    # i.seek(0) overwrites
    i.write('Test')

with open('test.txt', 'r') as rf:
    with open('test2.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

# with open('test.jpg', 'rb') as rf:
#     with open('test2.jpg', 'wb') as wf:
#         for line in rf:
#             wf.write(line)

# with open('test.jpg', 'rb') as rf:
#     with open('test2.jpg', 'wb') as wf:
#         chunk_size = 4096
#         rf_chunk = rf.read(chunk_size)
#         while len(rf.chunk) > 0:
#             wf.write(rf.chunk)
#             rf_chunk = rf.read(chunk_size)

print(g.closed)
