import sys, threading, os, time

def intro():
    print("Product[0]   Issue[1]    Company[2]    State[3]    Complaint ID[4]   Zip Code[5]")
    C1 = int(input("Column One->	"))
    C2 = int(input("Column Two->	"))
    SameProduct = int(input("Same Product [0-6](true) or (-1)(false)->	"))
    TargetRate = float(input("Target Rate->	"))
    FILE_COUNT = int(input("Thread count->	"))
    return C1, C2, SameProduct, TargetRate, FILE_COUNT

def fileLen(fileName, FILE_COUNT):
    a = open(fileName, "r")
    FILE_SIZE = int(len(a.readlines()) / (FILE_COUNT))
    a.close()
    return FILE_SIZE

def create_multi_file(file_size):
    with open("trashFile2", "r") as file:
        T = 0
        file_s = 1
        for s in file:
            if (T == 0):
                new_file = open("childFile" + str(file_s), "w")
                file_s += 1
            if (T <= file_size):
                new_file.write(s)
                T += 1
            else:
                new_file.close()
                T = 0

def similarity_rate(str1, str2, C1, C2):
    S1 = " ".join((str1.split(", "))[C1:C2 + 1]).split()
    S2 = " ".join((str2.split(", "))[C1:C2 + 1]).split()
    match_count = 0
    length = len(S1)
    if len(S1) < len(S2):
        length = len(S2)
    for i in S1:
        for j in S2:
            if i.upper() == j.upper():
                S2.remove(j)
                match_count += 1
    return round(100 * (match_count / length), 1)

MatchFile = open("MatchFile.txt", "w")

def File_finder(File_name, line, sub_thread_count, thread_id, sub_thread_id):
    while (1):
        ctrl_line = F[thread_id].readline()
        if (ctrl_line):
            if (SameProduct != -1):
                if (line.split(", ")[SameProduct] != ctrl_line.split(", ")[SameProduct]):
            	    continue
            match = similarity_rate(ctrl_line, line, C1, C2)
            if (match > TargetRate):
                print(ctrl_line[:60] + "->	[" + str(match) + "]	[" + File_name + "]	[" + str(thread_id) + "]	[" + str(sub_thread_id) + "]\n")
                MatchFile.write(ctrl_line[:60] + "->	[" + str(match) + "]	[" + File_name + "]	[" + str(thread_id) + "]	[" + str(sub_thread_id) + "]\n")
        else:
            return 0


def	sub_thread_start(File_name, line, Thread_count, thread_id):
    T = []
    for i in range(Thread_count):
        t = threading.Thread(target = File_finder, args = (File_name, line, int(100 / Thread_count), thread_id, i))
        T.append(t)
        t.start()
    for j in T:
        t.join()

def thread_start(Thread_count):
    line = "Checking savings account, Managing account, NAVY FEDERAL CREDIT UNION, FL, 328XX, 3238275"
    T = []
    for thread_id in range(Thread_count):
        t = threading.Thread(target = sub_thread_start, args=("childFile{}".format(thread_id + 1), line, Thread_count, thread_id))
        T.append(t)
        start_time = time.time()
        START_TIME.append(start_time)
        t.start()
    for t in T:
        end_time = time.time()
        END_TIME.append(end_time)
        t.join()


C1, C2, SameProduct, TargetRate, FILE_COUNT = intro()
START_TIME = []
END_TIME = []

create_multi_file(fileLen("trashFile2", FILE_COUNT))

F = []
for i in range(FILE_COUNT):
    fileee = open("childFile{}".format(i + 1), "r")
    F.append(fileee)

thread_start(FILE_COUNT)


for i in range(len(START_TIME)):
    print(str(i + 1) + ".Thread one process time->	" + str(END_TIME[i] - START_TIME[i]))
