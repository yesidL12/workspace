let obj = {};
let obj2 = new Object();

/**
 * new Array();
 * new String();
 * new Number();
 * new Boolean ();
 */

function Usuario() {
    this.name = "Chanchito feliz";
}
let user = new Usuario();
console.log(user.constructor);