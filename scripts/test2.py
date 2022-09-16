import os, os.path

def filesInDir(dir):
    final = sum([len(files) for r, d, files in os.walk(dir)])
    return final

def writetofile(input):
    f = open("failed_convertions.txt", "a")
    f.write(input + "\n")
    f.close()

NumFiles = filesInDir("nsfw_rsync/original/")
print(NumFiles)