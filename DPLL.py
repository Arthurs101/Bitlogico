def DPLL(B, I):
    if not B:  # Si no hay cláusulas restantes, la fórmula es satisfacible
        return True, I
    
    for clause in B:
        if not clause:  # Si alguna cláusula está vacía, la fórmula no es satisfacible
            return False, None
    
    # Seleccionar una literal L (aquí se selecciona el primer literal de la primera cláusula)
    L = next(iter(B[0]))

    # Crear B' eliminando cláusulas con L y complementos de L
    _B = [clause - {-L} for clause in B if L in clause]
    
    # Crear B'' eliminando cláusulas con complemento de L y L
    _B = [clause - {L} for clause in B if -L in _B]

    # Verificar que el tamaño de B disminuya en cada llamada recursiva
    if len(_B) >= len(B):
        return False, None

    # Asignar L como verdadero en la asignación parcial I
    I_true = I.copy()
    I_true[abs(L)] = True

    # Llamada recursiva con L verdadero
    result_true, assignment_true = DPLL(_B, I_true)
    if result_true:
        return True, assignment_true

    return False, None


if __name__ == "__main__":
    # Representación de la fórmula en forma de cláusulas (conjuntos de literales)
    B = [
        {1} ,
        {-1} 
    ]
    I = {}

    result, assignment = DPLL(B, I)

    if result:
        print("La fórmula es satisfacible. Asignación parcial:", assignment)
    else:
        print("La fórmula no es satisfacible.")
