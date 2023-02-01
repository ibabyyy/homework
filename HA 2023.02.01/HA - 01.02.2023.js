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
function CheckIfNumberBetween(g) {
    if (g>=50 && g<=99 || k>=50 && k<=99) {
    return ("true")
    }
    else {
        return ("false") //hab ein false eingebaut weil in der aufgabe net beschrieben war was passieren soll wenns nicht zutrifft
    }
}

console.log(CheckIfNumberBetween(g))

//5. Schreiben Sie ein JavaScript-Programm, um jedes n-te Element in einem gegebenen Array zu erhalten

//.filter




//6. Schreiben Sie ein JavaScript-Programm, um herauszufinden,
//ob ein Wort ein Palindrom ist, oder nicht. (z. B. Madam, Anna, Otto)