import ply.yacc as yacc
from lexer import tokens  # Importer les tokens du lexer

# Règles du parser
def p_start(p):
    '''start : statement
             | start statement'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[1].append(p[2])
        p[0] = p[1]

def p_statement_decl(p):
    'statement : DECLARER ID '
    p[0] = f"{p[2]} = None"

def p_statement_affect(p):
    'statement : ID EGAL expression'
    p[0] = f"{p[1]} = {p[3]}"

def p_expression(p):
    '''expression : term
                 | expression PLUS term
                 | expression MOINS term'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = f"{p[1]} {p[2]} {p[3]}"

def p_term(p):
    '''term : NUM
            | ID'''
    p[0] = str(p[1])

def p_error(p):
    if p:
        print(f"Erreur de syntaxe à '{p.value}'")
    else:
        print("Erreur de syntaxe à la fin du fichier")

# Fonction pour obtenir le parser
def get_parser():
    return yacc.yacc()
