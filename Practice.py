import time

def download_file_1():
    print("File-1 download starting")
    time.sleep(5) #Make program wait 5sec
    print("File-1 download completed")

def download_file_2():
    print("File-2 download starting")
    time.sleep(3) #Make program wait 3sec
    print("File-2 download completed")

start = time.time() #start time of the program
download_file_1()
download_file_2()
end = time.time() #end time of the program

print("Both file download is complete in:", end - start) #total time it took