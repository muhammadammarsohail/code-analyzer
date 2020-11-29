from BagOfWords.FilterStartingSpaces import FilterStartingSpaces
import re

def WordsGenerator(charList):
    filteredList = FilterStartingSpaces(charList)
    BagOfWords = []
    wordBreaker = ['+', '-', '*', '%', '<', '>', '!']
    alone = ['?', ';', ':', '(', ')', '{', '}', ',', '[', ']']
    temp = ""
    iterator = 0
    while iterator < len(filteredList):
        # handling identifiers or keywords.
        if re.match("^[a-zA-Z0-9]$", filteredList[iterator]):
            if temp != "" and re.match("^[a-zA-Z0-9|_]$", temp[len(temp)-1]):
                temp = temp + filteredList[iterator]
            elif temp != "" and not re.match("^[a-zA-Z0-9|_]$", temp[len(temp)-1]):
                BagOfWords.append(temp)
                temp = filteredList[iterator]
            else:
                temp = filteredList[iterator]
# handling any of the character present in alone list.
        elif filteredList[iterator] in alone:
            BagOfWords.append(temp)
            temp = ""
            BagOfWords.append(filteredList[iterator])
# handling spaces and newline charracter.
        elif filteredList[iterator] == " " or filteredList[iterator] == '\n':
            BagOfWords.append(temp) if temp != "" else False
            temp = ""
# handling charcter.
        elif filteredList[iterator] == '\'':
            if temp != "" and temp[0] == '\'':
                temp += '\''
                BagOfWords.append(temp)
                temp = ""
            else:
                temp = '\''
                iterator += 1
                while filteredList[iterator] != '\'' and temp[len(temp)-1] != '\\':
                    temp += filteredList[iterator]
                    iterator += 1
                continue
# handling strings.
        elif filteredList[iterator] == '\"':
            if temp != "" and temp[0] == '\"':
                temp += '\"'
                BagOfWords.append(temp)
                temp = ""
            else:
                temp = '\"'
                iterator += 1
                while filteredList[iterator] != '\"' and temp[len(temp)-1] != '\\':
                    temp += filteredList[iterator]
                    iterator += 1
                continue
# handling word breakers.
        elif filteredList[iterator] in wordBreaker:
            if temp == "":
                temp = filteredList[iterator]
                if filteredList[iterator+1] == "=":
                    iterator += 1
                    temp += filteredList[iterator]
                    BagOfWords.append(temp)
                    temp = ""
                    continue
                else:
                    BagOfWords.append(temp)
                    temp = ""
            else:
                BagOfWords.append(temp)
                temp = filteredList[iterator]
                if filteredList[iterator+1] == "=":
                    iterator += 1
                    temp += filteredList[iterator]
                    BagOfWords.append(temp)
                    temp = ""
                    continue
                else:
                    BagOfWords.append(temp)
                    temp = ""
# handling assignment and equality operators.
        elif filteredList[iterator] == '=':
            if temp != "=":
                BagOfWords.append(temp)
                temp = filteredList[iterator]
            elif temp == '=':
                temp += filteredList[iterator]
                BagOfWords.append(temp)
                temp = ""
            else:
                temp += filteredList[iterator]
# handling dot(.)
        elif filteredList[iterator] == '.':
            pass

        iterator += 1
    return BagOfWords