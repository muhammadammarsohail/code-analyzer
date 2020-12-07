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
            try: #for integer constant
                typeCastInt = int(valuePart)
            except:
                try: #for float constant
                    typeCastFloat = float(valuePart)
                except:
                    if valuePart == "":
                        continue
                    # elif re.match('^[0-9]{1,25}$',valuePart): #for integer constant
                    #     tokenSet.append(("Integer constant",valuePart,lineNumber)) 
                    elif valuePart=="true" or valuePart=="false": #for bool constant
                        tokenSet.append(("Boolean constant",valuePart,lineNumber)) 
                    elif re.match('^[a-zA-Z0-9|_]{1,100}$',valuePart): #for identifier
                        tokenSet.append(("Identifier",valuePart,lineNumber))
                    elif valuePart[0]=="\"" and valuePart[len(valuePart)-1]=="\"": #for string constant
                        tokenSet.append(("String constant",valuePart,lineNumber))
                    elif valuePart[0]=="\'" and valuePart[len(valuePart)-1]=="\'": #for character constant
                        tokenSet.append(("Character constant",valuePart,lineNumber))
                    else:
                        tokenSet.append(("Invalid",valuePart,lineNumber))
                    continue
                else:
                    tokenSet.append(("Float constant",valuePart,lineNumber))
                    continue
            else:
                    tokenSet.append(("Integer constant",valuePart,lineNumber))
                    continue

        tokenSet.append((classPart,valuePart,lineNumber))
    return tokenSet
