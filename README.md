# DESAFÍO: MUTANTES
Programación I - Desafío Mercado Libre
### Datos Personales:
* Nombre y Apellido: Giuliana Fragapane
* Legajo: 51529
* Email: giulianafragapanepravatta@gmail.com
## Proyecto
* Consigna:
<p align="justify">
Magneto quiere reclutar la mayor cantidad de mutantes para poder luchar contra los X-Mens. Te contrata para que desarrolles un proyecto que detecte si un humano es mutante basándose en su secuencia de ADN, utilizando la siguiente función: boolean isMutant(String[] dna), donde recibirás como parámetro un array de Strings que representan cada fila de una tabla de (6x6) con la secuencia del ADN. Ingrese por teclado las filas de la matriz, cargando las mismas.

Las letras de los Strings solo pueden ser: (A,T,C,G), las cuales representan cada base nitrogenada del ADN.
Sabrás si es mutante si encuentras MÁS DE UNA SECUENCIA de cuatro letras iguales, de forma oblicua (de derecha a izquierda y viceversa), horizontal o vertical.

#### Ejemplo (Caso mutante):
String[] dna = {"ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"};
En este caso el llamado a la función isMutant(dna) devuelve “True”.

Desarrolla el algoritmo de la manera más eficiente posible.
</p>

## Abordaje
* Lenguaje implementado: Python
### Algoritmo
- Definí la función solicitada (isMutant) dentro de la cual cree otras funciones en relación a las formas de búsqueda (horizontal, vertical y oblicua).
- Consideré estructuras para evitar en mu

## Cómo correrlo
Cómo tiene que correrlo el profe desde bash
Para ejecutar el proyecto es necesario 
``` 
print(codigo)
```