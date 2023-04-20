19.04

Lektrion1

1. Geben Sie für jeden der folgenden Pfade an, ob es sich um einen absoluten der relativen Pfad
handelt:

/home/user/Downloads  -  absolut
../Reports  -  relativ
/var  -  absolut
docs  -  relativ
/  - absolut

2. frage so lang die copy paste ich heir net rein

antwort : . .. rules.d udev.conf

3.Geben Sie den jeweils kürzesten Befehl an:

◦ Ihr aktueller Standort ist root (/). Geben Sie den Befehl an, mit dem ins Verzeichnis
lost+found im Verzeichnis home gelangen (Beispiel):

anwort: $ cd home/lost+found

◦ Ihr aktueller Standort ist root (/). Geben Sie den Befehl an, mit dem Sie ins Verzeichnis
/etc/network/ gelangen.

anwort: $ cd etc/network

◦ Ihr aktueller Standort ist /home/user/Documents/. Geben Sie den Befehl an, mit dem Sie
ins Verzeichnis /etc/ gelangen.

anwort: $ cd /etc

◦ Your current location is system. Navigate to the directory named user:

anwort: $ cd /home/user

4Betrachten Sie die folgenden Befehle:
$ pwd
/etc/udev/rules.d
$ cd ../../systemd/user
$ cd ..
$ pwd

Wie lautet die Ausgabe des letzten pwd Befehls?

antwort: /etc/systemd


Lektion2

aufgabe1
◦ Welcher Befehl wechselt ins Verzeichnis network unabhängig vom aktuellen Standort?

antwort: cd /etc/network

◦ Welchen Befehl kann user eingeben, um von /etc/udev ins Verzeichnis Documents zu
wechseln? Geben Sie den kürzestmöglichen Pfad an.

antwort: cd ~/Documents

◦ Welchen Befehl kann user eingeben, um in das Verzeichnis music des Benutzers michael
zu wechseln? Nutzen Sie den kürzestmöglichen Pfad.

antwort: cd ~michael/Music


aufgabe2

◦ Welche Datei steht zu Beginn, wenn Sie den Befehl ls -lrS ausführen?

antwort: scary.jpg

◦ Bitte beschreiben Sie, welche Ausgabe Sie von dem Befehl ls -ad */ erwarten.

antwort: alle verzeichnisse auch die versteckten aber ohne deren inhalt