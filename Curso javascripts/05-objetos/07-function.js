function Punto(x, y) {
    this.x = x;
    this.y = y;
    this.dibujar = function() { console.log("Dibujando...");}
}

let punto = { z: 7};
Punto.call({}, 1, 2);

console.log(punto);
// const Point = new Function("x" , "y", ` 
// this.x = x;
// this.y = y;
// this.dibujar = function() { console.log("Dibujando...");}`);

// const P = new Point(1,2);
// console.log(p);