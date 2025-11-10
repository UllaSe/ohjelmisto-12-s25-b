'use strict';

// hae viittaus kaikkiin output class elementteihin taulukkona
const outputElements =
    document.getElementsByClassName('output');
console.log(outputElements);

// viittaus yhteen elementtiin id:n perusteella
const outputElement2 =
    document.getElementById('output');
console.log(outputElement2);

// viittaus kaikkiin p-elementteihin tagin perusteella
const outputElement3 =
    document.querySelectorAll('p');
console.log(outputElement3)

// viittaus koko body-elementtiin
const body = document.querySelector('body');
body.querySelector('#output');

// Listan (ul) käsittely
const ulElement = document.querySelector('ul');
const newLi = document.createElement('li');
ulElement.appendChild(newLi);
newLi.textContent = 'Uusi itemi';

// innerHTML-esimerkki
//ulElement.innerHTML = '<li>uusi itemi</li><li>Toinen uusi</li>';

// haetaan viittaus kaikkiin li-elementteihin listan sisällä
const liElems = ulElement.querySelectorAll('li');
for (let i = 0; i < liElems.length; i++) {
    // muutetaan jokaisen li-elementin sisältöä perustuen taulukon indeksin arvoon
    liElems[i].textContent = `${i + 1}. itemi`;
}

// luodaan html-lista, jossa sisältö js-taulukosta
const inventory = ['kynä', 'kumi', 'läppäri', 'reppu'];
const inventoryOlElem = document.createElement('ol');
for (const item of inventory) {
    // luodaan html li-elementit ja sijoitetaa ol-elementi lapsiksi
    const liElem = document.createElement('li');
    liElem.textContent = item;
    inventoryOlElem.appendChild(liElem);
}
// lisätään luotu lista DOMiin käyttäen aiemmin haettu viittausta body-elementtiin
const inventoryHeader = document.createElement('h2');
inventoryHeader.textContent = 'Inventaario';
body.appendChild(inventoryHeader);
body.appendChild(inventoryOlElem);
inventoryHeader.classList.add('red');

// Tapahtumankäsittely

const button = document.querySelector('button');
// sidotaan tapahtuma ja tapahtumankäsittelijä yhteen
button.addEventListener('click', buttonClick);

// erillinen tapahtumankäsittelyfunktio
function buttonClick() {
    console.log('nappulaa klikattu');
}

// nimetön funktio tapahtumankäsittelijänä
inventoryHeader.addEventListener('click', function () {
    console.log('otsikkoa klikattu');
    inventoryHeader.classList.toggle('red');
});

// näppis-tapahtumaesimerkki
let inputString = '';
document.addEventListener('keypress', function (event) {
    //console.log('näppäintä painettu', event);
    inputString += event.key;
    if (event.key === 'Enter') {
        outputElement2.classList.remove('blue');
        outputElement2.classList.add('red');
    }
    //outputElement2.classList.add('blue');
    outputElement2.textContent = 'nappeja painettu: ' + inputString;
});

// hiiritapahtuma
document.addEventListener('mousemove', function (event) {
    //console.log('hiiri liikkuu', event);
    outputElements[0].textContent = `Hiiren sijainti: ${event.clientX}, ${event.clientY}`;
});

// estetään linkin oletustapahtuma
document.querySelector('a').addEventListener('click', function (event) {
    event.preventDefault();
    console.log('linkki klikattu, mutta se ei päivitä sivua');
});

// lomakkeen käsittely, lisätään asioita aiemmin luotuun inventaarioon
const addForm = document.querySelector('form');
const inputText = addForm.querySelector('input');
addForm.addEventListener('submit', function(event) {
    event.preventDefault();
    if (inputText.value.length < 3) {
        return;
    }
    const liElem = document.createElement('li');
    liElem.textContent = inputText.value;
    // lisätään asia myös js-taulukkoon (ei kuitenkaan käytetä tässä mihinkään)
    inventory.push(inputText.value);
    console.log('muistissa oleva inventaario', inventory);
    inventoryOlElem.appendChild(liElem);
    inputText.value = '';
});
