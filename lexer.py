import re

# Definición de tokens
TOKEN_SPECIFICATION = [
    ('COMMENT', r'^comentario:.*'),
    ('NUMBER', r'^\d+$'),
    ('ASSIGN', r'\basignale\b'),
    ('TYPE', r'\btipo\b'),
    ('PRINT', r'\bmuestra\b'),
    ('A', r'\ba\b'),
    ('VAR', r'^[a-zA-Z_][a-zA-Z0-9_]*$'),
    ('NEWLINE', r'\n'),
    ('SKIP', r'[ \t]+'),
    ('MISMATCH', r'.'),
]

TOKENS = {name: re.compile(pattern) for name, pattern in TOKEN_SPECIFICATION}

# Función para encotrar el valor de un token
def find_token(text):
  for token, pattern in TOKENS.items():
      match = pattern.match(text)
      if match:
          value = match.group()
          if token == 'NUMBER':
            return (token, int(value))
          else:
            return (token, value)
  raise ValueError(f'Invalid token: {text}')

print(find_token('variable'))
print(find_token('cosa'))
print(find_token('123'))
print(find_token('1a'))
print(find_token('a32'))
print(find_token('comentario'))
print(find_token('comentario: esto es un comentario'))
print(find_token('tipo'))
print(find_token('muestra'))
print(find_token('asignale'))
print(find_token('a'))
print(find_token('aa'))
print(find_token('a1'))
print(find_token('\n'))
print(find_token('   '))
print(find_token('123a'))
print(find_token('%'))
print(find_token('@45'))