import sys
from lexer import Lexer
from parser import Parser
from interpreter import Interpreter

def main(filename):
    with open(filename, 'r') as file:
        code = file.read()

    lexer = Lexer(code)
    tokens = lexer.tokenize()

    parser = Parser(tokens)
    ast = parser.parse()

    interpreter = Interpreter(ast)
    interpreter.interpret()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Uso: python app.py archivo.abi")
    else:
        main(sys.argv[1])
