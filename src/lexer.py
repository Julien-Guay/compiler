import ply.lex as lex

# Définition des tokens
tokens = (
    'DECLARER',
    'ID',
    'PLUS',
    'MOINS',
    'NUM',
    'EGAL',
    'FIN',
)

# Règles du lexer
def t_DECLARER(t):
    r'Declarer'
    return t

def t_AFFECTER(t):
    r'Affecter'
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_PLUS = r'\+'
t_MOINS = r'-'
t_EGAL = r'='
t_FIN = r'FIN'

# Ignorer les espaces
t_ignore = ' '

# Ignorer les retours à la ligne
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Ignorer les tabulations
def t_tab(t):
    r'\t+'
    pass

def t_error(t):
    print(f"Caractère illégal '{t.value[0]}'")
    t.lexer.skip(1)

# Fonction pour obtenir le lexer
def get_lexer():
    return lex.lex()
