// short-circuit

//Falso

// false
// 0
//''
//undefined
//NaN
let nombre = 'Chanchito feliz';
let username = nombre || 'Anonimo';
console.log(username);

function fn1() {
    console.log('soy funcion 1');
    return true;
}
function fn2() {
    console.log('soy funcion 2');
    return true;
}
