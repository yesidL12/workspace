// Array Methods

const meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo"];

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

//forEach
meses.forEach(function(mes) {
    if(mes == "Marzo") {
        console.log("Marzo si existe");
    }
}); 

// Includes
let resultado = meses.includes("Marzo");

//Some ideal para arregle de objetos
resultado = carrito.some(function (producto) {
    return producto.nombre === "Celular"
})

//reduce
resultado = carrito.reduce(function(total, producto){
    return total + producto.precio
}, 0);


// Filter
resultado = carrito.filter(function(producto){
    return producto.precio <400
})
console.log(resultado);