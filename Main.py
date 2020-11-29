if __name__ == "__main__":
    import re #Importing ReGex module
    from WordTokenizer import WordTokernizer
    str = """ name _nam19 ?;= 1983nameer 
    waqas \'hello world\'\'nameer\' \"waqas\" +=- 
    """ 
    #may it will come directly from the Text box.
    charArr = list(str) #Character list/array.
    print(WordTokernizer(charArr))