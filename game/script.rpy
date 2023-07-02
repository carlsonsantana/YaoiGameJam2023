# The script of the game goes in this file.

init python:
    def getDialogs():
        path = renpy.loader.transfn("resources/dialogs.txt");
        path = path.replace("\\","/")
        data = renpy.file(path).read().decode("utf-8")
        data = data.split("\n")
        d = {}
        lineInd = 1
        for line in data:
            d[int(lineInd)] = line[:-1]
            lineInd += 1
        return d
        
# The game starts here.
label start:
    call test_script
