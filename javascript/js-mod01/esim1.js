/**
Tässä tiedostossa on ensimmäisiä JavaScript-esimerkkejä
*/
'use strict'; // muista käyttää aina tiedoston alussa

// Käytä const-avainsanaa muuttujan esittelyyn, paitsi jos sen arvoa
// tarttee myöhemmin muuttaa
let teksti = 'Moi maailma!'

console.log(teksti);
teksti = 'Moi Joku';
// Selaimen oma alert-ikkuna (popup)
//alert('Kukkuu!!');
document.querySelector('.output').textContent = teksti;

let name = 'Matti';
let age = 23;
let greeting = `Moi ${name}, ${age} v!`;
console.log(greeting);

// syötteen lukeminen
name = prompt('Anna nimesi:');
//console.log('käyttäjän syöte', userInput);
age = parseInt(prompt('Anna ikäsi:'));

if (10 < age && age < 100) {
    greeting = `Moi ${name}, ikäsi vuoden päästä ${age + 1} v!`;
    document.querySelector('.output').textContent = greeting;
} else {
    console.log('Olet liian nuori tälle sivulle.');
}

// Math-luokka
// noppaesimerkki 1-6
const result =  Math.ceil(Math.random()*6);
console.log('nopanheitto', result);

switch (result) {
    case 6:
        console.log('Voitit 100 e');
        break;
    case 5:
        console.log('Voitit 50 e');
        break;
    case 4:
        console.log('voitit 20 e');
        break;
    default:
        console.log('et voittanut mitään');
}

