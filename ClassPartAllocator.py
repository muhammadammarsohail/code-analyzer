from Classes import Classes as Cls

def ClassPartAllocator(param):
    Classes = Cls()
    if param=="":
        return -1
    for key,value in Classes.items():
        if param in value:
            return key
    return -1