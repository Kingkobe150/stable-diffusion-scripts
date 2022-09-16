numero = -1
for i in range(12):
    numero = numero + 1
    str_numero = str(numero)
    zfilled = str_numero.zfill(2)
    json_file_name = "posts0000000000" + zfilled + ".json"
    print(json_file_name)