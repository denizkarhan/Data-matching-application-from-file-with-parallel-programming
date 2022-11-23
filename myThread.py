import sys, threading, os, time

START_TIME = []
END_TIME = []
DATA = []
F = []

NAME = ["Product", "Issue", "Company", "State", "Zip Code", "Complaint ID"]
total_time = 0

############     Partition the main file into as many files as there are threads     ############
def create_multi_file(file_size):
    file = open("trashFile2", "r", encoding="utf-8")
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
    file.close()

############     Match rate in a certain range. (0 not include)     ############
def similarity_rate(str1, str2, C3, C4):
	S1 = " ".join((str1.split(", "))[C3:C4 + 1]).split()
	S2 = " ".join((str2.split(", "))[C3:C4 + 1]).split()
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

def InterFace_data(ctrl_line, C1, C2, match):
    S = ctrl_line.split(", ")
    D = {}
    for i in range(C1, C2+1):
        D.update({NAME[i]:S[i]})
    D.update({"Match":"%"+str(match)})
    return (D)

############     Print matching data to file     ############
def File_finder(File_name, line, sub_thread_count, thread_id, C1, C2, C3, C4, SameProduct, TargetRate, complaint_id, FILE_COUNT):
    if ((complaint_id not in line) and complaint_id != "-1"):
        return 1
    while (1):
        try:
            ctrl_line = F[thread_id].readline()
        except:
            return 0
        if (ctrl_line):
            flag = 1
            if (SameProduct != -1):
                a = similarity_rate(line, ctrl_line, SameProduct, SameProduct)
                if (a <= 99):
                    flag = 0
            if (flag == 1):
                match = similarity_rate(ctrl_line, line, C3, C4)
                if (match >= TargetRate):
                    print(", ".join(ctrl_line.split(", ")[C1:C2+1]).strip(" \n\r\t"))
                    DATA.append(InterFace_data(ctrl_line, C1, C2, match))
        else:
            return 0

############     Create (100 / thread_count) sub-threds and send them to match check     ############
def	sub_thread_start(File_name, line, thread_id, C1, C2, C3, C4, SameProduct, TargetRate, complaint_id, FILE_COUNT):
    T = []
    for i in range(5):
        t = threading.Thread(target = File_finder, args = (File_name, line, int(1), thread_id, C1, C2, C3, C4, SameProduct, TargetRate, complaint_id, FILE_COUNT))
        T.append(t)
        t.start()
    for j in T:
        t.join()

############     Create desired number of threads and send to sub-thread generation (100 / number of threads)     ############
def thread_start(C1, C2, C3, C4, SameProduct, TargetRate, complaint_id, FILE_COUNT):
    line = "Checking savings account, Managing account, NAVY FEDERAL CREDIT UNION, FL, 328XX, 3198084"
    s = 0
    for i in range(FILE_COUNT):
        fileee = open("childFile{}".format(i + 1), "r")
        F.append(fileee)
    T = []
    for thread_id in range(FILE_COUNT):
        t = threading.Thread(target = sub_thread_start, args=("childFile{}".format(thread_id + 1), line, thread_id, C1, C2, C3, C4, SameProduct, TargetRate, complaint_id, FILE_COUNT))
        T.append(t)
        start_time = time.time()
        START_TIME.append(start_time)
        t.start()
    for t in T:
        end_time = time.time()
        END_TIME.append(end_time)
        t.join()
    for f in F:
        F[s].close()
        s += 1
    F.clear()
    # print(total_time)

############     Function triggered by UI (User Interface)     ############
def start_find(_C1, _C2, _C3, _C4, _SameProduct, _TargetRate, _complaint_id, _FILE_COUNT):
    Total_time = time.time()
    ###	Split master file into (MAIN-FILE-SIZE / FILE-COUNT) equal parts
    create_multi_file(int(1074017 / int(_FILE_COUNT)))
    ###	Starting thread function
    thread_start(int(_C1), int(_C2), int(_C3), int(_C4), int(_SameProduct), float(_TargetRate), str(_complaint_id), int(_FILE_COUNT))
    ###	Threads runtime
    Process_Time = []
    for i in range(len(START_TIME)):
        Process_Time.append(str(END_TIME[i] - START_TIME[i]))
        print(str(i + 1) + ".Thread one process time->	" + str(END_TIME[i] - START_TIME[i]))
    i = 0
    START_TIME.clear()
    END_TIME.clear()
    total_time = time.time() - Total_time
    return (DATA, Process_Time, "Checking savings account, Managing account, NAVY FEDERAL CREDIT UNION, FL, 328XX, 3198084", total_time)
