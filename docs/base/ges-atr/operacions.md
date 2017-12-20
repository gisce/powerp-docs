## Operació


### Creació d'un cas com a originador

![](../_static/atr/NouCas.png)

Nosaltres som l'inici del procés. A partir d'una sol·licitut del Client omplim
les dades necessàries del cas i generem el **Pas 1** del procés. En aquest
procés, nosaltres serem l'``Agent Sol·licitant``

En alguns casos haurem de partir d'una pólissa ja existent. Per exemple, en el
cas d'un C1, necessitem que el contracte ja estigui en esborrany.


#### Creació del cas

Des del llistat de tots els casos, premem sobre el botó **Nou** i se'ns obrirà
el formulari del cas. Haurem d'anar omplint les dades de les diferents
pestanyes.

* **Descripció**: Descripció del cas per poder-lo trobar. Si es deixa buida,
  s'omplirà automàticament.

A la pestanya ``Contactes``:

* **Empresa**: Seleccionar l'empresa elèctrica destinatària del procés i el seu
  contacte
* **email**: Podem canviar-lo per el que ens interessi

A la pestanya ``Switching``:

* **Procés**: Escollir el procés que generem (C1, C2 o M1)
* **CUPS**: Podem seleccionar un CUPS dels donats d'alta. Per tant haurà
  d'existir a la base de dades de CUPS. S'omple automàticament si seleccionem
  la pólissa
* **Pólissa**: Podem seleccionar el contracte afectat pel procés. Cal que
  existeixi , encara que estigui en esborrany.
* **Ref. Contracte**: La referència al contracte a la distribuidora. És
  obligatori i s'omplirà amb el valor que tingui a la Pólissa seleccionada

!!! Tip "Consell"
    Els camps ``CUPS``, ``Pòlissa`` i ``Ref. Contracte`` s'ompliran
    automàticament un cop s'ha escollit el cups o la pólissa.

Guardem el cas amb el botó **Guardar** i ens quedarà en estat ``Esborrany``


#### Obrir Cas

Per poder treballar amb el cas cal primer que l'obrim. per fer-ho podem prèmer
al botó **Obrir** de la pestanya ``General``

Per crear el Pas 1 del procés haurem d'anar a la pestanya switching i crear un
nou pas amb el botó **Nou** del llistat de passos. Se'ns obrirà el formulari de
nou Pas

* **Procés**: Haurem d'escollir de quin procés es tracta
* **Pas**: En el nostre cas escollirem el pas 1, ja que som el sol·licitant

La resta de camps no caldrà que els modifiquem, ja que s'omplen automàticament
quan guardem el cas

Tanquem el formulari i Guardem el cas amb el botó **Guardar**


#### Informació del cas

Tota la informació relativa a la sol·licitud es podrà editar a la informació
del Pas.

Per exemple és *obligatori* separar correctament el noms i els cognoms. Com que
aquest procés no es pot fer automàticament, l'haurem de fer nosaltres a mà.

Així doncs revisem les dades del pas obrint el pas 1 del llistat de passos de
la pestanya de ``Switching`` i obrim la carpeta al costat del camp **Info del
Pas**. Se'ns obrirà el formulari amb les dades del Pas.

Podrem editar els cognoms i el nom, afegir la informació que creiem convenient,
modificar els paràmetres del pas, etc... Aquesta informació serà la que
s'inclourà dins de l'XML.


#### Generació Pas 1

Per generar l'XML podem utilitzar el formulari d'exportació amb el botó
**Exportar XML**. Podrem descarregar el fitxer XML al nostre ordinador per
poder-lo enviar al destinatari.

També podrem enviar un mail directament des de l'ERP amb el XML adjuntat
prement al botó **Enviar Mail** del cas. Si tenim correctament configurat el
mòdul ``Power Email`` ens demanarà:

* **Des de**: Quin dels comptes configurats volem utilitzar
* **Receptor (Per a)**: utilitzarà el mail definit a la pestanya Contactes
* **Passos**: Sol·licitarà l'XML de quin pas volem adjuntar al mail
* Podrem escriure el contingut del mail que creguem necessari a l'àrea de text
  que hi ha a sota

---

### Creació d'un cas a partir d'un XML entrant

Rebem una petició a partir d'un XML enviat per un altre agent en un procés on
nosaltres hi som implicats.


#### Creació del cas

Premem sobre l'opció ``Importar XML`` del menú de Switching i carreguem el
fitxer. Si tot és correcte ens apareixerà un diàleg explicatiu amb el que ha
passat i podrem anar al llistat de casos directament.

En el llistat de casos veurem que s'ha creat el nou Cas en estat ``Obert``.
GISCE-ERP crea el cas en funció del fitxer XML rebut o afegeix el pas al procés
corresponent.
