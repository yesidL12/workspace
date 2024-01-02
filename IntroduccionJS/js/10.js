// Objetos

const nombreproducto = "Monitor 20 oulgadas";
const precio = 300;
const disponible = true;


const producto = {
    nombreproducto : "Monitor 20 pulgadas",
    precio : 300,
    disponible : true,
}

console.log(producto);

console.log(producto.precio); //Para acceder a algo especifico del objeto
console.log(producto.nombreproducto);
console.log(producto.disponible);

console.log(producto["precio"]);