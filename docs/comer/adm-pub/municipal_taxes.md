# Documentació del modul per crear informes de taxes municipals

## Introducció

Alguns municipis demanen certa informació respecte als impostos sobre la
circulació d'electricitat pel seu municipi. Aquest mòdul permet crear un fitxer
amb aquesta informació de forma fàcil i ràpida.

## Generació

Per generar el fitxer només hem de seleccionar el municipi o municipis dels
quals volem crear l'informe en la llista de municipis que trobarem a
*Administració Pública > Administracions locals > Impostos > Municipis*.

![Figura 1](../_static/municipal_taxes/menu.png)

Un cop hàgem seleccionat tots els municipis que desitgem podrem prémer el botó
d'*Accions*, que obrirà una finestra com la següent:

![Figura 2](../_static/municipal_taxes/wizard_ini.png)

Aquí haurem d'entrar les següents dades:

* **Data d'inici**. Data d'inici del període pel qual volem fer l'informe (inclosa).
* **Data de fi**. Data de fi del període pel qual volem fer l'informe (exclosa).
* **Afegir llista factures**. Si marquem aquest camp s'afegiran dos llistats de
totes les factures realitzades entre les dates seleccionades, separades entre
les factures de proveïdors i les factures a clients.
* **Tipus de fitxer generat**. Ens permet seleccionar el tipus de fitxer que volem
que es generi. Si seleccionem CSV tota la informació es guardarà en una sola pàgina,
donant el resum del total i, si s'ha marcat **Afegir llista factures**, les factures
de proveïdors i les factures a clients. Aquestes dades les tindrem per cada poble
que hàgem seleccionat, ordenats alfabèticament. Altrament, si seleccionem que volem
un Excel els llistats de factures (en cas de demanar-los) es guardaran per separat
en dues altres pestanyes, una per factures de proveïdors i l'altre per factures a
clients. Aquestes dades també estaran ordenades alfabèticament pel nom del municipi.

Un cop entrades totes les dades, podem prémer el botó de generar. Això farà les
consultes necessàries per generar el fitxer i el generarà, permetent obrir-lo
directament o guardar-lo a l'ordinador.

![Figura 3](../_static/municipal_taxes/wizard_fin.png)

## Dades utilitzades

Per tal de generar el fitxer es tenen en compte totes les factures amb una data
de factura entre les dates seleccionades. També es tenen en compte cada una de
les línies de factura i els seus account_invoice associats. A més, s'utilitza
la pòlissa associada a les factures per trobar la CUPS, que finalment ens permet
trobar a quin municipi pertany cada factura.

D'altra banda, per tal de generar la part del llistat de factures (si s'ha
seleccionat) s'utilitzen les taules de res_partner per trobar la informació de
la distribuïdora i del client i les tarifes per mirar quina tarifa té cada client.