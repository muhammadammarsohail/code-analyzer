from BagOfWords.WordsGenerator import WordsGenerator
from Tokenization.ClassPartAllocator import ClassPartAllocator
import re

def WordTokernizer(charList):
    bagOfWords = WordsGenerator(charList)
    # print(bagOfWords)
    for index in bagOfWords:
        print(index)
    return "Will return tokenset"
