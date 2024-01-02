// Objetos
const producto = {
    nombreproducto : "Monitor 20 pulgadas",
    precio : 300,
    disponible : true,
}

//forma anterior
const precioProducto = producto.precio;

console.log(precioProducto);
console.log(nombreProducto);



//Destructuring de objetos
const {precio} = producto;
const {nombreProducto} = producto;

console.log(producto);
