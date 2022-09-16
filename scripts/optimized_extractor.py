import json
import os
import shutil

directoryToSave = 'extracted'
directoryToSearch = 'resized_rsync'
directoryMetadata = 'metadata'

def writefile(filename, text):
    f = open(filename, "w")
    f.write(text)
    print('Saved the following: ' + text)
    f.close()

numero = -1
for i in range(12):
    numero = numero + 1
    str_numero = str(numero)
    zfilled = str_numero.zfill(2)
    json_file_name = "metadata/posts0000000000" + zfilled + ".json"
    print(json_file_name)
    