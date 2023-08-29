def evaluar_formula(clausula, asignacion):
    for literal in clausula:
        variable = literal[1:]
        print("literal: ", variable)
        print("variable: ", variable)
        negado = literal[0] == '-'
        
        if variable not in asignacion:
            continue
        
        valor = asignacion[variable]
        if (negado and valor == 0) or (not negado and valor == 1):
            return True
    
    return False

def fuerza_bruta(formula):
    if formula == "":
        return False, {}

    variables = set()
    clausulas = formula.split('∧')
    
    for clausula in clausulas:
        clausula = clausula.strip()
        variables.update(literal[1:] for literal in clausula.split('∨'))
        variables.update(literal[1:] for literal in clausula.split('∧'))
        variables.update(literal[1:] for literal in clausula.split('|'))
    
    variables = list(variables)
    
    for i in range(2 ** len(variables)):
        asignacion = {variables[j]: (i >> j) & 1 for j in range(len(variables))}
        satisfactible = True
        
        for clausula in clausulas:
            if not evaluar_formula(clausula.split('∨'), asignacion) and not evaluar_formula(clausula.split('∧'), asignacion) and not evaluar_formula(clausula.split('|'), asignacion):
                satisfactible = False
                break
        
        if satisfactible:
            return True, asignacion
    
    return False, {}

formulas = ["p∧-p", "p∧-q", "p∨q", "p∨-q", "p|q", ""]
for formula in formulas:
    es_satisfactible, asignacion = fuerza_bruta(formula)

    if es_satisfactible:
        print(f"La fórmula '{formula}' es satisfactible con la asignación:")
        for variable, valor in asignacion.items():
            print(f"{variable}: {valor}")
    else:
        print(f"La fórmula '{formula}' no es satisfactible.")
