from ClassPartAllocator import ClassPartAllocator
import re

    # lineNumber  = 1
    # temp = "" #To hold value temporarily
    # tokenSet=[]
    # for char in charArr:
    #     if char == " ":
    #         classPart = ClassPartAllocator(temp)
    #         if classPart == -1:
    #             classPart = "Identifier" if re.match("^[a-z|_]([a-zA-Z0-9]{1,25})?$",temp) else "Invalid"
    #         tokenSet.append((classPart,temp,lineNumber))
    #         temp=""
    #     elif char=="=" or char == ";":
    #         temp = temp + char
    #         classPart = ClassPartAllocator(char)
    #         tokenSet.append((classPart,temp,lineNumber))
    #     else:
    #         if re.match("^[a-zA-Z0-9]$",char) :
    #             temp = temp + char
    #             continue
    # return tokenSet
def FilterStartingSpaces(charList=[]):
    # return param
    for char in charList:
        if re.match("^[ ]$",char):
            charList.pop(charList.index(char))
        else:
            return charList

def WordTokernizer(charList):
   return FilterStartingSpaces(charList)