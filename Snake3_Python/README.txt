VIDEREUTVIKLET BASERT PÅ KODE/INSPIRASJON FRA: https://www.geeksforgeeks.org/create-a-snake-game-using-turtle-in-python/
Denne koden er også lagt ved i filen 'originalSnakeGeeks.py'

Spillet STARTES FRA 'main.py'
Enjoy!


Utviklingshistorikk:
--------------------

Versjon 3.0
- klargjort for showcase :-)
- forbedret hvordan hastighet oeker gjennom spillet (opp til en viss grense)

Versjon 2.7
- slangen starter med hale, ikke bare med hode
- organisert mye kode paa nye maater: samlet game og world i egne filer og klasser

Versjon 2.6
- flyttet score utenfor rammen
- flyttet og samlet noen metoder inn i Snakes-klassen (f.eks. move())

Versjon 2.5 (januar 2024)
- funksjoner for pause, avslutte og fortsette spill lagt til
- kan nå styre slangen med piltaster i tillegg til ASDW

Tidligere versjoner
Per mars 2022
Har bl.a. utviklet følgende:
- laget variabler for å kontrollere størrelsen på spilleområdet og gjøre det enkelt med ulike størrelser på spillområdet
- tegnet ytterkanter
- fjernet blå mat som en mulighet (usynlig på blå bakgrunn)
- mat kan ikke dukke opp for nærme slangehodet i starten av et spill
- mat kan ikke plasseres under halen på slangen (er IKKE implementert i alle senere versjoner)
- underveis: sortert deler av koden i funksjoner og laget flere funksjoner der det virket naturlig og fornuftig

Per 8. april 2022
- startet på utvikling i retning objekt-orientert programmering

Senere har jeg også utviklet (per versjon 2.3)
- legge ut mer mat samtidig
- utvidet poengsystemer (ulik mat/poeng)
- endre fart underveis
- brukerstyrt mulighet for å avslutte spillet med Q

Ideer til videreutvikling:
- 2-player-modus
- unngaa at mat kommer under slangen eller paa toppen av annen mat
- legge til info om game-mode, level (fart) etc.
- lage algoritme for styring av en slange ('datastyrt'), slik at man kan spille mot den
- back-end-design: legge flere funksjoner og variabler til food-klassen (posisjonering?)
- vanskelighetsgrad mulig aa velge fra start
- pause-vindu med statistikk (lengde på slange, spilletid, evt. pausetid, evt. mer)
- bug-fiksing: ved raske trykk etter hverandre f.eks. opp+venstre når beveger seg mot
    hoyre, vil slangen kollidere i egen hale, tror jeg. Kanskje ok at det er slik, men kan fikses.
- ulike nerde-temaer, for eksempel spise neste siffer i pi for (ekstra) bonus
- flytte start-meny til selve turtle-vinduet
- legge mat i et synlig eller usynlig rutenett
- highscore-liste (skrive til/lese fra en egen fil)
- behandle grensetilfeller for avslutning på spillet 
    (til slutt vil ikke mat finne nye mulige plasseringer)
