const user = { id: 1 };

user.name = 'Nicolas';
user.guardar = function () {
    console.log('Guardando', user.name);
}

user.guardar();

delete user.guardar; // delete para borrar
delete user.guardar;
console.log(user);

const user1 = Object.freeze({ id: 1 }); // SE ultiliza para que no se pueda modificar el objeto
const usr1 = object.seal({ id: 1 }); // Se utiliza para modificar los valores pero nos las propiedades del objeto

