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
# Ejemplo de un MUTANTE con una matriz 6x6
dna_ex = [
    "GTGGGG",
    "CAACTC",
    "TCCTGT",
    "ATTAGG",
    "CTTCAA",
    "TCATGT"
]
print("||| Bienvenido a GenomeSpy Ultra |||\n Por favor, siga las instrucciones:")
# Ingresar las filas de la matriz por teclado
#dna = [input(f"Ingrese la fila {i + 1} de la matriz: ").upper() for i in range(6)]

# Verificar si es mutante y mostrar el resultado
result = isMutant(dna_ex)
print("- - - - -\nResultado: ", result)
if result:
    print("- - - - - \nMUTANTE DETECTADO \nSe encontró más de 1 secuencia \nComienza fase de aislamiento...\n- - - - -")
else:
    print("- - - - - \nNO MUTANTE\nEspere a la entrega de su certificado\n- - - - -")