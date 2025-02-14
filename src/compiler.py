from lexer import get_lexer
from parser import get_parser

# Construction
lexer = get_lexer()
parser = get_parser()

# Fonction de test
def compile(text):
    result = parser.parse(text, lexer=lexer)
    if result:
        return '\n'.join(result)
    return ''

# Test
code = """Declarer x
  x=2 """
print(compile(code))
