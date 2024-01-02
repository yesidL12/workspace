const usuarioAutenticado = new Promise((resolve , reject) => {
    const auth = true;
    
    if (auth) {
        resolve(`Usuario Autenticado`); // El promise se cumple
    } else {
        reject(`No se pudo iniciar seción`); // El promise no se cumple
    }
});

usuarioAuntenticado
    .then( resultado => console.log(resultado));
    .catch( error => console.log(error));



// EN los Promises existen 3 valores
// Pending: No se ha cumplido pero tampoco se ha rechazado
//Fulfilled: Ya se cumpló
// Rejected: SE ha rechazado o no se pudo cumplir