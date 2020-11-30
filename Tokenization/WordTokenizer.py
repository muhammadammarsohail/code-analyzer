from BagOfWords.WordsGenerator import WordsGenerator
from Tokenization.ClassPartAllocator import ClassPartAllocator
import re

def WordTokernizer(charList):
    bagOfWords = WordsGenerator(charList)
    for index in bagOfWords:
        print(index,end=' ')
        print(ClassPartAllocator(index),end='\n')
    return bagOfWords
