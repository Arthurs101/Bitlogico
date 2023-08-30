elements = {}
Index = 1
def DPLL(B, I):
	if not B:  # Si no hay cláusulas restantes, la fórmula es satisfacible
		return True, I
	
	for clause in B:
		if not clause or len(clause) == 0:  # Si alguna cláusula está vacía, la fórmula no es satisfacible
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
	result_true, assignment_true = DPLL(_B, I_true)
	if result_true:
		return True, assignment_true
	# asignacion con false
	_B = [clause for clause in B if -abs(L) not in clause]
	_B = [clause.difference({abs(L)}) for clause in _B]
	# Asignar L como verdadero en la asignación parcial I
	I_false = I.copy()
	I_false[abs(L)] = False
	result_false, assignment_false = DPLL(_B, I_false)
	if result_false:
		return True, assignment_false
	return False, None
def reparse(assignations):
	tmp = {}
	for akey,avalue in assignations.items():
		for key, value in elements.items():
			if value == akey:
				tmp[key] = avalue
				break
	return tmp
def parse(expression):
	Index = len(elements.keys()) + 1
	B = []
	for e in expression.split('},{'):
		temp = "{"
		for el in e.strip('{').strip('}').split(","):
			if el.startswith('-'):
				if el in elements :
					temp = temp + str(elements[el]) + ","
				elif el.strip('-') in elements:
					temp = temp + str(-elements[el.strip('-')]) + ","
				else:
					elements[el.replace('-','')] = Index
					temp = temp + str(-Index) + ","
					Index += 1
			else:
				if el in elements:
					temp = temp + str(elements[el]) + ","
				else:
					elements[el] = Index
					temp = temp + str(Index) + ","
					Index += 1
		temp = temp[:-1] + "}"
		B.append(eval(temp))

	return B
# Ejemplo de uso
elements = {"p" : 1, "q" : 2 ,"r": 3,"s" : 4}
if __name__ == "__main__":
	# Representación de la fórmula en forma de cláusulas (conjuntos de literales)
	EXPRESSIONS = ["{p},{-p}","{q,p,-p}",
		"{-p,-r,-s},{-q,-p,-s}","{-p,-q},{q,-s},{-p,s},{-q,s}"
		,"{-p, -q, -r}, {q, -r, p}, {-p, q, r}",
		"{r}, {-q, -r}, {-p, q, -r}, {q}"]
	Transforms = [[{1}, {-1}],[{2, 1, -1}],[{-1, -3, -4}, {-1, -2, -4}],[{-1, -2}, {2, -4}, {-1, 4}, {-2, 4}],
	       [{-1,-2,-3},{2,-3,1},{-1,2,3}],[{3},{-2,-3},{-1,2,-3},{2}]]
	# EXPR = "{-p,-q},{p,-q}".strip(" ")
	for EXPR in EXPRESSIONS:
		# B = parse(EXPR)
		B = Transforms[EXPRESSIONS.index(EXPR)]
		I = {}
		result, assignment = DPLL(B, I)
		if result:
			print(f"La fórmula {EXPR} es satisfacible. Asignación parcial: {reparse(assignment)}")
		else:
			print(f"La fórmula {EXPR} no es satisfacible.")
