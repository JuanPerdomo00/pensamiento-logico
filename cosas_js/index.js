// Funcion en javascript
function segundoNumeroGrande(numero) {
    let primero = numero[0];
    let segundo = 0;

    for(let i = 0; i < numero.length; i++) {
        if(numero[i] > primero) {
            segundo = primero;
            primero = numero[i];
        } 
        if (numero[i] > segundo && numero[i] < primero) {
            segundo = numero[i];   
        }
    }
        return segundo;
}

let num = [1,8,7,6,5,9,12,2,11,2]

console.log(segundoNumeroGrande(num))