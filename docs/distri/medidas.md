# Documentació del mòdul de mesures

## Mòdul de Mesures REE

Aquest mòdul serveix per la generació de fitxers d'intercanvi de mesures amb
REE, ja siguin d'origen Telegestió, Telemesura o Perfilat.
Inclou generació, processament i validació.

## Menú de Mesures REE

En el menú de Mesures REE que segueix a la imatge, s'hi troben els següents
apartats.

* Perfils: permet visualitzar els perfils horaris generats a filtrar per
factura o CUPS, aquests es calculen automáticament a l'obrir la factura

!!! Info "Nota"
    Per tal de desactivar la perfilació de forma automàtica, cal posar la
    variable de configuració `profile_on_invoice_open` a `0`.

* Períodes de Mesures: mostra l'estat, i el progrés, dels lots de perfilació
* Tancaments: visualitza els tancaments M+1 , M+3, Provisional i Definitiu
* Casos de perfilació: casos CRM que reporten el comportament al perfilar
* Casos de mesures: casos CRM que reporten el comportament al generar els
fitxers de mesures
* Crear períodes de Mesures: assistent que permet crear els períodes segons any

![](_static/medidas/menu_general.png)

## Preparació de les dades

Abans de generar els fitxers de mesures, cal comprobar que les dades que han
d'incloure aquests están preparades. Els origens de dades es descriuen a
continuació.

### Telegestió:
Curves reals, que s'haurán d'entregar sense forats. Aquestes
curves passen per un procés de validació i ajustament. El procés de validació
consisteix en trobar i descartar consums impossibles, hores duplicades... I es
fa automáticament a una certa hora del dia. El procés d'ajustament de la curva
s'anomena `fix_cch_fact`. Es fa automàticament a l'obrir la factura (si és de
telegestió). Aquest procés consisteix en emplenar els forats i ajustar el
consum de la curva perqué sigui el consum real, en cas de no está correcte. La
mateixa factura indica si té el fix de la curva fet amb el camp `CCH disponible`
Per assegurar-se que no ha quedat cap curva sense ajustar-se, existeix un
llistat a
**Facturació > General > Factures Client > Factures Client CCH no disponible**

![](_static/medidas/factures_cch_no_disponible.png)

### Telemesura:
Les dades de telemesura ens poden venir de diversos origens, genéricament
carregarem les curves de telemesura mitjançant fitxers llegits directament del
comptador per tal de tenir la curva real. Per tant es important carregar
aquestes curves el més aviat millor.

### Perfil:
Quan no es possible disposar de cap dels dos origens anteriors**, s'ha de
perfilar una curva horária mitjançant els coeficients que publica mensualment
REE [Perfils de consum](https://www.ree.es/es/actividades/operacion-del-sistema-electrico/medidas-electricas)
El perfilat es realitza de forma automàtica una vegada s'obre la factura.

!!! Info "Nota"
    Les curves del tipus 3 (>50kWh) s'han d'entregar amb curva real.

## Períodes de mesures

Els fitxers de REE, s'entreguen per períodes a mes complet, cada període de
mesures és un mes en concret, el qual engloba les dates, el número de factures,
de contractes i el procés de perfilació.

![](_static/medidas/periodes_mesures.png)

## Fitxers REE

Per tal de generar els fitxers de REE, cal dirigir-se a Mesures REE > Períodes
de mesures > Fitxers REE.
En aquesta vista es disposa de uns botons (Generar CLMAG, Generar CLMAG5A...)
per tal de crear aquests fitxers. Per fer-ho, sols s'ha de fer click damunt
del botó. És convenient generar-los un a un. No existeix cap ordre en concret.

A la part esquerre es visualitzen les agregacions que imputen energía en aquest
període en concret. Amb el botó Generar Nivells d'Agregació, es crean aquestes
agregacions. Tot generant els fitxers, és quan s'anirán omplint les dates i el
consum.

Per començar el procés de perfilació s'ha de clicar a '**Lots de Perfilació**',
on apareixerà una finestra on podrem realitzar el procés de perfilat. Abans
d'això caldrà realitzar unes comprovacions bàsiques de les pòlisses a perfilar
que a continuació expliquem.

![](_static/medidas/mesures_ree.png)
