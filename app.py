import sys
from lexer import Lexer
from parser import Parser

def main(filename):
    with open(filename, 'r') as file:
        code = file.read()

    lexer = Lexer(code)
    tokens = lexer.tokenize()

    print("Tokens:", tokens)

    parser = Parser(tokens)
    ast = parser.parse()

    print("AST:", ast)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Uso: python app.py archivo.abi")
    else:
        main(sys.argv[1])
