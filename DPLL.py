def DPLL(B, I):
	if not B:  # Si no hay cláusulas restantes, la fórmula es satisfacible
		return True, I
	
	for clause in B:
		if not clause:  # Si alguna cláusula está vacía, la fórmula no es satisfacible
			return False, None
	
	# Seleccionar una literal L (aquí se selecciona el primer literal de la primera cláusula)
	L = next(iter(B[0]))

	#asignacion con true
	# Crear B' eliminando cláusulas con L y complementos de L 
	_B = [clause for clause in B if abs(L) not in clause]
	_B = [clause.difference({-abs(L)}) for clause in _B]
	# Asignar L como verdadero en la asignación parcial I
	I_true = I.copy()
	I_true[abs(L)] = True

	# Llamada recursiva con L verdadero
	result_true, assignment_true = DPLL(_B, I_true)
	if result_true:
		return True, assignment_true
	
	# asignacion con false
	_B = [clause for clause in B if -abs(L) not in clause]
	_B = [clause.difference({abs(L)}) for clause in _B]
	# Asignar L como verdadero en la asignación parcial I
	I_false = I.copy()
	I_false[abs(L)] = False
	# Llamada recursiva con L falso
	result_false, assignment_false = DPLL(_B, I_false)
	if result_false:
		return True, assignment_false

	return False, None

# Ejemplo de uso
if __name__ == "__main__":
	# Representación de la fórmula en forma de cláusulas (conjuntos de literales)

	EXPR = "{{p,-q},{-p,-r}}"

	elements = {}
	curr_Index = 1

	B = []
	indexes = {}
	for e in EXPR.split(','):
		el = e.strip('{}')
		if el.startswith('-'):
			if el in elements :
				B.append({elements[el]})
			elif el.strip('-') in elements:
				B.append({-elements[el.strip('-')]})
			else:
				elements[el] = curr_Index
				B.append({-curr_Index})
				curr_Index += 1
		else:
			if el in elements:
				B.append({elements[el]})
			else:
				elements[el] = curr_Index
				B.append({curr_Index})
				curr_Index += 1

	# print(B)
	_b = [{-1,-2},{-1,3}]
	I = {}
	result, assignment = DPLL(_b, I)

	if result:
		print("La fórmula es satisfacible. Asignación parcial:", assignment)
	else:
		print("La fórmula no es satisfacible.")
