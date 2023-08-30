import itertools

def fuerza_bruta(formula):
    literales = set()
    for clausula in formula:
        for literal in clausula:
            literales.add(literal[0])
 
    literales = list(literales)
    
    n = len(literales)
    for valor in itertools.product([True,False], repeat=n):
        asignacion = set(zip(literales, valor))
        if all([bool(literal.intersection(asignacion)) for literal in formula]):
            return True, asignacion
    return False, None

# (p∧¬p)
formula = [
    {("p", True)},
    {("p", False)}
]

#(p ∨ q ∨ ¬r)
# formula = [{("p", True)}, 
#     {("q", True)}, 
#     {("r", False)}
# ]

# ¬p
# formula = [
#     {("p", False)}
# ]


satisface, asignacion = fuerza_bruta(formula)

print("\n================================\n||        Fuerza Bruta        ||\n================================\n")
if satisface:
    print("La formula es satisfacible.")
    print("Asignacion :", asignacion)
else:
    print("La formula no es satisfacible.")
    
print("\n================================\n")
