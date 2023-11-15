import time
def isMutant(dna):
    rows = len(dna)
    cols = len(dna[0])

    # Verifica si hay secuencias iguales en forma horizontal, vertical o diagonal
    def control_sequence(secuencia):
        return 'AAAA' in secuencia or 'TTTT' in secuencia or 'CCCC' in secuencia or 'GGGG' in secuencia

    # Verifica si hay secuencias iguales en forma horizontal
    def valid_horizontal(matrix):
        count = 0
        for row in matrix:
            # if para evitar entrar en el bucle, si no se cumple la condición no es necesario el análisis
            if row[2] == row[3]:
                for col in range(cols - 3):
                    secuencia = ''.join(row[col:col + 4])
                    if control_sequence(secuencia):
                        count += 1
                        if count < 3:
                            print("Secuencia horizontal encontrada: ", secuencia)
        return count
    # Llamamos a la función
    count = valid_horizontal(dna) 
    if count >= 2:
        return True
    else:
    # Verifica si hay secuencias iguales en forma vertical
        def valid_vertical(matrix, count):
            for col in range(cols):
                # if para evitar entrar en el bucle, si no se cumple la condición no es necesario el análisis
                if matrix[2][col] == matrix[3][col]:
                    for row in range(rows - 3):
                        secuencia = ''.join(matrix[row + i][col] for i in range(4))
                        if control_sequence(secuencia):
                            count += 1
                            if count < 3:
                                print("Secuencia vertical encontrada: ", secuencia)
            return count
        count = valid_vertical(dna,count)
        if count >= 2:
            return True
        else:
    # Verifica si hay secuencias iguales en forma diagonal (de izquierda a derecha)
            def valid_diagonal(matrix, count):
                for row in range(rows - 3):
                    for col in range(cols - 3):
                        secuencia = ''.join(matrix[row + i][col + i] for i in range(4))
                        if control_sequence(secuencia):
                            count += 1
                            if count < 3:
                                print("Secuencia diagonal encontrada: ", secuencia)
                return count
            count = valid_diagonal(dna,count)
            if count >=2:
                return True
            else:
    # Verifica si hay secuencias iguales en forma diagonal (de derecha a izquierda)
                def valid_rev_diagonal(matrix, count):
                    for row in range(rows - 3):
                        for col in range(3, cols):
                            secuencia = ''.join(matrix[row + i][col - i] for i in range(4))
                            if control_sequence(secuencia):
                                count += 1
                                if count < 3:
                                    print("Secuencia diagonal sec. encontrada: ", secuencia)
                    return count
                count = valid_rev_diagonal(dna,count)
                if count >= 2:
                    return True
                else:
                    return False

print("||| Bienvenido a Genome Scan |||\n Por favor, siga las instrucciones:\n - Ingrese la serie de su ADN (4 bases: A, T, C o G)")
time.sleep(3)
bases = {'A', 'T', 'C', 'G'}
dna = [
    "ACGTAG",
    "CAGCAC",
    "GCTACT",
    "CATTAG",
    "ACGACC",
    "ATGCGG"
]
print("Datos ingresados:", dna)
print("Analizando datos...")
time.sleep(4)
# Verifica si es mutante y muestra el resultado
result = isMutant(dna)
print("- - - - -\nResultado: ", result)
if result:
    print("- - - - - \nMUTANTE DETECTADO \nSe encontró más de 1 secuencia \nComienza fase de aislamiento...\n- - - - -")
else:
    print("- - - - - \nNO MUTANTE\nEspere a la entrega de su certificado\n- - - - -")