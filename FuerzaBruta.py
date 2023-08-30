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
Formula1= [set({('p', True)}), set({('p', False)})]
Formula2= [{('q', True), ('p', True),('p', False)}]
Formula3 = [set({('r', False), ('s', False), ('p', False)}), set({('q', False), ('s', False), ('p', False)})]
Formula4 =  [set({('q', False), ('p', False)}), set({('q', True), ('s', False)}), set({('s', True), ('p', False)}), set({('q', False), ('s', True)})]
Formula5 =  [set({('q', False), ('p', False), ('r', False)}), set({('q', False), ('r', True), ('p', True)}), set({('q', True), ('p', True), ('r', True)})]
Formula6 = [set({('r', True)}), set({('q', False), ('r', False)}), set({('r', False), ('p', False), ('q', True)}), set({('q', True)})]


formulas = [Formula1,Formula2,Formula3,Formula4,Formula5,Formula6]


print("\n================================\n||        Fuerza Bruta        ||\n================================\n")
for formula in formulas:
    print(formula)
    satisface, asignacion = fuerza_bruta(formula)
    if satisface:
        print("La formula es satisfacible.")
        print("Asignacion :", asignacion)
    else:
        print("La formula no es satisfacible.")
        
    print("\n================================\n")
