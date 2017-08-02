# Tipus de rectificadores

## Normal (N)

### Ús

Les factures Normals són les més comúns. Totes les factures que es creen des dels
lots de facturació o des de les pólisses amb "Factura Manual" són factures Normals.

### Facturació

En aquestes factures totes les linies es facturen al client segons el signe que
tenen, és a dir, els valors positius es cobren i els negatius es descompten de la
factura.

## Anul·ladora (A)

### Ús

Una factura Anul·ladora es fa servir per desfer una factura que no s'hauria d'haber emés.

Per exemple, si des d'una distribuidora enviem una factura per una pòlissa a una
comercialitzadora que ja no té aquesta pòlissa, haurem de fer una anul·ladora.

El mateix passaria si des de comercialitzadora enviessim una factura a un client
que ha donat la seva pòlissa de baixa.

### Facturació

Com que aquestes factures són anul·ladores és facturen exactament al contrari que
les factures normals. Això vol dir que tots els camps positius són valors que s'han
de retornar al client, mentre que els camps negatius són descomptes que es van fer
al client que ja no apliquen, ja que la factura no era valida.

Per tant, tot i que estem fent una factura per retornar els diners al client, el més
normal és que el total estigui en positiu.

## Anul·ladora amb rectificadora (B)

### Ús

Les factures Anul·ladores amb Rectificadora funcionen de manera molt similar a les
Anul·ladores. La principal diferencia és que les factures Anul·ladores amb
rectificadora sempre van acompanyades d'una Rectificadora.

Aquestes factures s'utilitzen per tal de refacturar una factura que s'ha emés amb
dades incorrectes. Per exemple, si hem facturat una quantitat incorrecte d'energia
podem crear una factura Anul·ladora amb Rectificadora i una Rectificadora per tal
de facturar l'energia correcte.

La funció de les factres Anul·ladores amb Rectificadora és la d'anular la factura
original, de manera que el balanç sigui 0.

**NOTA: A partir del 31/07/17 aquestes factures ja no es fan servir per enviar les
factures amb F1, sinó que s'han substituit per Rectificadora sense anuladora (RA).
Tot i això, es poden seguir utilitzant per facturar a clients.**

### Facturació

A nivell de facturació, les factures Anul·ladores amb rectificadora funcionen
exactament igual que les factures Anul·ladores.

## Rectficadora (R)

### Ús

Tal com s'explica a les factures Anul·ladora amb rectificadora, les factures les
factures Rectificadores i les Anul·ladores amb rectificadora sempre van aparellades.

La funció de la parella és la de compençar una factura que s'ha emés amb dades
incorrectes i facturar els valors que s'haurien d'haber facturat. Un cop hem
compençat la factura original amb l'Anul·ladora amb Rectificadora, la factura
Rectificadora ens servirà per facturar els valors correctes.

**NOTA: A partir del 31/07/17 aquestes factures ja no es fan servir per enviar les
factures amb F1, sinó que s'han substituit per Rectificadora sense anuladora (RA).
Tot i això, es poden seguir utilitzant per facturar a clients.**

### Facturació

A nivell de facturació, les factures Rectificadores funcionen igual que les factures
Normals, ja que s'està facturant el que s'hauria d'haber facturat inicialment.

## Rectificadora sense anuladora (RA)

### Ús

Aquestes factures tenen la mateixa funcionalitat que la parella de Anul·ladora amb
Rectificadora i Rectificadora. És a dir, s'utilitzen per tal de facturar correctament
una factura que en el seu moment es va facturar amb valors incorrectes.

A partir del 31/07/17, amb els nous formats de gestió ATR, els F1 de rectificació
s'han d'enviar amb aquest format.

### Facturació

A l'hora de facturar, aquestes factures realitzen les funcions tant de les factures
Anul·ladores amb Rectificadora com de les Rectificadores.

Si mirem les linies de la factura, veurem que són les que s'haurien d'haber facturat
en el seu moment. Totes aquestes linies és sumen per tal de calcular el total de la
factura. Aquesta és la part que fa de rectificadora en la factura.

Tot i això, encara hem de fer la part de la anul·ladora. Per tal de fer-ho
considerarem que tot el que s'ha pagat en la factura original serveix com a
pagament de la nova factura. D'aquesta manera, en la nova factura només s'haurà de
pagar la diferencia entre el que es va pagar i el que s'hauria d'haber pagat.
Aquesta diferencia s'indica en el camp "Residual".

#### Refacturar per un total superior

En aquest apartat s'explica com queden els valors si estem refacturant una factura
i el nou total que hem de facturar és superior al que haviem facturat originalment.

Per exemple, imaginem que teniem una factura original on cobravem *10€*. Tot i això,
després d'obrir la factura ens adonem que en realitat s'haurien d'haber facturat
*15€*. Com que ja hem emés la primera factura, hem de refacturar. Suposem que per
tal de refacturar generem una Rectificadora sense Anuladora.

Aquesta nova factura tindrà un total de *15€*, ja que aquest és el valor que hauriem
d'haber facturat. Tot i això, com que ja s'han facturat *10€* en la factura
anterior, només falten *5€* a facturar. És per això que el camp "Residual" de la
factura tindra un valor de *5€*.

#### Refacturar per un total inferior

En aquest apartat s'explica com queden els valors si originalment vam facturar més
del que s'hauria d'haber facturat.

Per exemple, imaginem que hem emés la una factura original de *10€* igual que en
l'apartat anterior, però que en aquest cas s'haurien d'haber facturat *6€*. Això vol
dir que s'han facturat *4€* més dels que s'haurien d'haber facturat.

En aquest cas la nova factura tindrà un total de *6€*, ja que això és el que
s'hauria d'haber facturat. Tot i això, com que originalment s'han facturat *10€*
això vol dir que s'han de tornar *4€* al client. És per això que el camp "Residual"
tindrà un valor de *-4€*, indicant que s'han de tornar *4€* al client.
