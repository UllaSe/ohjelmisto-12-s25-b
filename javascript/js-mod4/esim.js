'use strict';

console.log('the script starts');

// esimerkki materiaalista
function synchronousFunction() {
    let number = 1;
    for (let i = 1; i < 100000; i++) {
        number += i;
        console.log('synchronousFunction running');
    }
    console.log('regular function complete', number);
}

async function asynchronousFunction() {                 // asynchronous function is defined by the async keyword
    console.log('asynchronous download begins');
    try {                                               // error handling: try/catch/finally
        const response = await fetch('https://api.chucknorris.io/jokes/random');    // starting data download, fetch returns a promise which contains an object of type 'response'
        const jsonData = await response.json();          // retrieving the data retrieved from the response object using the json() function
        console.log(jsonData.value);    // log the result to the console
        document.querySelector('.output').textContent = jsonData.value;
    } catch (error) {
        console.log(error.message);
    } finally {                                         // finally = this is executed anyway, whether the execution was successful or not
        console.log('asynchronous load complete');
    }
}

//synchronousFunction();
asynchronousFunction();

// pics.json latausesimerkki

// oldschool promisen käsittely (toimii, mutta ei suositella)
fetch('pics.json').then(function (data) {
    console.log('response data: ', data);
    data.json().then(function (data) {
        console.log('json data', data);
        // tänne koodi, millä käsitellään ladattu json data
    }).catch(function (error) {
        console.error(error);
    });
}).catch(function (error) {
    console.error(error);
});

// suositeltu moderni tapa (await-async)
async function fetchPics(){
    const picsDiv = document.querySelector('#pics');
    try {
        const response = await fetch('pics.json');
        //console.log('response status', response.status, response.statusText, response.ok);
        // testataan ettei 404 yms. virhettä
        if (!response.ok) {
            throw new Error('response status no ok');
        }
        const pics = await response.json();
        console.log('pics', pics);
        for (const pic of pics) {
            const imgElem = document.createElement('img');
            imgElem.src = pic.address;
            imgElem.alt = pic.description;
            picsDiv.append(imgElem);
        }
    } catch (error) {
        console.log(error);
        picsDiv.innerHTML = '<p>Kuvien lataamisessa ongelma</p>'
    }
}

// nappula kuvien hakemiseen
document.querySelector('button').addEventListener('click', function () {
    fetchPics();
});

// tv maze esimerkki

// Datan haku, asynkroninen funktio
async function searchTVMaze(searchString) {
    // TODO: lisää virheenkäsittely
    const response = await fetch('https://api.tvmaze.com/search/shows?q=' + searchString);
    const results = await response.json();
    console.log('tv maze results', results);
    // tulokset voisi lisätä DOMiin tässä
    return results;
}

// Hakulomakkeen käsittelijä
const searchForm = document.querySelector('form#tvmaze');
const inputText = searchForm.querySelector('input');
// eventinkäsittelijä on määritelty async, koska funktiossa käytetetään await:ia
searchForm.addEventListener('submit', async function(event) {
    event.preventDefault();
    if (inputText.value.length > 1 ) {
        // hakufunktio on asynkroninen, joten se palauttaa promisen, joka pitää käsitellä await:illa
        const tvMazeResults = await searchTVMaze(inputText.value);
        // haun tulokset
        console.log('event handler hakutulokset', tvMazeResults);
        // tulokset voisi lisätä DOMiin tässä
    }
});



console.log('the script ends');