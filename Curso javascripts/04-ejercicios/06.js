/**
 * Crear algoritmo que devuelva cantidad
 * de números positivos de un array
 */

let array = [2, 5, 15, -100, 55];

function cuantosPositivos(array) {
    let cantidad = 0;
    for (elemento of arr) {
        if (elemento > 0) {
            cantidad++
        }
    }
    return cantidad;
}

let resultado = cuantosPositivos(array);
console.log(resultado);