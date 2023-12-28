def getdescription(path:str)->str:
    with open(path, 'r') as file:
        return file.read()
    
