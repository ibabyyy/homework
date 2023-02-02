//1. Schreiben Sie ein JavaScript-Programm,
// um den Flächeninhalt eines Dreiecks zu ermitteln, dessen drei Seitenlängen a, b, c sind
const a = 5
const b = 3
const c = 7

function DreieckFläche(a, b, c) {
    console.log(Math.sqrt((a+b+c)*(-a+b+c)*(a-b+c)*(a+b-c)))*0.25
    return
}
    
DreieckFläche(a, b, c)

//2. Schreiben Sie ein JavaScript-Programm, 
//um den String 'Techstarter' periodisch alle 2 Sekunden auf die Konsole anzuzeigen.
//const d = "Techstarter"
var i = 0
var interval = setInterval(function(){
    console.log("Techstarter")
    i++;
    if(i>=5) {
            clearInterval(interval); //!Hab Stop nach 5x Widerholung eingebaut!
        }
}, 2000);

console.log(interval)

//3. Schreiben Sie ein JavaScript-Programm, 
//um die Differenz zwischen einer gegebenen Zahl und 13 zu erhalten, 
//wenn die Zahl größer als 13 ist, geben Sie die doppelte absolute Differenz zurück.

const d = 15
function Checknumber(d) {
    if (d<=13) {
        e = (13-d)
        return e
    }
    else {
        f = (d-13)*2
        return f
    }
}

console.log(Checknumber(d))

//4. Schreiben Sie ein JavaScript-Programm,
//um zu prüfen, ob zwei gegebene Integer-Werte im Bereich 50..99 (einschließlich) liegen.
//Geben Sie wahr zurück, wenn einer von ihnen in dem genannten Bereich liegt.

const g = 101
const k = 55
function CheckIfNumberBetween(g, k) {
    if (g>=50 && g<=99 || k>=50 && k<=99) {
    return ("true")
    }
    else {
        return ("false") //hab ein false eingebaut weil in der aufgabe net beschrieben war was passieren soll wenns nicht zutrifft
    }
}

console.log(CheckIfNumberBetween(g, k))

//5. Schreiben Sie ein JavaScript-Programm, um jedes n-te Element in einem gegebenen Array zu erhalten

const array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
var nth = 4

const every_nth = (array, nth) => array.filter((e, i) => {
    return i % nth === nth - 1
});

console.log(every_nth(array, nth))


//6. Schreiben Sie ein JavaScript-Programm, um herauszufinden,
//ob ein Wort ein Palindrom ist, oder nicht. (z. B. Madam, Anna, Otto)

//7. Schreiben Sie eine JavaScript-Funktion, die alle Kombinationen eines Strings generiert.
//Example string: 'dog'; Expected Output: d,o,do,g,dg,og,dog.

//8. Schreiben Sie ein JavaScript-Programm, um die nicht eindeutigen Werte in einem Array herauszufiltern.
// (Beispiel-Array: [1, 2, 2, 3, 4, 4, 5]).
// hab lange rumprobiert ohen erfolg, dann hab ich gegoogelt und den code für mich angepasst.
const arraytwo = [ 5, 3, 4, 2, 3, 7, 5, 6 ];
 
const findDuplicates = arraytwo => {
    return arraytwo.filter((item, index) => {
        return arraytwo.indexOf(item) !== index;
    });
}
const duplicates = findDuplicates(arraytwo);
console.log(duplicates);

//9. Schreiben Sie eine JavaScript-Funktion, um das erste Element eines Arrays abzurufen.
// Das Übergeben eines Parameters 'n' gibt die ersten 'n' Elemente des Arrays zurück.
//Test Data :
//console.log(first([7, 9, 0, -2]));
//console.log(first([],3));
//console.log(first([7, 9, 0, -2],3));
//console.log(first([7, 9, 0, -2],6));
//console.log(first([7, 9, 0, -2],-3));

//Expected Output :
//7
//[]
//[7, 9, 0]
//[7, 9, 0, -2]
//[]

//10. Schreiben Sie ein JavaScript-Programm, um ein Array zu mischen.
// hab ich auch net hinbekommen hab nen code dann genommen und wollte den irgendwie anpassen,
//dass es zumindest geht aber ging net
var arrayz = new Array(0, 1, 2, 3, 4, 5, 6, 7, 8, 9);

var ausgabe = arrayz.join(", ");



class arrayShuffle {
    constructor() {
        var tmp, rand;
        for (var i = 0; i < this.length; i++) {
            rand = Math.floor(Math.random() * this.length);
            tmp = this[i];
            this[i] = this[rand];
            this[rand] = tmp;
        }
    }
}
  
  Array.prototype.arrayz =arrayShuffle;
