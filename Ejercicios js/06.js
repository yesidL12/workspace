// FizzBuzz

function FizzBuzz(numero) {
    if (numero % 3 === 0 && numero % 5 === 0) {
        return 'FizzBuzz'
    }else if (numero % 5 === 0) {
        return 'Buzz'
    }else if (numero % 3 === 0) {
        return 'Fizz'
    } else {
        return numero
    }
}

console.log(FizzBuzz(6))
console.log(FizzBuzz(20))
console.log(FizzBuzz(30))
console.log(FizzBuzz(8))