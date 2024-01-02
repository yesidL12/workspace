// POO

//Object Literal
const producto = {
    nombre: `Tablet`,
    precio: 500
}

// Object Constructor
function Producto(nombre, precio,Disponible) {
    this.nombre = nombre;
    this.precio = precio;
    this.Disponible = Disponible;
}
// EL prototyphe nos va a permitir crear funciones que solo se utilizan en un objeto especifico.
Producto.prototype.formatearProducto = function() {
    return ` EL Producto${this.nombre} tiene un precio de: $ ${this.precio}`;
}

const producto2 = new Producto(`Monitor Curvo de 49"`, 8000 , true);
const producto3 = new Producto(`Laptop`, 300, false);


console.log(producto2.formatearProducto());
console.log(producto3.formatearProducto());


