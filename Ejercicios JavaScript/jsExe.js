// function minAndMax(numbers) {
//     let masMenos = 0
//     numbers.sort((a,b) => a - b)
//     const min = Math.min(...numbers)
//     const max = Math.max(...numbers)
//     masMenos = min + max
//     return masMenos
//   }

// console.log(minAndMax([4,6,9,-3,5,8]))

// function romanoAEntero(romano){
//   //crear un objeto con numeros romanos y sus valores numericos
//   const tablaRomanos = {
//     M: 1000,
//     CM: 900,
//     D: 500,
//     CD: 400,
//     C: 100,
//     XC: 90,
//     L: 50,
//     XL: 40,
//     X: 10,
//     IX: 9,
//     V: 5,
//     IV: 4,
//     I: 1
//   }

//   //variable para el resultado
//   let res = 0;
//   //recorrer numero romano letra a letra
//   for (let i = 0; i < romano.length; i++) {
//     console.log(tablaRomanos[romano[i]]);
//     if (i === romano.length - 1 || tablaRomanos[romano[i + 1]] <= tablaRomanos[romano[i]]) {
//       res += tablaRomanos[romano[i]]
//     }else{
//       res -= tablaRomanos[romano[i]]
//     }    
//     console.log(res);
    
//   }



//   return res
// }
// romanoAEntero("CXX");
// //romanoAEntero("CXX");

function esPalindromoV1(palindromo){
  const esPalindromo = palindromo.split("").reverse().join("")

  return ( esPalindromo === palindromo)
}

console.log(esPalindromoV1("ana"));

function esPalindromo(palindromo){
  //DIVIDIR LA CADENA DE TEXTO
  let vec = []
  for (let i = 0; i < palindromo.length; i++) {
    vec.push(palindromo[i]);    
  }

  let letrasInvertidas = []
  for (let i = vec.length - 1; i >= 0; i--) {
    letrasInvertidas.push(vec[i]);
  }
  let palabraInvertida = ""
  for (let i = 0; i < letrasInvertidas.length; i++) {
    palabraInvertida += letrasInvertidas[i];
    
  }

  return (palabraInvertida === palindromo)
}

console.log(esPalindromo("anuel"));
 