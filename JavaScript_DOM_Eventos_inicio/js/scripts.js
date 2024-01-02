// querySelector
const heading = document.querySelector(".header__texto h2") // Retorna 0 a 1 Elemntos
console.log(heading);


//querySelectorALl
const enlaces = document.querySelectorAll(`.navegacion a`);
enlaces[0].textContent = `Nuevo Texto para Enlace`
enlaces[0].classList.add(`nueva-clase`);
// enlaces[0].classList.remove(`navegacion__enlace`);

// Generar un nuevo enlace con codigo de js
const nuevoEnlace = document.createElement(`A`);

// Agregar el href
nuevoEnlace.href = `nuevo-enlace.html`;

//Agregar el texto
nuevoEnlace.textContent = `Un Nunevo Enlace`;

// Agregar la clase
nuevoEnlace.classList.add(`navegacion__enlace`);

// Agregarlo al documento
const navegacion = document.querySelector(`.navegacion`);
navegacion.appendChild(nuevoEnlace);



console.log(nuevoEnlace);



// Eventos

// console.log(1);

// window.addEventListener(`load`, function () { // load espera a que el JS y los archivos que dependel del HTML estén listos
//     console.log(2);
// });

// window.onload = function () {
//     console.log(3);
// }

// document.addEventListener(`DOMContentLoaded`, function () { //Solo espera que se descargue el HTML, pero no espera CSS o imagenes
//     console.log(4);
// })

// console.log(5);



// window.onscroll = function (evento) {
//     console.log(evento);
// }


// Seleccionar elementos y asociarles un evento
// const btnENviar = document.querySelector(`.boton--primario`);
// btnENviar.addEventListener(`click`, function (evento) {
//     console.log(evento);
//     evento.preventDefault(); // util para formularios

//     // validar un formulario
//     console.log(`Enviando formulario`);
// });

// Eventos de los inputs o text area

const datos = {
    nombre: ``,
    email: ``,
    mensaje : ``
}

const nombre = document.querySelector(`#nombre`);
const email = document.querySelector(`#email`);
const mensaje = document.querySelector(`#mensaje`);
const formulario = document.querySelector(`.formulario`);

nombre.addEventListener(`input`, leerTexto);
email.addEventListener(`input`, leerTexto);
mensaje.addEventListener(`input`, leerTexto);

// el evento de submit
formulario.addEventListener(`submit`, function (evento) {
    evento.preventDefault();

    // validar el formulario

    const { nombre, email, mensaje } = datos;

    if (nombre === '' || email === '' || mensaje === '') {
        mostrarAlerta('Todos los campos son obligatorios', true );
        

        return; //Corta la ejecución del codigo
    } 

    //crear la alerta de enviar correctamente
    mostrarAlerta('Mensaje enviado correctamente');

});

function leerTexto(e) {
    // console.log(e.target.value);
    datos[e.target.id] = e.target.value;

    // console.log(datos);
}

function mostrarAlerta(mensaje, error = null) {
    const alerta = document.createElement('P');
    alerta.textContent = mensaje;

    if (error) {
        alerta.classList.add('error');
    } else {
        alerta.classList.add('correcto');
    }

    formulario.appendChild(alerta);

        //Desaparezca despues de 5 seg
        setTimeout(() => {
            alerta.remove();
        }, 5000);
} 