# KARTUVĖS
Žaidimas "Kartuvės", kuriame galima spėlioti žodžius, kurie yra generuojami automatiškai iš tinklapio (šiuo atveju: https://lt.wikipedia.org/wiki/Telefonas).

Paleidimo instrukcija:
1. parsisiųskite visus failus;
2. įsirašykite trūkstamus python modulius, pagal requirements.txt failą;
3. atsidarykite grafiką.pyw kodo failą ir jį paleiskite;
4. grafinės sąsajos dešinėje pusėje esančiame įvedimo lange įvedę raidę ir paspaudę "ENTER" užfiksuosite savo spėjimą;
5. atspėjus visas raides Jūs laimėsite žaidimą;
6. neatspėjus visų žodžio raidžių galėsite bandyti iš naujo paspaudę meniu mygtuką "Naujas žodis".

Veikimo principas:
  Programa sudaryta iš dviejų kodo failų (grafika.pyw ir db_kurimas.py) ir grafinių elementų (paveikslėliai ir icona).
Paleidus grafika.pyw kodo failą atsiras vartotojo grafinė sasaja, kurios viršuje bus parodyti meniu elementai: "Naujas žodis"(programos paleidimas iš naujo 
ir naujo spėliojamo žodžio sugeneravimas); "Išeiti"(programos išjungimas). Grafinės sasajos kairėje pusėje patalpintas paveikslėlis su "kartuvėmis", kuris
kis priklausomai nuo Jūsų neatspėtų raidžių (likusių "gyvybių") skaičiaus. Grafinės sąsajos dešinėje pateikiama trumpa informacija apie galimų likusių spėjimų
skaičių, paslėptas spėliojamas žodis (kiekviena raidė priskirta brūkšniui), įvedimo laukas su instrukcija apie galimus įvesti elementus ir neatspėtų raidžių
sąrašas.
  Paleidus kodą (grafika.pyw) bus sugeneruotas atsitiktinis žodis (db_kurimas.py kodo failo pagalba) iš tinklapio (šiuo atveju: https://lt.wikipedia.org/wiki/Telefonas), 
kurio ilgis yra nuo 5 iki 8 raidžių, šis žodis paverčiamas brūkšniais (brūkšnių skaičius yra lygus raidžių spėjamame žodyje skaičiui). Jums į įvedimo langą įvedus raidę
ir paspaudus "ENTER" bus užfiksuotas Jūsų spėjimas ir jei atspėsite raidę, informaciniame lauke (grafinės sąsajos kairės pusės apačioje) atsiras užrašas "Atspėjote" ir
paslėptame žodyje Jūsų spėta raidė nebebus brūkšnio pavidale, Jums neatspėjus Jūs būsite informuotas, kad neatspėjote raidės žodyje ir pasikeis kairėje pusėje esantis
paveikslėlis, kaip ir likusių neteisingų spėjimų sumą. Pralaimėsite jei neteisingai spėsite 6 raides, laimėsite jei atspėsite visą žodį neišnaudoję visų 6 gyvybių.

Veikimo pavyzdžiai:
https://imgur.com/EdFZZcR    .
https://imgur.com/T5E8BBi    .
https://imgur.com/FdaINV5
