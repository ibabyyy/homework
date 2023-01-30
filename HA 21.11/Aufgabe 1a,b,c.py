#Aufgabe 1
#(a) Entschlüssele die in der Abbildung gezeigte Antwort von Asterix.   (a) Ergebnis: HALLO CAESAR WIR HABEN DEIN VERSCHLUESSELUNGSVERFAHREN GEKNACKT  (MAIN1 siehe unten)

#(b) Entschlüssele die Nachricht: Surjudpplhuxqj lvw hlqidfk qxu phjd jxw.            (b) Ergebnis: programmierung ist einfach nur mega gut (MAIN1 siehe unten)

#(c) Verschlüssele analog eine selbst gewählte Nachricht. Benutze jetzt eine          (c) Ergebnis:hssl thluuly ihzl klmmlu / alle maenner base deffen (MAIN2 siehe unten)
#    Alphabetverschiebung um 7 Zeichen, die 'A' durch 'H' ersetzt 
#    ('B' durch 'I', 'C' durch 'I').



#convert letters to ascii code and store in list
def convertascii(code):
    a = [ord(i) for i in code]
    
    return(a)

#convert ascii code list to letters
def convert_ascii_to_code(my_ascii_list_added):
    a = [chr(i) for i in my_ascii_list_added]

    return(a)

#-----------------------------------MAIN 1------------------------

code = input("enter your code : ")

my_ascii_list = convertascii(code)

my_ascii_list_added = [x-3 for x in my_ascii_list]

print(convert_ascii_to_code(my_ascii_list_added))

#---------------------------------MAIN 2----------------------

code = input("enter your code : ")

my_ascii_list = convertascii(code)

my_ascii_list_added = [x+7 for x in my_ascii_list]

print(convert_ascii_to_code(my_ascii_list_added))