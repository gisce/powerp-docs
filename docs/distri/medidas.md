# Mesures REE

## Mòdul de Mesures REE

Aquest mòdul serveix per la generació de fitxers d'intercanvi de mesures amb
REE, siguin d'origen Telegestió, Telemesura o Perfilat.
Inclou generació, processament i validació d'aquests fitxers.

## Menú de Mesures REE

En el menú de Mesures REE que segueix a la imatge, s'hi troben els següents
apartats.

* Perfils: permet visualitzar els perfils horaris generats a filtrar per
factura o CUPS, aquests es calculen automàticament a l'obrir la factura.

!!! Info "Nota"
    Per tal de desactivar la perfilació de forma automàtica, cal posar la
    variable de configuració `profile_on_invoice_open` a `0`.

* Períodes de Mesures: mostra l'estat, i el progrés, dels períodes de mesures
* Tancaments: visualitza les dates d'entrega dels fitxers de REE (M+1, M+3...)
* Casos de perfilació: casos CRM que reporten el comportament al perfilar
* Casos de mesures: casos CRM que reporten el comportament al generar els
fitxers de mesures
* Crear períodes de Mesures: assistent que permet crear els períodes segons any

![](_static/medidas/menu_general.png)

## Preparació de les dades

Abans de generar els fitxers de mesures, cal comprovar que les dades a incloure
en aquests, estan preparades. Els orígens de dades són els que segueixen:

### Telegestió
Són corbes provinents de contadors telegestionats, corbes reals, que s'hauran
d'entregar sense forats.
Aquestes corbes passen per un procés de validació i ajustament.

* Procés de validació:
consisteix en trobar i descartar consums impossibles, hores duplicades... Es
realitza automàticament i diàriament a una certa hora del dia.

* Procés d'ajustament (FIX CCH):
El procés d'ajustament de la corba s'anomena `fix_cch_fact`. Es fa
automàticament a l'obrir la factura (si és de telegestió). Aquest procés
consisteix en emplenar els forats i ajustar el consum de la corba perquè doni
el consum real.
La mateixa factura indica si la corba té el fix fet, mitjançant el camp
`CCH disponible`.
Per assegurar-se que no ha quedat cap corba sense ajustar-se, existeix un
llistat a:
**Facturació > General > Factures Client > Factures Client CCH no disponible**

![](_static/medidas/factures_cch_no_disponible.png)

### Telemesura

Les dades de telemesura ens poden venir de diversos orígens, genèricament es
carreguen les corbes de telemesura mitjançant fitxers llegits directament del
comptador per tal de tenir la corba real. Aquesta explicació bé recollida en un
altre apartat d'aquest manual. És important carregar aquestes corbes el més
aviat millor.

### Perfil
Quan no es possible disposar de cap dels dos orígens anteriors, cal perfilar
una corba horària mitjançant els coeficients que publica mensualment
REE [Perfils de consum](https://www.ree.es/es/actividades/operacion-del-sistema-electrico/medidas-electricas)
El perfilat es realitza de forma automàtica una vegada s'obre la factura.

!!! Info "Nota"
    Les corbes del tipus 3 (>50kWh) s'han d'entregar amb corba real.
Per comprovar que totes les factures estan perfilades correctament, cal fixar-se
en la barra de progrés del mateix període de mesures. Per actualitzar aquest
progrés, es necessari utilitzar el botó **Actualitzar Progrés de Perfilació**

![](_static/medidas/actualitzar_perfilacio.png)

* Factures del període:
Dins cada període de mesures descrit en el següent apartat, es disposa un
llistat amb totes les factures del període ordenades i filtrables per orígen
**(telemesura, telegestió, perfil)**. Aquestes últimes, al acabar el seu progrés
de perfilació es marquen com estat: Finalitzat. Aquest llistat ajuda a revisar
quines factures no s'ha perfilat encara.

![](_static/medidas/factures_periode.png)

## Períodes de mesures

Els fitxers de REE, s'entreguen per períodes a **mes complet**, cada període de
mesures és un mes en concret, el qual engloba les dates, el número de factures,
de contractes i un control del procés de perfilació.

![](_static/medidas/periodes_mesures.png)

## Fitxers REE

Per tal de generar els fitxers de REE, cal dirigir-se a Mesures REE > Períodes
de mesures > Fitxers REE.
Aquest mòdul permet la generació i tractament dels següents fitxers:

* AGCL
* CLMAG
* CLMAG5A
* CLINME
* AGCL (publicat per l'Operador del sistema)
* AGCLACUM
* AGCLACUM5

Cada fitxer porta associat un botó per tal de procedir a la seva generació, per
fer-ho, sols cal fer click al damunt. La generació d'aquests no té cap ordre en
concret, però es convenient generar-los d'un a un. Cal recordar que REE espera
primer l'entrega de l'AGCL per tal de "obrir la pasarela d'entrega per aquell
període en concret", i seguidament espera els altres fitxers. Si no es manté
aquest ordre d'entrega, REE rebutja els fitxers ja que no s'han publicat
l'inventari d'agregacions d'aquell mes.

A la part esquerre es visualitzen les agregacions que imputen energía en aquest
període en concret. Amb el botó Generar Nivells d'Agregació, es crean aquestes
agregacions. Tot generant els fitxers, és quan s'aniran omplint les dates i el
consum d'aquestes.

![](_static/medidas/mesures_ree.png)
