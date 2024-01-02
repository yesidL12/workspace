// Arrow function

const sumar2 = (n1, n2) => console.log(n1 + n2)
sumar2(5,20)


const aprendiendo = tecnologia => console.log(`Aprendiendo ${tecnologia}`)
aprendiendo(`Javascript`)


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
meses.forEach( mes => {
    if(mes == "Marzo") {
        console.log("Marzo si existe");
    }
}); 


let resultado;
//Some ideal para arregle de objetos
resultado = carrito.some(producto => producto.nombre === "Celular")

//reduce
resultado = carrito.reduce(total,producto => total + producto.precio, 0);


// Filter
resultado = carrito.filter(producto => producto.precio <400)
console.log(resultado);

