# Validacions

## Validacions a la importació d'F1

Les validacions que es mostren a continuació es realitzen en la importació de F1.

### Identificadors de les validacions

Cada validació tindrà un codi a l'ERP. Aquest codi sempre comença amb la fase en la qual es crea, seguit del nombre de template que té l'error. Per exemple, [3001] seria la validació del template 001 de la fase 3. Tots els texts que tinguin el mateix codi seguiran el mateix format i seran deguts a la mateixa causa.

Un sol fitxer F1 pot tenir dues o més vegades el mateix error si aquest error es repeteix.

### Nivells de les validacions

Les validacions tenen tres nivells, descrits a continuació:

- **Critical (E)**: Aquest és un error que ens impedeix seguir amb la importació. Això causarà que la importació s'aturi en la iteració a la que estigui.
- **Warning (W)**: Aquest és un possible error que s'hauria de revisar però que no ha de ser necessàriament problematic. En aquest cas no s'aturarà la importació.
- **Information (I)**: Aquest és un cas especial però que no hauria de portar mai problemes, simplement es dona la informació que ha passat. Tampoc atura la importació.

### Activar i desactivar validacions

Podem activar i desactivar algunes de les validacions. Per tal de fer-ho simplement ens hem de dirigir a `Facturació > General > Configuració > Switching > Error plantilles`.

No totes les validacions es poden activar i desactivar. Concretament, hi ha validacions que estan incloses en el codi, de manera que no ens les podem saltar. D'altra banda, per qüestions de seguretat, s'ha decidit que les validacions de nivell crític no es podran desactivar mai.

Existeix un camp que ens permet cercar les validacions segons si es poden desactivar o no, per facilitar la cerca de les validacions que es poden desactivar.

El camp `actiu` es mostrarà en només lectura quan aquest no es pugi desactivar. Altrament, es mostrarà modificable si es pot desactivar.

### Validacions que es realitzen

#### Fase 1

#### Fase 2

#### Fase 3

- Comprovacions comptadors

    - **[3001] Adequar gir a lectura (I)**: És realitza una validació de que el gir que tenim a la base de dades és diferent al que ens donen al fitxer F1.
    - **[3014] El gir de l'F1 no es correcte (I)**: És realitza una validació de que el gir que ens donen al fitxer F1 sigui suficient per les lectures que ens donen. Per exemple, si ens donen un gir de 100 i una lectura de 4560 sabem que com a mínim el gir ha de ser de 10000.
    - **[3002] El comptador existeix (W)**: Comprovem que el comptador que ens donen existeix en la nostra base de dades. Tenim en compte que hi pot haver padding de zeros. *Veure el punt Moguts a la iteració 4*
    - **[3003] Comptador repetit (I)**: Comprovem si en una sola factura tenim dues vegades un mateix comptador.
    - **[3004] Comptador de reactiva (I)**: Comprovem si algun dels comptadors només té lectures de reactiva (pels casos en que tenim un comptador per activa i un per reactiva).
    - **[3005] Més d'un comptador actiu (W)**: Comprovem si la pòlissa té més d'un comptador actiu actualment.

- Comprovacions dades CCH

    - **[3006] Coincidència amb estat del contracte (W)**: Comprovem quin és el valor del camp IndicativoCurvaCarga del fitxer F1. Depenent de la pòlissa esperarem els següents valors:
        - Si la pòlissa té una tarifa 3.1 o 6.X sempre haurà de ser *03*.
        - Si la pòlissa té una tarifa inferior a 3.1 dependrà de si tenim la telegestió activada o no
            - Si la pòlissa té la telegestió operativa, esperarem el valor *01*.
            - Si la pòlissa té la telegestió no operativa, esperarem el valor *02*.

- Lectures d'Energia i Reactiva

    - **[3007] Divergència entre la lectura existent i l'F1 (E)**: Si tenim una lectura entrada pel mateix dia que ens arriba amb el fitxer F1, comprovem si són iguals. Aquesta comprovació només es realitza per factures no rectificadores.
    - **[3008] Nombre de períodes (E)**: Tenim un nombre incorrecte de períodes per un comptador segons la seva tarifa.
    - **[3009] Lectures negatives (E)**: El consum d'alguna de les lectures importades és negatiu.
    - **[3010] Ajust integrador (I)**: Alguna de les lectures importades té ajust integrador.
    - **[3011] Possible gir de comptador (I)**: Alguna de les lectures finals són inferiors a les lectures inicials.
    - **[3012] Factura rectificadora (I)**: La factura és rectificadora, de manera que les lectures es sobreescriuran.
    - **[3013] Origen "Sin lectura (99) (I)**: Alguna de les lectures té com a origen 99, és a dir, no hi ha lectura. *Veure el punt Moguts a la iteració 4*
    - **[3015] Unitats d'importació (I)**: S'indicaran quines són les unitats amb les que suposarem que ens venen els valors.

