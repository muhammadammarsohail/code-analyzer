import re #Importing ReGex module
from flask import Flask, jsonify, render_template
from tokenization.WordTokenizer import WordTokernizer

str = r"""
    a=a+b+c%d%p;     
""" 

charArr = list(str) #Character list/array.
TokenSet = WordTokernizer(charArr)
print(TokenSet)

#may be it will come directly from the Text box.

app = Flask(__name__)
@app.route('/')
def handleHome():
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

