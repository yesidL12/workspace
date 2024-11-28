// IMC (indice de masa corporal)

function bmi(peso,altura) {
    let imc = peso / altura ^ 2
    if (imc >= 30) {
        return 'Obeso'
    }else if (imc >= 25 || imc <= 29.9) {
        return 'Sobrepeso'
    } else if (imc >=18.5 || imc <= 24.9) {
        return 'Normal' 
    } else if (imc <18.5) {
        return 'Bajo de peso'
    }
}

console.log(bmi(80, 1.78))