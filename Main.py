if __name__ == "__main__":
    import re #Importing ReGex module
    from WordTokenizer import WordTokernizer
    str = """   a int age nameer _ammar main class  = ; 
    """ 
    #may it will come directly from the Text box.
    charArr = list(str) #Character list/array.
    print(WordTokernizer(charArr))