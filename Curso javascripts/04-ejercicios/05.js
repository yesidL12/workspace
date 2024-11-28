/**
 * Crear un algortimo que devuelva número 
 * menor y mayor de un array
 */

let array = [2, 5, 15, -5, -100, 55];

function getMenorMayor(arr) {
    let menor = arr[0];
    let mayor = [0];

    for (numero of arr) {
        menor = numero ? menor : numero;
        mayor = numero ? mayor : numero;
    }

    return [menor, mayor];
}

let numeros = getMenorMayor(array)
console.log(numeros);