const boton = document.querySelector("#boton");

boton.addEventListener(`click`, function () {
    Notification.requestPermission()
        .then(resultado => console.log(`El resultado es ${resultado}`))
})



if (Notification.permission == `grantes`) {
    new Notification(`Esta es una notificación`, {
        icon:
        body: (`Codigo con Juan, los mejores tutoriales`)
    })
}