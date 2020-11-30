if __name__ == "__main__":
    import re #Importing ReGex module
    from Tokenization.WordTokenizer import WordTokernizer

    str =r""" 
            '\\n'=!!!!!
    """ 
    #may be it will come directly from the Text box.

    charArr = list(str) #Character list/array.
    TokenSet = WordTokernizer(charArr)