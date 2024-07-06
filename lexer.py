import re

# Definición de tokens
TOKEN_SPECIFICATION = [
    ('COMMENT', r'^comentario: .*'),
    ('NUMBER', r'^\d+$'),
    ('ASSIGN', r'\basignale\b'),
    ('TYPE', r'\btipo\b'),
    ('TYPE_NUMBER', r'\bentero\b'),
    ('TYPE_BOOLEAN', r'\blogico\b'),    
    ('PRINT', r'\bmuestra\b'),
    ('A', r'\ba\b'),
    ('VAR', r'^[a-zA-Z_][a-zA-Z0-9_]*'),
    ('NEWLINE', r'\n'),
    ('SKIP', r'[ \t]+'),
    ('MISMATCH', r'.'),
]

TOKENS = {name: re.compile(pattern) for name, pattern in TOKEN_SPECIFICATION}

class Lexer:
  def __init__(self):
    self.tokens = []

  def lex(self, text):
    self.tokens = []
    lines = text.split('\n')
    for line_num, line in enumerate(lines, start=1):
      pos = 0
      if not line.strip():
        continue
      while pos < len(line):
        for token, pattern in TOKENS.items():
          match = pattern.match(line[pos:])
          if match:
            value = match.group()
            if token == 'COMMENT':
              self.tokens.append((token, value[12:]))
            else:
              self.tokens.append((token, value))
            pos += len(value)
            break
        else:
          raise ValueError(f'Invalid token at line {line_num}, position {pos + 1}: {line[pos]}')
      self.tokens.append(('NEWLINE', '\n'))
    return self.tokens

# Código de prueba
code = """
a mi_caja tipo entero asignale 42
"""

lexer = Lexer()
tokens = lexer.lex(code)

print("Código de ejemplo:")
print("_"*40)
print(code)
print("_"*40)


for token in tokens:
    print(token)