- Lectures de Maxímetre

    - **[3007] Divergència entre la lectura existent i l'F1 (E)**: Si tenim una lectura entrada pel mateix dia que ens arriba amb el fitxer F1, comprovem si són iguals. Aquesta comprovació només es realitza per factures no rectificadores.
    - **[3008] Nombre de períodes (E)**: Tenim un nombre incorrecte de períodes per un comptador i un tipus.
    - **[3009] Lectures negatives (E)**: El consum d'alguna de les lectures importades és negatiu.
    - **[3010] Ajust integrador (I)**: Alguna de les lectures importades té ajust integrador.

- Lectures d'energia

    - **[3016] Lectura impossible (W)**: La lectura no és possible ja que el seu valor és superior a consumir la potència contractada durant totes les hores del període entre les dates de les lectures.

- Mode facturació

    - **[3017] Tarifes inconsistents (W)**: La tarifa que tenim guardada i la tarifa de l'XML no coincideixen.
    - **[3018] Facturació de potència inconsistent (W)**: El mode de facturació de potència (Maxímetre o ICP) que tenim guardat per la pòlissa i el que indica l'XML no coincideixen.
    - **[3019] Lectura en baixa inconsistent (W)**: L'indicador de si les lectures són en baixa no coincideix entre el que tenim guardat per la pòlissa i l'XML.
    - **[3020] Autoconsum inconsistent (I)**: Hi ha algun concepte amb tipus corresponent a l'autoconsum però nosaltres tenim la pòlissa sense autoconsum.


## Validacions al lot

Cada validació té un codi associat que permet la cerca de diferents pòlisses amb el mateix problema.

Les validacions que apareixen a continuació es realitzen en els lots de facturació abans de crear les factures. Les següents validacions es realitzen tant a les empreses comercialitzadores com en les distribuidores.

- [V001] Hi ha hagut una volta de comptador
- [V002] Comprovació de que existeixin lectures anteriors respecte les que haurem de comparar
- [V003] Comprovació de que hi ha lectures per a cada periode de la tarifa
- [V004] Control dels canvis de contador
- [V005] Comprovació de que la pòlissa tingui un comptador actiu en les dates de facturació
- [V006] Validació de que el consum no sigui negatiu
- [V007] Validació de que existeixin intervals pels quals facturar
- [V008] Validació de que el consum no sigui inferior a un cert limit
- [V009] Validació de que la lectura del maxímetre no sigui superior en més d'un percentatge a la potència contractada, per periode
- [V010] Validació de que el consum no sigui superior a un cert limit, que depén de la tarifa
- [V011] Validació de que les lectures de reactiva no siguin superiors a un percentatge de l'activa, per periode
- [V012] Analisi de quins periodes falten per les dates de facturació
- [V013] Les lectures anteriors i actuals són iguals
- [V014] Falta la lectura de tancament per un comptador de baixa dins del periode de facturació

Les següents validacions només es realitzen en les empreses comercialitzadores:

- [V015] Hi ha algun problema amb el mandato

Les següents validacions només es realitzen en les empreses distribuidores:

- [V016] Comprovació si un comptador està al TPL

## Validacions en la creació de factures

Les següents validacions es realitzen quan creem una factura després de passar o saltar-nos les validacions de lot.

- [F001] El consum (kWh) del mes és superior en un percentatge al màxim dels últims n mesos
- [F002] La potencia (kW) del mes és superior en un marge absolut al màxim dels últims n mesos
- [F003] El consum (kWh) del mes és superior en un marge absolut al màxim dels últims n mesos
- [F004] L'import d'energía facturat (€) és inferior o igual a un valor mínim
- [F005] L'import de potència facturat (€) és inferior o igual a un valor mínim
- [F006] L'import total facturat (€) és inferior o igual a un valor mínim
- [F007] L'import total és superior a un valor màxim, que depèn de la tarifa
- [F008] El consum (kWh) del mes no esta dins d'un marge. Aquests marge ve definit a partir d'un percentatge de la mitjana de consum dels ultims n mesos. També hi ha un valor absolut que defineix el marge mínim.
