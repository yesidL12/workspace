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

// ForEach // para mostrar en consola

carrito.forEach(producto =>  console.log(producto));


// map //Para crear un nuevo arreglo

carrito.map(producto => console.log(producto));