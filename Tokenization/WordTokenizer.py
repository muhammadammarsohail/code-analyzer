from BagOfWords.WordsGenerator import WordsGenerator
from Tokenization.ClassPartAllocator import ClassPartAllocator
import re

def WordTokernizer(charList):
    bagOfWords = WordsGenerator(charList)
    tokenSet = []
    for valuePart in bagOfWords:
        classPart=ClassPartAllocator(valuePart)
        # print(valuePart)
        if classPart == -1:
            if valuePart == "":
                continue
            elif re.match('^[a-zA-Z|_]([a-zA-Z]{1-100})?$',valuePart): #for identifier
                tokenSet.append(("Identifier",valuePart))
            elif valuePart[0]=="\"" and valuePart[len(valuePart)-1]=="\"": #for string
                tokenSet.append(("String",valuePart))
            elif valuePart[0]=="\'" and valuePart[len(valuePart)-1]=="\'": #for character
                tokenSet.append(("Character",valuePart))
            else:
                tokenSet.append(("Invalid",valuePart))
            continue
        tokenSet.append((classPart,valuePart))
    return tokenSet
