from tokenization.Classes import Classes as Cls

def ClassPartAllocator(param):
    ClassesApla,ClassesSymba = Cls()
    if param=="":
        return -1
    for key,value in ClassesApla.items():
        if param in value:
            return key
    for key,value in ClassesSymba.items():
        if param in value:
            return key
    return -1