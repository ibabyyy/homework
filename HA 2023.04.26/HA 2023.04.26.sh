a) Das BashScript soll prüfen, ob die Datei /etc/resolv.conf vorhanden ist.
Wenn ja, soll das BashScript eine positive Rückmeldung mit `echo` ausdrücken.
Wenn nein, soll das Script dies ebenfalls erklären. 

#!/bin/bash

if [ -e "/etc/resolv.conf" ]; then
  echo " /etc/resolv.conf ist da. das ist eine positive ürckmeldung"
else
  echo "/etc/resolv.conf ist nicht vorhanden."
fi

b) Das BashScript soll prüfen, ob der Ordner /etc/default existiert.
Wenn ja, ob dort die Datei /etc/default/pam.conf existiert.
Wenn ja, soll das BashScript eine positive Rückmeldung mit `echo` an den User zurückgeben.
Wenn nein, soll das Script nach der Datei pam.conf suchen. Zeige die Ergebnisse auf der Konsole an. 

#!/bin/bash

if [ -d "/etc/default" ]; then
  if [ -e "/etc/default/pam.conf" ]; then
    echo "die datei /etc/default/pam.conf existiert."
  else
    echo "die datei /etc/default/pam.conf existiert nicht."
    find / -name "pam.conf" -print 2>/dev/null
  fi
else
  echo "der ordner /etc/default existiert nicht."
fi


c) Das BashScript soll ein Argument entgegen nehmen. 
Wenn das Argument eine Zahl ist, soll das Script sagen: "Das Argument ist eine Zahl". 
Wenn das Argument ein Wort ist, soll das Script eine entsprechende Anzeigen schalten. 

#!/bin/bash
echo "schreib irgendwas ich sage dir ob es eine zahl oder ein wort ist"
read argument

if [[ $1 =~ ^[0-9]+$ ]]; then
  echo "Das Argument ist eine Zahl."
else
  echo "Das Argument ist ein Wort."
fi


d) Das BashScript soll dich dazu auffordern, deinen Namen und dein Alter einzugeben,
sowie deine Lieblingstechnologie.
Das Script soll anschließend die Aussage "Ich bin ... und ich bin ... Jahre alt. 
Meine Lieblingstechnologie ist ..." auf die Konsole printen.

#!/bin/bash

echo "wie heist du:"
read name
echo "wie alt bist du:"
read alter
echo "was ist deine leiblignstechnologie:"
read liebling

echo "Ich heiße $name und bin $alter jahre alt. meine lieblingstechnologie ist $liebling.
