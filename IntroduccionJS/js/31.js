// Async // await

function descargarNuevosClientes() {
    return new Promise(resolve => {
        console.log(`Descargando CLientes... espere...`);

        setTimeout(() => {
            resolve(`Los CLientes fueron descargados`);
        }, 5000);
    });
}


function descargarUltimosPedidos() {
    return new Promise(resolve => {
        console.log(`Descargando Pedidos... espere...`);

        setTimeout(() => {
            resolve(`Los Pedidos fueron descargados`);
        }, 3000);
    });
}


async function app() {
    try {
        // const clientes = await descargarNuevosClientes();
        // const Pedidos = await descargarUltimosPedidos();
        // console.log(clientes); 
        // console.log(pedidos); 
        
        const resultado = await Promise.all([descargarNuevosClientes(), descargarUltimosPedidos()]);
        console.log(resultado[0]);
        console.log(resultado[1]);
    } catch (error) {
        console.log(error);
    };