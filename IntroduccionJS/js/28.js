// Classes


class Producto {
    constructor(nombre, precio) {
        this.nombre = nombre;
        this.precio = precio;
    }

    formatearProducto() {
        return ` EL Producto ${this.nombre} tiene un precio de: $ ${this.precio}`;
    }

    formatearPrecio() {
        return `El precio de ${this.nombre} es de: $${this.precio}`;
    }
}

const producto2 = new Producto(`Monitor Curvo de 49"`, 8000 , true);
const producto3 = new Producto(`Laptop`, 300, false);

//Herencia
 
class Libro extends Producto {
    constructor(nombre, precio, isbn) {
        super(nombre, precio);
        this.isbn = isbn;
    }

    formatearProducto() {
        return `${super.formatearProducto()} y su ISBN es ${this.isbn}`;
    }
}


const libro = new Libro(`JavaScript la Revolución`, 120, `910313981389139`);
console.log(libro.formatearProducto());

console.log(producto2.formatearProducto());