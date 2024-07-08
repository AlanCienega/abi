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
  def __init__(self, code):
    self.code = code
    self.tokens = []
    self.pos = 0
    self.line = 1
    
  def tokenize(self):
    lines = self.code.split('\n')
    for line_num, line in enumerate(lines, start=1):
      pos = 0
      if not line.strip():
        continue
      while pos < len(line):
        for token_type, pattern in TOKENS.items():
          match = pattern.match(line[pos:])
          if match:
            value = match.group()
            if token_type == 'COMMENT':
              self.tokens.append((token_type, value[12:]))
            elif token_type == 'NEWLINE':
              self.line += 1
              self.tokens.append((token_type, value))
            elif token_type == 'SKIP':
              pos += len(value)
              break
            elif token_type == 'MISMATCH':
              raise RuntimeError(f'{value} inesperado en la línea {line_num}')
            else:
              self.tokens.append((token_type, value))
            pos += len(value)
            break
        else:
            raise ValueError(f'Carácter inesperado: {line[pos]} en la línea {line_num}')
      self.tokens.append(('NEWLINE', '\n'))
    return self.tokens
