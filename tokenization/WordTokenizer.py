from bagOfWords.WordsGenerator import WordsGenerator
from tokenization.ClassPartAllocator import ClassPartAllocator
import re

def WordTokernizer(charList):
    bagOfWords = WordsGenerator(charList)
    lineNumber = 1
    tokenSet = []
    for valuePart in bagOfWords:
        if type(valuePart) == int:
            lineNumber = valuePart
            continue
        classPart=ClassPartAllocator(valuePart)
        if classPart == -1:
            if valuePart == "":
                continue
            elif re.match('^[a-zA-Z0-9|_]{1,100}$',valuePart): #for identifier
                tokenSet.append(("Identifier",valuePart,lineNumber))
            elif valuePart[0]=="\"" and valuePart[len(valuePart)-1]=="\"": #for string
                tokenSet.append(("String",valuePart,lineNumber))
            elif valuePart[0]=="\'" and valuePart[len(valuePart)-1]=="\'": #for character
                tokenSet.append(("Character",valuePart,lineNumber))
            else:
                tokenSet.append(("Invalid",valuePart,lineNumber))
            continue
        tokenSet.append((classPart,valuePart,lineNumber))
    return tokenSet
