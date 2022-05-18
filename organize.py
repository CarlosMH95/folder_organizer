import os 
from pathlib import Path
from uuid import uuid1
def make_unique_name(string):
    ident = uuid1().__str__()
    return f"{ident}-{string}"

DIRECTORIOS={}

def init_directories():
    d = {}
    file = open('directories.csv', 'r')
    for line in file:
        directory_list = line.strip("\n").split(',')
        dir_name = directory_list.pop(0)
        d[dir_name] = directory_list
    file.close()
    return d

def pickDirectory(value):
    for category, suffixes in DIRECTORIOS.items():
        for suffix in suffixes:
            if suffix == value:
                return category
    return "MISC"       

def organizeDirectory():
    for item in os.scandir():
        uniq=1
        #que salte el item si es un directorio
        if item.is_dir():
            continue
        fileName=item.name
        filePath = Path(item)
        fileType = filePath.suffix.lower()
        directory = pickDirectory(fileType)
        directoryPath = Path(directory)
        #crear el directorio si no existe el path
        if directoryPath.is_dir() != True:
            directoryPath.mkdir()
        #mover el archivo al nuevo directorio
        if fileType == ".py" or fileName == "directories.csv":
            continue
        path = directoryPath.joinpath(filePath)
        if (not os.path.exists(path)):
            filePath.rename(path)
        else:
            #Corregir error, no lo mueve a la carpeta final, y no se que pasa si encuentra otro con el mismo nombre
            while os.path.exists(path):
                path_string = path.name
                index = path_string.index(".")
                path_string = path_string[:index] +"-" + str(uniq) + path_string[index:]
                path = Path(path_string)
                uniq += 1
            filePath.rename(path)
DIRECTORIOS = init_directories()
organizeDirectory()

