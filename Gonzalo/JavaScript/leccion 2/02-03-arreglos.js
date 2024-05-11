
//Creacion de array o arreglos
//let autos = new Array('Ferrari', 'Renault', 'BMW'); esta es la sintaxis vieja
const autos = ['Ferrari', 'Renault', 'BMW'];
console.log(autos);

//Recorremos los elementos de un arreglo
console.log(autos[0]);
console.log(autos[2]);

for(Let i = 0; i < autos.length; i++){
console.log(i+' : '+autos[i]);
}

//modificamos lo elementos del areglo
autos[1] = 'volvo';
console.log(autos[1]);

//Agregamos nuevos valores al arreglo
autos.push('audi'); // Agregamos el elemento al final del arreglo
console.log(autos);

//otras formas de agregar elementos al arreglo
autos[autos.length] = 'porche';
console.log(autos);

//tercera forma de agregar elementos teniendi Cuidado
autos[6] = 'Renault';
console.log(autos);

//como preguntar si es una Array o Arreglo
console.log(Array.isArray(autos)); // devuelve un booleano


console.log(autos instanceof Array); // Preguntamos si la variable es una instancia de la clase Array

