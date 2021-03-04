# All imports
from tokenization.WordTokenizer import WordTokernizer
from LexicalErrs import LexicalErrorDetector
from syntaxAnalyzer.syntaxAnalyzer import SA

#                           Implemetation
# Word tokenizer will generate the token sets.
tokenSets = WordTokernizer(
"""ijtemai class meri{

}
class myClass{
    void Main(){

    } 
}
""")
print(f"==========>>Token Set\n{tokenSets}\n<<==========")

# Lexical error detector will detect the invalid tokens from tokens set

LexicalErrorDetector(tokenSets)

# Syntax analyzer, analyzes token sets and will print the syntax error, if occur.
tokenSets.append(("$", "$", -1))

saInst = SA()
saInst.SyntaxAnalyzer(tokenSets)
