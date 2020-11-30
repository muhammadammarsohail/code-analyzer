if __name__ == "__main__":
    import re #Importing ReGex module
    from Tokenization.WordTokenizer import WordTokernizer

str = r"""
==++=*++===-+o-=o-o-o+o
""" 
#may be it will come directly from the Text box.

# app = Flask(__name__)
# @app.route('/')
# def handleHome():
charArr = list(str) #Character list/array.
TokenSet = WordTokernizer(charArr)
    # return jsonify(TokenSet)

# if __name__=="__main__":
#     app.run(debug=True)

