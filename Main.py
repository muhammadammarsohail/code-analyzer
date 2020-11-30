import re #Importing ReGex module
from flask import Flask, jsonify
from Tokenization.WordTokenizer import WordTokernizer


str = r"""
int name = "nameer";
jabtak(name=='a'){
    print("Hello Wrold") a1.909asd9.55
}
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