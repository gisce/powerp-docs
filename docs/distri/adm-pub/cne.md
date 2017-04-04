# Documentació de les funcionalitat per CNE

## Liquidacions per la CNE

### Generació de les liquidacions per la CNE

Per tal de generar les liquidacions per la CNE utilitzarem l'assistent que es troba
en el menú principial de **Liquidacions**:

_"Liquidacions > Generar liquidacions a partir de les factures"_

![](../_static/adm-pub/cne/liq_0.png)

En executar aquest asssistent es mostrarà una finestra on hem d'escollir el període
pel qual volem generar la liquidació de la CNE.

![](../_static/adm-pub/cne/liq_1.png)

Apretem el botó **Generar liquidacions** i ens esperem a que finalitzi el càlcul.

!!! note
   Pot ser que el programa es bloquegi, segons el número de factures que estiguin
   incloses en el període de liquidació seleccionat. Veurem que el botó es queda
   _clavat_, ens hem d'esperar que finalitzi l'operació.

!!! tip   
    Si volem continuar treballant, podem obrir un altre client de l'ERP i continuar
    fent feina.

En el cas que ja hi haguessin línies de liquidació entrades en el període seleccionat i
aquest període de liquidació es trobés en estat **esborrany** el programa ens
avisaria que ja conté línies i si les volem eliminar.

![](../_static/adm-pub/cne/liq_2.png)

És una situació normal, quan es vol re-generar la liquidació ja sigui perquè s'han refet
algunes factures o s'ha corretgit algun error.

Un cop realitzada l'operació de les liquidacions se'ns mostrarà un diàleg
anunciant que l'operació s'ha realitzat correctament.

![](../_static/adm-pub/cne/liq_3.png)

A través del botó **Mostrar liquidació** se'ns obrirà una pestanya nova amb la liquidació generada.

![](../_static/adm-pub/cne/liq_4.png)

Podem fer doble clic sobre la liquidació generada i això ens obrirà la liquidació en
mode formulari.

![](../_static/adm-pub/cne/liq_5.png)

Podem imprimir la liquidació a PDF mitjançant el botó _Imprimir_ o la opció
_Liquidació_ al menú de la dreta un cop dins la liquidació

### Exportació de liquidacions a CSV

GISCE-ERP també permet exportar les liquidacions mitjançant un fitxer CSV. Per
fer-ho, podem seleccionar una liquidació i prèmer al botó _Acció_ o la opció
_Exportar Liquidació (CSV)_ del menú de la dreta un cop dins la liquidació. Se'ns obrirà
l'assistent que permetrà descarregar-nos el fitxer CSV generat.

![](../_static/adm-pub/cne/liq_8.png)

!!! note
   El Fitxer s'anomenarà automàticament amb el format
   **liquidacio_RRRR_YYYYMM.csv** on _RRRR_ és el codi de referència de la
   distribuidora i _YYYYMM_ l'any i mes de la liquidació.

!!! note
   El fitxer CSV generat separa els camps per punt i coma (**;**) i pels valors numèrics
   utilitza el punt (**.**) com a separador de decimals.


### Com es generen els càlculs de la liquidació

* **Factures normals**:

    Les factures normals generades a través d'un lot s'assignen al mateix període de liquidació que
    correspon al lot de facturació. Així doncs el lot de facturació 10/2011 es correspon amb el
    període de liquidació 10/2011.

* **Factures rectificadores/anul·ladores**:

    Quan es rectifica/anul·la una factura es demana en quin període de liquidació es vol assignar el
    resultat d'anul·lar rectificar. S'ha de tenir en compte que les anul·ladores comptaran en negatiu,
    per tant s'ha de vigilar on s'assignen les factures recitificadores/anul·ladores per tal que no surti
    un total negatiu.


### Localitzar factures segons els període de liquidació

Podem filtrar les factures segons el perídode de liquidació al llistat de factures generals, clicant
sobre el més per ampliar els paràmetres de filtratge i filtrant pel període de liquidació.

![](../_static/adm-pub/cne/liq_6.png)

Podem veure en una factura el període de liquidació assignat a la pestanaya **Energia**.

![](../_static/adm-pub/cne/liq_7.png)


## Càlcul de les quotes per la CNE


Per tal de calcular les quotes que hem de presentar mensualment a la CNE ho
podem fer a través del menú **Administració Pública > CNE > Facturació >
Calcular quotes CNE**

Hem de seleccionar quin període volem generar les quotes.

Si en el període que ens trobem hi ha hagut un canvi de quotes per part de la
CNE, podem introduïr en l'assistent la data de canvi de les quotes en el
camp **data de tall**, d'aquesta forma el programa ja repartirà tant
l'energía com els euros facturats. La data de tall està inclosa en el segon
període per tant ha de ser la data en que s'apliquen els nous percentatges.

El la següent imatge es mostra un exemple on hi ha hagut un canvi en el dia
03/08/2013, per tant, aquesta és la data que hem de posar en el camp **data
de tall** i un cop calculat el resultat ens mostrarà els valors que hem
d'introduïr a la web de la CNE.


![](../_static/adm-pub/cne/quota_1.png)
