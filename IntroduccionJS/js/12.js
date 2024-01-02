// "use strict"; //Correr JS en modo estricto
// Objetos
const producto = {
    nombreproducto : "Monitor 20 pulgadas",
    precio : 300,
    disponible : true,
}


Object.freeze(producto); //Object.freeze no permiti agregar, eliminar o modificar el elemento //Object. seal  si permite modificar pero no eliminar ni agregar


producto,imagen = "imagen.jpg";

console.log(Object.isFrozen(producto));


console.log(producto);