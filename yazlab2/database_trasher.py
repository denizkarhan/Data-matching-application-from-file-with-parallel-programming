import csv, threading

file_name = "trashFile"
stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

def multi_file_create():
    dosya = open("rows.csv","r+",encoding="utf8")
    with open('rows.csv', 'r') as csv_file:
        file = open(file_name, "w")
        for j in csv_file:
            file.write(j)
        file.close()

def remove_stopwords(data):
    output_array=[]
    for sentence in data:
        temp_list=[]
        for word in sentence.split():
            if word.lower() not in stopwords:
                temp_list.append(word)
        output_array.append(' '.join(temp_list))
    return output_array

def file_reader():
    file = open(file_name, "r")
    file2 = open("trashFile2", "w", encoding="utf8")
    for j in file:
        a = j.split(",")
        element = ""
        c = []
        flag = 1
        for i in a:
            if (("\"" not in i) and (flag == 1)):
                c.append(i.strip("\"\', \n"))
            elif(("\"" in i) and (flag == 0)):
                element += i
                c.append(element.strip("\"\', \n"))
                element = ""
                flag = 1
            else:
                flag = 0
                element += i
        i = 0
        for s in c:
            if (i == 1 or i == 3 or i == 7 or i == 8 or i == 9 or i == 17):
                if (len(s) < 1):
                    continue
            i += 1
            try:
                if (i == 17 and i<=18):
                    elmnt = c[1] + ", " + c[3] + ", " + c[7] + ", " + c[8] + ", " + c[9] + ", " + c[17]
                    elmnt = ", ".join(remove_stopwords(elmnt.split(",")))
                    file2.write(elmnt + "\n")
            except:
                pass
    file2.close()
    file.close()

multi_file_create()
file_reader()