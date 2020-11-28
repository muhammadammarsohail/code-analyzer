from ClassPartAllocator import ClassPartAllocator
import re


def FilterStartingSpaces(charList=[]):
    # return param
    for char in charList:
        if re.match("^[ ]$", char):
            charList.pop(charList.index(char))
        else:
            return charList


def WordTokernizer(charList):
    filteredList = FilterStartingSpaces(charList)
    lineNumber = 1
    BagOfWords = []
    wordBreaker = ['+', '-', '*', '%', '<', '>', '!']
    alone = ['?', ';', ':', '(', ')', '{', '}', ',', '[', ']']

    temp = ""

    for char in filteredList:
        if re.match("^[a-zA-Z0-9]$", char):
            if re.match("^[a-zA-Z0-9|_]$", temp[len(temp)-1]):
                temp = temp + char
            else:
                BagOfWords.append(temp)
                temp = char
        elif char in alone:
            BagOfWords.append(temp)
            temp = ""
            BagOfWords.append(char)
        elif char is " " or char is '\n':
            BagOfWords.append(temp)
            temp = ""