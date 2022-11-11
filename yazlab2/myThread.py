import sys, threading, os, time

C1 = 0
C2 = 5
SameProduct = -1
TargetRate = 0
complaint_id = "-1"
FILE_COUNT = 10

def intro(_C1, _C2, _SameProduct, _TargetRate, _complaint_id, _FILE_COUNT):
	C1 = int(_C1)
	C2 = int(_C2)
	SameProduct = int(_SameProduct)
	TargetRate = float(_TargetRate)
	complaint_id = str(_complaint_id)
	FILE_COUNT = int(_FILE_COUNT)
	return C1, C2, SameProduct, complaint_id, TargetRate, FILE_COUNT

def fileLen(fileName, FILE_COUNT):
	return int(1074017 / FILE_COUNT)

def create_multi_file(file_size):
	with open("trashFile2", "r", encoding="utf-8") as file:
		T = 0
		file_s = 1
		for s in file:
			if (T == 0):
				try:
					new_file = open("childFile" + str(file_s), "w")
					file_s += 1
				except:
					pass
			if (T <= file_size):
				try:
					new_file.write(s)
					T += 1
				except:
					pass
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
	if (complaint_id not in line and complaint_id != "-1"):
		return 1
	while (1):
		ctrl_line = F[thread_id].readline()
		if (ctrl_line):
			if (SameProduct != -1):
				if (line.split(", ")[SameProduct] not in ctrl_line):
					continue
			match = similarity_rate(ctrl_line, line, C1, C2)
			if (match > TargetRate):
				print(ctrl_line[:60] + "->	[" + str(match) + "]	[" + File_name + "]	[" + str(thread_id) + "]	[" + str(sub_thread_id) + "]\n")
				MatchFile.write(ctrl_line[:60] + "->	[" + str(match) + "]	[" + File_name + "]	[" + str(thread_id) + "]	[" + str(sub_thread_id) + "]\n")
		else:
			return 0


def	sub_thread_start(File_name, line, Thread_count, thread_id):
	print(Thread_count)
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

START_TIME = []
END_TIME = []
F = []
def start_find(_C1, _C2, _SameProduct, _TargetRate, _complaint_id, _FILE_COUNT):
	C1 = int(_C1)
	C2 = int(_C2)
	SameProduct = int(_SameProduct)
	TargetRate = float(_TargetRate)
	complaint_id = str(_complaint_id)
	FILE_COUNT = int(_FILE_COUNT)
	create_multi_file(fileLen("trashFile2", FILE_COUNT))

	
	for i in range(FILE_COUNT):
		fileee = open("childFile{}".format(i + 1), "r")
		F.append(fileee)
		
	thread_start(FILE_COUNT)

	for i in range(len(START_TIME)):
		print(str(i + 1) + ".Thread one process time->	" + str(END_TIME[i] - START_TIME[i]))

