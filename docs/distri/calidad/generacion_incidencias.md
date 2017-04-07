# Generació d’incidències
## Generació d’incidències AT amb GISCE-WEB

L’usuari que realitza la simulació de la incidència ha de tenir permisos
d’escriptura per realitzar aquesta simulació.

L’usuari de GISCE-ERP_QS entrarà el seu ususari i contrassenya en el quadre
d’acces al GIS tal com es pot veure en l’imatge.

Per accedir a la simulació de les incidències en AT s’ha d’anar al menú del
programa de GIS “Simulacions/Qualitat de servei AT”.

* **Font**. En aquest apartat es selecciona del desplegable la font des de la qual
  es realitzarà la simulació de la incidència. Es pot seleccionar una de les
  fonts existents a la xarxa de la llista de fonts.
* **Interruptors AT tancats**. En aquest apartat apareixen tots els interruptors
  susceptibles de ser oberts per efectuar la simulació.
* **Interruptors AT oberts**. En aquest apartat apareixen tots els interruptors
  oberts que es carreguen a partir del “Estat de la xarxa” que es poden tancar.

!!! Note
    Per canviar l’estat d’un interruptor de “tancat” a “obert” només cal
    seleccionar-lo en la llista d’interruptors tancats i arrossegar-lo a
    la llista de “ Interruptors oberts”.

!!! Note
    Per canviar l’estat d’un interruptor de “obert” a “tancat” només cal
    seleccionar-lo en la llista de “Interruptors oberts” i arrossegar-lo
    a la llista de “ Interruptors tancats”.

!!! Note
    Una vegada definit l’estat dels interruptors de la xarxa AT, ja es
    pot passar a realitzar la simulació de la incidència.

* **Nova incidència**. Es seleccionarà aquesta opció quan es vol crear una nova
  incidència, amb el seu interval associat.
* **Incidència existent**. Es seleccionarà aquesta opció quan es vol crear un
  nou interval en una incidència existent.
* **Nom de la  incidència**. S’ha d’indicar el nom de la nova incidència que es
  vol crear, o seleccionar-ne una d’existent si s’ha seleccionat la opció
  “Incidència existent”.
* **Origen de la incidència**. Es seleccionarà l’origen de la nova incidència
  seleccionant la opció desitjada del desplegable tal com s’ha definit a
  l’[apartat 3.2](./terminos_y_definicion.md#recollida-dinformacio) els possibles orígens.
* **Tipus incidència**. Es seleccionarà del desplegable la opció “programada”
  o “imprevista” segons s’indica a l’[apartat 3.7](./terminos_y_definicion.md#desagregacio-de-les-dades-de-la-interrupcio).
* **Causa de la incidència**. Es seleccionarà la causa de la incidència segons
  s’ha definit a l’[apartat 3.7](./terminos_y_definicion.md#desagregacio-de-les-dades-de-la-interrupcio).

Una vegada seleccionada la incidència, l’origen, el tipus i la causa es
procedeix a definir l’interval de la incidència que es simularà en el GIS.

* Nom de l’interval: S’ha d’indicar el nom de l’interval que es vol simular.
* Hora inici: S’indicarà la data i hora del inici de la interrupció.
* Hora final: S’indicarà la data i hora del final de la interrupció.
* Iniciar la simulació: Una vegada complimentats tots els camps anteriorment
  exposats es procedeix a realitzar la simulació de la interrupció i es guardarà
  automàticament al mòdul GISCE-ERP_QS.

En el mapa del GIS es simularà la interrupció deixant en color vermell les
instal·lacions que han quedat afectades per la interrupció i en verd les que
segueixen amb tensió.
