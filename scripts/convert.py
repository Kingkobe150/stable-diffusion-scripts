#resizes and adds a black bar to all images in directory original
import traceback
import os, os.path

def filesInDir(dir):
    final = sum([len(files) for r, d, files in os.walk(dir)])
    return final

def writetofile(input):
    f = open("failed_convertions.txt", "a")
    f.write(input + "\n")
    f.close()

def writetolist(input):
    f = open("failedIds.txt", "a")
    f.write(input + "\n")
    f.close()

from PIL import Image, ImageOps
from pathlib import Path
import os

directory = 'nsfw_rsync/original'
saveTo = 'resized_rsync'
numFiles = filesInDir(directory)
counter = 0

for filename in os.listdir(directory):
    var1 = directory + '/' + filename
    saveToTmp2 = saveTo + '/' + filename
    os.makedirs(saveToTmp2, exist_ok=True)
    for i in os.listdir(var1):
        var4 = var1 + '/'
        var2 = var1 + '/' + i
        if os.path.isfile(var2):
            counter = counter + 1
            print(str(counter) + "/" + str(numFiles) + " " + "Doing: " + str(var2))
            fileActualExt = Path(var2).suffix
            if fileActualExt == ".jpg" or ".jpeg" or ".gif" or ".png" or ".bmp" or ".webp":
                try:
                    im = Image.open(var2)
                    fileActualName = Path(var2).stem
                    im = im.convert('RGB')
                    im = ImageOps.pad(im, (512, 512), color='black')
                    im.save(saveToTmp2 + "/" + fileActualName + '.jpg', format="JPEG", quality=100)
                except:
                    traceback.print_exc()
                    var = traceback.format_exc()
                    print("The following image failed so save!: " + var2)
                    writetofile("common_failure " + var2 + "Exception: " + str(var))
                    writetolist(var2)
            else:
                print("file not an image " + var2)
                writetofile("file_not_img " + var2)
            




