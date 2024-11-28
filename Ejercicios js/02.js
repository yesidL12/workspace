// Calcular Impuestos

function calcularImpuestos(edad, ingresos) {
    if (edad >= 18 && ingresos >= 1000) {
        return ingresos * 0.40
    } else {
        return 0
    }
}

console.log(calcularImpuestos(18, 1000))