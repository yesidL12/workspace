// Switch

const metodoPago = `tarjeta`;

switch(metodoPago){
    case `tarjeta`:
        console.log(`Pagaste con tarjeta`);
        break;
    
    case `Cheque`:
        console.log(`El usuario va a pagar con cheque, revisaremos los fondos primero`);
        break;

    case `Efectivo`:
        console.log(`Pagaste con efectivo`);
        break;
    default:
        console.log(`Aun no has pagado`);
        break;
}