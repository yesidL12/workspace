// Imprimir un arreglo

function imprimirArreglo(arreglo) {
    // Iterar sobre cada elemento del arreglo
    for (let i = 0; i < arreglo.length; i++)
        // Imprimir cada elemento en una linea aparte
        console.log(arreglo[i]);
}

// Ejemplo de uso
const miArreglo = [1, "Hola", 2, "Mundo"];
imprimirArreglo(miArreglo);
