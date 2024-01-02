// for loop

// for(let i = 0; i < 10; i++) {
//     console.log(i);
// }

// for(let i = 0; i <= 100; i++) {
//     if(i% 2 === 0) {
//         console.log(`EL número ${i} es PAR`);
//     } else{
    // console.log(`El número ${i} es IMPAR`);
//         }
//     }
// }

const carrito = [
    {nombre: "Monitor 20 pulgadas", precio:500},
    {nombre: "Televisión 50 Pulgadas", precio:700},
    {nombre: "Tablet", precio:300},
    {nombre: "Audifonos", precio:200},
    {nombre: "Teclado", precio:50},
    {nombre: "Celular", precio:500},
    {nombre: "Bocinas", precio:300},
    {nombre: "Laptop", precio:800},
];

for(let i = 0; i < carrito.length; i++ ) {
    console.log(carrito [i].nombre);
}

// while loop

let i = 1; // Indice

while( i <= 100) { //condición


    if(i % 2 === 0){
        console.log(`El número ${i} es PAR`)
    }else{console.log(`El número ${i} es IMPAR`)}
    i++; // Incremento
}

// Do while loop

let i = 0;

do{
    console.log(i);


    i++;
} while(i < 10);

// La diferencia entre el while loop y el  do while es que en el while evalua la condicion y si no es verdadera no ejecuta el codigo, 
//pero en el do while ejecuta el codigo al menos una vez y despues evalua
