def isMutant(dna):
    rows = len(dna)
    cols = len(dna[0])

    # Verifica si hay secuencias iguales en forma horizontal, vertical o diagonal
    def control_sequence(secuencia):
        return 'AAAA' in secuencia or 'TTTT' in secuencia or 'CCCC' in secuencia or 'GGGG' in secuencia

    # Verifica si hay secuencias iguales en forma horizontal
    def valid_horizontal(matriz):
        for row in matriz:
            for col in range(cols - 3):
                secuencia = ''.join(row[col:col + 4])
                if control_sequence(secuencia):
                    return True
    # Verifica si hay secuencias iguales en forma vertical
    def valid_vertical(matriz):
        for col in range(cols):
            for row in range(rows - 3):
                secuencia = ''.join(matriz[row + i][col] for i in range(4))
                if control_sequence(secuencia):
                    return True

    # Verifica si hay secuencias iguales en forma diagonal (de izquierda a derecha)
    def valid_diagonal(matriz):
        for row in range(rows - 3):
            for col in range(cols - 3):
                secuencia = ''.join(matriz[row + i][col + i] for i in range(4))
                if control_sequence(secuencia):
                    return True

    # Verifica si hay secuencias iguales en forma diagonal (de derecha a izquierda)
    def valid_reverse_diagonal(matriz):
        for row in range(rows - 3):
            for col in range(3, cols):
                secuencia = ''.join(matriz[row + i][col - i] for i in range(4))
                if control_sequence(secuencia):
                    return True

# Ejemplo de matriz 6x6
dna_ejemplo = [
    "AAAACG",
    "CCTTGC",
    "AAAAAT",
    "TTGCTG",
    "CGCTCC",
    "AATAAA"
]
# Resultado final
result = isMutant(dna_ejemplo)
print(result)