import os 
from pathlib import Path
DIRECTORIOS={
    "DOCUMENTOS":['.pdf','.docx','.txt'],
    "CALCULO":['.xls','.csv','.xlsx'],
    "AUDIO":['.mp3','.m4a', '.m4b'],
    "VIDEO":['.mov','.mp4','.avi'],
    "IMAGENES":['.jpg','.jpeg', '.png'],
    "COMPRIMIDOS":['.7z','.rar','.zip'],
    "INSTALADORES":['.msi','.exe']
}
def pickDirectory(value):
    for category, suffixes in DIRECTORIOS.items():
        for suffix in suffixes:
            if suffix == value:
                return category
    return "OTROS"       
def organizeDirectory():
    for item in os.scandir():
        #que salte el item si es un directorio
        if item.is_dir():
            continue
        filePath = Path(item)
        fileType = filePath.suffix.lower()
        directory = pickDirectory(fileType)
        directoryPath = Path(directory)
        #crear el directoriuo si no existe el path
        if directoryPath.is_dir() != True:
            directoryPath.mkdir()
        #mover el archivo al nuevo directorio
        if fileType == ".py":
            continue
        filePath.rename(directoryPath.joinpath(filePath))
organizeDirectory()