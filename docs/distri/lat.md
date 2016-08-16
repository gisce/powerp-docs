***********
Alta Tensió
***********

Introducció
===========

El mòdul d'alta tensió ens permet inventariar les línies i els trams d'alta
tensió

Crear una nou tram d'Alta Tensió
================================

Per crear un nou Tram d'Alta Tensió ho podem fer a través del llistat de
tots els trams AT i després apretar el botó de **Nou**, igual que es fa amb la
resta de registres de l'ERP.

També es pot crear des del llistat de Trams de la fitxa de *Línia AT* prement a
la icona de nou habitual en els llistats de l'ERP.

Ens apareixerà un formulari on podem visualitzar una capçalera i diferents
parts:

  * General
  * Dades Administratives
  * Observacions
  * Expedients

En l'apartat de **Dades Administratives** tenim els camps:

  .. image:: _static/lat/formulari_administratiu.png

  * **Propietari**: Per indicar si som propietaris o no. Es calcula
    automàticament segons la línia associada al tram i no es pot modificar.
  * **% pagat per la compañia**: Per indicar quin percentatge ha pagat l'empresa
    per aquest element.
  * **Bloquejar APM**: Permet fixar a una data concreta la *Data APM*. D'aquesta
    forma es permet posar-hi una data fixa i que no es sobreescrigui
    automàticament tal com s'explica a *Data APM*
  * **Data APM**: En quina data es va posar en marxa. Aquest camp
    s'actualitza sol segons la data d'autorització més gran dels expedients
    associats si no es marca el camp *Bloquejar APM*. En aquest cas es pot posar
    una data arbritària.
  * **Actiu**: Per marcar si aquest tram està actiu o no. En el cas que no
    estigui activa, no ens apareixerà al llistat a no ser que li diguem
    explícitament que volem veure els trams no actius.
  * **Data de baixa**: Per indicar en quina data es va donar de baixa el tram.
    Aquest camp només és visible quan el camp *Actiu* no està activat.
  * **Obres**: Amb quines obres relacionem aquest tram.
  * **Expedients**: Amb quins expedients relacionem aquest tram.
