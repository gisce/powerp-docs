# Compra i magatzem de comptadors

## Introducció

En aquest manual s'explica el mòdul de magatzems de GISCE-ERP per a la gestió
de comptadors. Concretament:

* Producte comptador
* Compra de comptadors
* Gestió de números de sèrie
* Recepció de lots amb números de sèrie correlatius

La gestió dels comptadors d'aquesta forma ens permet la seva traçabilitat, la
gestió del seu stock i localització i la gestió dels números de sèrie. Tot
aquest procés és **imprescindible** pels comptadors de telegestió que
s'utilitzin en el mòdul de telegestió de GISCE-ERP

El flux general, i pels comptadors en particular, seria el següent:

1. Donar d'alta el _producte_ comptador segons fabricant i model
2. _Comprar_ un determinat nombre de comptadors fent la petició de compra
   corresponent
3. _Rebre_ els comptadors i assignar-los el número de sèrie
4. Assignar el _número de sèrie_ , i per tant producte, als comptadors del menú
   **Infraestructura**

.. blockdiag::

 blockdiag {

    "Orden de compra" -> Confirmar
    Confirmar -> "Aceptada por proveedor" [label = "OK"]
    "Aceptada por proveedor" -> Recepción [label = "paquete"]
    Recepción -> "Asignación de Nº de série" [label = "albarán"]
    "Asignación de Nº de série" -> "Asociar a contador" [label = "install"]

 }

## Producte comptador

El primer pas per poder gestionar els comptadors correctament és donar-los
d'alta a la base de dades de productes. Podem accedir a la fitxa de productes
des del menú ``Productes``. Per crear o cercar el producte, és millor anar a la
categoria de producte corresponent des del menú ``Productes per categoria``

!!! tip
    Es recomana crear una categoria de producte **Comptador** o **Equips de
    mesura** per tenir localitzats els comptadors.

.. figure:: /_static/Captura06.png

   Fitxa de producte

A la figura podem veure els camps de la fitxa de producte (:ref:`fitxaproducte`)

