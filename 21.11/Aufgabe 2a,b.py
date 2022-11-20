#AUFGABE2

#(a) Das Python-Programm zur Buchstabenverschiebung funktioniert nicht, wenn man z.B.   
#zeichen = 'T' und schluessel = 10 vorgibt. Teste und begründe.

#ERGEBNIS: es geht nicht weil er den + faktor auf die gesamte ascii tabelle macht, und nicht nur auf a-z


#(b) Ändere das Python-Programm zur Buchstabenverschiebung so ab, dass es für alle      
#sinnvollen Vorgaben zeichen = ... und schluessel = ... korrekt funktioniert.

#Ergebnis:



zeichen = 'p'
schluessel = 7
zahl = ord(zeichen)
neueZahl = zahl + schluessel
neuesZeichen = chr(neueZahl)
print(neuesZeichen)