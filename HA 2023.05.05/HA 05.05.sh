HA 05.05.2023
3.3 Lektion1

1. Der Benutzer gibt Folgendes in seine Shell ein:
$ PATH=~/scripts
$ ls
Command 'ls' is available in '/bin/ls'
The command could not be located because '/bin' is not included in the PATH environment
variable.
ls: command not found

◦ Was hat der Benutzer gemacht?

◦ Welcher Befehl kombiniert den aktuellen Wert von PATH mit dem neuen Verzeichnis
~/scripts?

2. Betrachten Sie das folgende Skript. Beachten Sie, dass es elif verwendet, um nach einer
zweiten Bedingung zu suchen:
> /!bin/bash
> fruit1 = Apples
> fruit2 = Oranges
if [ $1 -lt $# ]
then
echo "This is like comparing $fruit1 and $fruit2!"
> elif [$1 -gt $2 ]
then
> echo '$fruit1 win!'
else
> echo "Fruit2 win!"
> done

◦ Die mit einem > markierten Zeilen enthalten Fehler. Beheben Sie die Fehler.

#!/bin/bash
fruit1="Apples"
fruit2="Oranges"
if [ $1 -lt $# ]
then
    echo "This is like comparing $fruit1 and $fruit2!"
elif [ $1 -gt $2 ]
then
    echo "$fruit1 wins!"
else
    echo "$fruit2 wins!"
fi


3. Was wird in den folgenden Situationen ausgegeben?

$ ./guided1.sh 3 0   - $fruit1 wins!

$ ./guided1.sh 2 4  - This is like comparing Apples and Oranges!

$ ./guided1.sh 0 1   -This is like comparing Apples and Oranges!



3.3 Lektion2

1. Lesen Sie das folgende script1.sh:
#!/bin/bash
if [ $# -lt 1 ]
then
echo "This script requires at least 1 argument."
exit 1
fi
echo $1 | grep "^[A-Z]*$" > /dev/null
if [ $? -ne 0 ]
then
echo "no cake for you!"
exit 2
fi
echo "here's your cake!"
exit 0

Wie lautet die Ausgabe der folgenden Befehle?
◦ ./script1.sh

◦ echo $?

◦ ./script1.sh cake

◦ echo $?

◦ ./script1.sh CAKE

◦ echo $?

2. Lesen Sie das folgende Skript script2.sh:
for filename in $1/*.txt
do
cp $filename $filename.bak
done

Beschreiben Sie den Zweck des Skripts so, wie Sie es verstehen.

das sucht nach dateien mit txt endung und kopiert die datei dann aber anstatt .txt mit der endung .bak