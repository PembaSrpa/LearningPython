try:
    f = open('testfile.txt')
    if f.name == 'currupt.txt':
        raise Exception #custom exception
except FileNotFoundError:
    print('File Doesnt exist')
except Exception as e:
    print("An error occurred:", e)
else: #runs if theres no exception
    print("File opened successfully")
    # You can add code here to work with the file
    f.close()
finally: #runs anyway
    print("Execution completed, whether an error occurred or not.")
    if 'f' in locals() and not f.closed:
        f.close()
        print("File closed.")