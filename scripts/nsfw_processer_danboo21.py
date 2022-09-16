#converts nsfw-ids.txt entries to rsync readable file
import json

def file_len(filename):
    with open(filename) as f:
        for i, _ in enumerate(f):
            pass
    return i + 1

def writetofile(input):
    f = open("files2download.txt", "a")
    f.write(input + "\n")
    f.close()

with open("nsfw-ids.txt", 'r', encoding="utf8") as nsfwfile:
    nsfw_list = list(nsfwfile)
count = 0
linescount = file_len("nsfw-ids.txt")

with open('data.json') as data:
    dictdump = json.loads(data.read())

##Read line
for line in nsfw_list:
    line = line.strip()
    # print(line)
    linefilled1 = line.zfill(4)
    linelast3 = linefilled1[-3:]
    linedirectory = linelast3.zfill(4)
    # print("line: " + ">>"+ line + "<<")
    # print("Linefilled1: " + linefilled1)
    # print("linelast3: " + linelast3)
    # print("linedirectory: " + linedirectory)
    file_ext = dictdump[line]
    #print(file_ext)
    directory = "original/" + linedirectory + "/" + line + "." + file_ext
    # print(directory)
    # print(directory2)
    writetofile(directory)
    count = count + 1
    print(str(count) + "/" + str(linescount))
