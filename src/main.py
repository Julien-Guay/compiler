# main.py
from compiler import compiler

# Exemple de pseudo-code à compiler
pseudo_code = '''
Déclarer x
Affecter x à 10
Si x est plus grand que 5 alors
    Affecter x à 20
Tant que x est inférieur à 30 faire
    Affecter x à x + 1
fin
'''

# Compiler le pseudo-code en Python
python_code = compiler(pseudo_code)
print(python_code)