És molt important que els impostos de client i proveïdor estiguin introduïts
correctament. (A la imatge es mostra l'IVA vigent en aquell moment)

!!! tip

    Quan es creen productes, es recomana duplicar un producte de la mateixa
   categoria que tingui tots els camps omplerts i així s'estalvia temps de
   creació del producte. S'ha de fer des de ``Formulari > Duplicar``
   Un cop duplicat s'han de canviar el *nom de producte*, el *codi*, el *preu*,
   la *referència del proveïdor* i el *proveïdor* quan sigui necessari.

La fitxa de producte es pot completar amb la pestanya ``Preus & proveïdors`` on
s'hi indicarà el preu de cost, els possibles proveïdors, els noms i les
referències de cada proveïdor per aquest producte (:ref:`fitxaproductepreus`).

.. _fitxaproductepreus:

.. figure:: /_static/Captura07.png

   Pestanya preus i proveïdors de la fitxa de producte

* **Preu cost**: És el preu que s'utilitzarà a l'ordre de compra d'aquest
  producte
* **Mètode de cost**: Si en aquest camp es posa *Preu mig* (serà el més
  habitual) el preu de compra s'anirà actualitzant a partir dels diferents
  preus de compra que es vagin donant.

Les dades de les pestanyes ``Proveïments i Ubicacions``, ``Descripcions`` i
``Empaquetament`` són dades informatives del producte, per tant no és
obligatori que estiguin omplertes.

## Compra de comptadors

Es descriu com realitzar l'ordre de compra dels comptadors i la recepció del
material en el magatzem.

.. figure:: /_static/Captura01.png

   Mòdul de compres

Per començar es selecciona el menú ``Compres > Comandes de compra > Sol·licitud
de presupostos``

.. figure:: /_static/Captura02.png

   Sol·licitud de pressupost

Prement el botó **Nou** (:ref:`novacomanda`)

.. _novacomanda:

.. figure:: /_static/Captura03.png

   Nova ordre de compra

creem una nova ordre de compra i primer omplim els camps tal com es veu a la
imatge :ref:`fitxasollicitudcompra`

.. _fitxasollicitudcompra:

.. figure:: /_static/Captura04.png

   Fitxa de sol·licitud de compra

S'ompliran com a mínim els camps de color blau:

* **Ref. ordre**: Aquest camp s'omple automàticament quan es guarda l'ordre de
  compra
* **Magatzem**: S'indicarà el magatzem previst d'entrada de material
* **Data**: Data de sol·licitud del pressupost
* **Empresa**: Amb la lupa, seleccionem l'empresa a la qual es farà la
  sol·licitud de pressupost o la comanda directament
* **Direcció**: S'indicarà a quin comercial de l'empresa escollida se li farà
  la sol·licitud
* **Llista de preus**: S'indica la llista de preus que s'utilitzarà per obtenir
  els preus del producte. Per defecte, si no s'ha creat una llista de preus
  específica es farà servir la *"Default purchase list"* o llista de preus per
  defecte
* **Referència de l'ordre**: Camp informatiu en el cual es pot anotar la obra a
  la qual van dirigits els materials o deixar-la en blanc
* **Referència de l'empresa**: Si la comanda ha de portar alguna referència
  interna de la companyia es posa en aquest camp. Si no, es pot deixar en
  blanc.

Un cop omplert l'encapçalament de la sol·licitud de pressupost amb aquestes
dades es poden omplir les línies de la sol·licitud de pressupost seleccionant,
de la llista de productes, el producte i la quantitat a sol·licitar.

.. figure:: /_static/Captura05.png

   Afegir productes a sol·licitud de pressupost

.. |nou| image:: /_static/iconaNou.png
   :align: middle

Es selecciona el botó nou |nou| de l'apartat ``línia de ordre de compra``

El producte que es vol comprar ha d'estar degudament introduït a la base de
dades de productes amb totes les dades omplertes correctament.

I a la imatge següent (:ref:`formulariliniacompra`) es pot observar com es
selecciona el producte a comprar i s'omple la línia de la sol·licitud de
compra. Es marca en vermell els camps que ha d'omplir l'usuari.

.. _formulariliniacompra:

.. figure:: /_static/Captura08.png

   Omplir línia de compra

* **Producte**: Amb la lupa es selecciona el producte desitjat. Poden
  utilitzar-se els filtres necessaris per filtrar (``categoria``,
  ``proveïdor``, etc..) per una localització més fàcil dels productes.
* **Quantitat**: S'ha d'indicar les unitats d'aquest producte que es desitja
  comprar.
  Poden introduïrse tantes línies de compra com es desitgi a cada ordre de
  compra.

Prement el botó **Calcular** es mostrarà el cost total previst de la compra a
partir dels preus de compra introduïts a la base de dades.

.. figure:: /_static/Captura09.png

   Ordre de compra a punt per confirmar

Un cop introduïdes totes les línies de sol·licitud de compra i confirmats els
preus de compra es pot prèmer el el botó **Confirmar comanda de compra**

.. note::

   Es pot anul·lar posteriorment si es decideix no realitzar-la prement el botó
   **Cancel·la comanda de compra**

Un cop confirmada, es pot veure com l'estat de la comanda ha passat de l'estat
``Petició de pressupost`` a ``confirmat`` tal com es veu a la casella ``Estat
de la comanda``

.. figure:: /_static/Captura10.png

   Ordre de compra confirmada

Podem accedir posteriorment a les comandes confirmades a la opció de menú
``Compres > Comandes de compra > Comanda de compra esperant aprovació`` on es
llistaran totes les comandes confirmades que esperen l'aprovació per part del
proveïdor, confirmació de preus de compra, disponibilitat de productes, etc...

.. figure:: /_static/Captura11.png

   Menú de comandes de compra. Esperant aprovació

Podem veure el llistat :ref:`llistatOCpendents` de totes les ordres de compres
que estan esperant la confirmació per part del proveïdor

.. _llistatOCpendents:

.. figure:: /_static/Captura12.png

   Llistat de comandes de compra pendents d'aprovació

Fent doble clic sobre l'ordre de compra, es mostrarà en format formulari.

Un cop fetes les gestions amb el proveïdor i es consensuin els preus amb la
companyia, ja es pot prèmer el botó **Aprovada pel proveïdor**

Mentre no es premi el botó **Aprovada pel Proveïdor** s'és a temps de modificar
el preu dels productes o les seves quantitats.

Un cop s'ha apretat el botó, l'ordre de compra passa a l'estat de ``ordres de
compra en procés``. Totes aquestes comandes les veurem al llistat accessible
des del menu ``Compres > Comandes de compra > Comandes de compra en procés``

.. figure:: /_static/Captura13.png

   Menu de comandes de compra. En procés

Obtindrem el llistat :ref:`llistatOCproces` de totes les ordres de compra que
han estat aprovades.

.. _llistatOCproces:

.. figure:: /_static/Captura14.png

   Llistat de comandes de compra en procés

L'ordre de compra encara es pot cancel·lar. Per fer-ho accedim a l'ordre de
compra i premem el botó **Cancel·la comanda de compra**

.. figure:: /_static/Captura15.png
   :width: 80%

   Cancel·lar ordre de compra en procés

## Recepció de material amb número de sèrie

Accedim a l'*ordre de compra en procés* per realizar-ne la recepció fent
doble-click.

.. figure:: /_static/Captura15.png

   Ordre de compra a punt per rebre el material

Quan arriba l'albarà amb el material al magatzem es procedeix a la seva
recepció prement al botó de la part superior dreta **Paquet/Albarà**

Obtindrem el formulari amb la línia de paquets que es mostra a la figura
:ref:`albarapaquets`

.. _albarapaquets:

.. figure:: /_static/Captura16.png

   Linies de paquets d'un albarà

Prement sobre la línia de recepció de paquets obtindrem finalment la fitxa per
omplir les dades de la recepció del material.

.. figure:: /_static/Captura17.png

   Fitxa de recepció de material

Aquesta fitxa conté un seguit de camps a títol informatiu:

* **Ref. origen**: És el codi d'albarà en el qual ha arribat el material, per
  defecte GISCE-ERP li assigna una referència de la comanda
* **Data prevista**: Data en la qual es fa la recepció del material. No es pot
  modificar.
* **Tipus d'enviament**: Quan el material arriba del proveïdor, sempre és
  ``Recepció mercaderies``

Fent doble-click sobre la línia del material, apareix la fitxa per fer la
recepció :ref:`recepciomaterial`

.. _recepciomaterial:

.. figure:: /_static/Captura18.png

   Fitxa recepció de línia de material

Per fer la recepció del material, podem fer-ho segons diferents casos:

.. _cas1:

Cas 1: Tots els comptadors amb número de sèrie correlatius
----------------------------------------------------------

Suposem que els 10 comptadors d'una comanda tenen número de sèrie consecutius
del 10000001 al 10000010.

Premem el botó **Dividir en sèries** i es crearan 10 línies cadascuna amb un
comptador i el seu número de sèrie, quedant la recepció de material tal com es
veu en la imatge :ref:`recepciocas1`

.. _recepciocas1:

.. figure:: /_static/Captura19.png

   Fitxa recepció material dividida en 1 sèrie correlativa (Cas 1)

Per acabar, prement el botó **Productes rebuts** apareixerà el cuadre de diàleg
:ref:`recepciocas1rebuts` i prement el botó **Crear albarà** es donarà el
procés de recepció de material per acabat, passant a estat ``realitzat``
:ref:`recepciocas1realitzat`

.. _recepciocas1rebuts:

.. figure:: /_static/Captura20.png

   Productes rebuts (Cas 1)

.. _recepciocas1realitzat:

.. figure:: /_static/Captura21.png

   Fitxa recepció material en estat realitzat (Cas 1)

.. _cas2:

Cas 2: Comptadors amb 2 grups de número de sèrie correlatius
------------------------------------------------------------

.. |accio| image:: /_static/iconaAccio.png
   :align: middle

Estem en aquest cas quan la recepció del material sigui parcial o bé que els
números de sèrie no siguin correlatius.

Suposem que arriben 4 comptadors amb número de sèrie correlatiu 10000100 al
10000104, i un altre grup de 6 comptadors amb els números de sèrie de 20000200
al 20000206.

Es procedirà de la següent forma:

Des de la fitxa de recepció de material :ref:`recepciomaterial` haurem de
dividir la línia de 10 comptadors en dues línies, una de 6 comptadors i una
altra de 4 comptadors. Seleccionem la línia i premem el botó d'**acció**
|accio| i del menú que apareix seleccionem la opció ``Divideix línia de
moviment``

.. figure:: /_static/Captura22.png

   Menú acció

A la casella blava haurem d'indicar quants comptadors tenen número consecutiu,
(en el nostre exemple indicarem *6*) i prèmer el botó **Dividir**

.. figure:: /_static/Captura23.png

   Partició de línies

El resultat serà que es crearan 2 línies a la fitxa empaquetat/albarà
(:ref:`recepciomaterial`). Apareixeràn les dues línies al fer doble-click sobre
la línia.

.. figure:: /_static/Captura24.png

   Recepció de material partida en dues línies (Cas 2)

Un cop divit l'``Empaquetat/Albarà`` es procedirà com en el :ref:`cas1` per cada
una de les linies creades.

Es pot fer d'aquesta forma si no hi ha recepcions parcials de material.

En el cas de comandes que arriben amb diferents albarans d'entrega, el procés
es realitza com en el :ref:`cas2`.
