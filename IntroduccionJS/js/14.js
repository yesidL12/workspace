// Arreglos o Arrays
// Sirven para agrupar elementos del mismo tipo o relacionados
// Util para los carritos de compras

const numeros = [10,20,30,40,50];

console.table(numeros);

const meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo"];

console.table(meses);


// // Acceder a los valores de un arreglo
// console.log(numeros[4]);

// // Conocer la exencion de un arreglo
// console.log(meses.length);

// meses.forEach( function(numero) {
//     console.log(numero);
// })

numeros[5] = 60; // Si se agraga una posición que no existe, lo agrega al final

numeros.push(60); // .push lo que hace es agregar un elemento al final del arreglo
numeros.unshift(-10,-20,-30); // . unshift agrega datos al inicio del arreglo

console.table(numeros);

// const meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo"];

// meses.pop(); // Elimina el último elemento
// meses.shift(); // Elimina el primer elemento

// meses.splice(2,1);
// console.table(meses);

// Rest operator o Spread Operator

const nuevoArreglo = [...meses, "junio"];
console.log(nuevoArreglo);