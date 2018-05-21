# Generació i enviament de XML's


## Generació del fitxer

El fitxers XML es generen a partir de la informació del pas actual, es a dir,
el pas en el qual està el cas.
Alguns agents, reclamen els XML's en format **ISO-8859-1** en comptes de UTF-8.
GISCE-ERP permet configurar-les per a utilitzar aquesta codificació mitjançant
el camp **Encoding XML switching** de la pestanya **Ventas y Compras** de la
fitxa de l'empresa corresponent.


##### Camp per modificar la codificació XML a la fitxa d'empresa
![](../_static/atr/EncodingXML.png)

Per intercanviar XML's tenim dues opcions:

* **Exportar XML**: Crea un ZIP amb tots els XML's seleccionats o un sol XML si
  només és un cas
* **Enviar XML**: En via el XML per mail al destinatari


### Exportar XML

Es genera el fitxer XML d'un pas per poder-lo emmagatzemar en l'ordinador de
l'usuari i enviar-lo al receptor per altres vies. Si s'utilitza aquesta opció,
no es podrà fer un seguiment de l'intercanvi de informació amb el destinatari
automàticament si no s'utilitzen les utilitats d'historització del CRM
(``Pestanya General``)


##### Formulari per exportar un fitxer XML
![](../_static/atr/FormulariExportarXML.png)

* **Passos**: Podrem escollir el pas del qual volem generar l'XML
* **Marca com enviat**: Es marcaran com a enviats tots els passos que es
  generin. D'aquesta forma ja no sortiran en el llistat de casos **pendents
  d'enviar**.

Prement al botó **Generar Fitxer** ens mostrarà un formulari per
descarregar-nos el fitxer.
El nom del fitxer generat tindrà el format
``PP_SS_OOOO_DDDD_YYYYMM_NNNNNNNNNNNNNNN_CCCCCCCCCCCCCCCCCCCCCC`` on:

* *[PP]*: Procés (C1,C2,M1)
* *[SS]*: Pas (01,02,...)
* *[OOOO]*: Codi REE de l'agent origen
* *[DDDD]*: Codi REE de l'agent destinatari o nom comercial
* *[YYYYMM]*: Any i mes de inici del procés
* *[NNNNNNNNNNNNNNN]*: Codi de sol·licitud
* *[CCCCCCCCCCCCCCCCCCCCCC]*: CUPS

!!! Tip "Consell"
    Si es vol que el camp destinitari *[DDDD]* contingui un nom d'empresa per
    facilitar la seva gestió, es pot configurar el nom comercial de la fitxa
    d'empresa segons es veu a la imatge següent


##### Camp *Nom comercial* a fitxa de l'empresa
![](../_static/atr/NomComercial.png)

Es pot exportar més d'un cas al mateix temps i es generarà un fitxer ZIP amb
tots els fitxers XML a l'interior. Això ens permet carregar un sol fitxer en
els portals dels agents que ho permeten.

Si es seleccionen casos de diferents destinataris, es generarà un zip per cada
empresa destinatària amb els seus XML's corresponents dins el mateix fitxer.
D'aquesta forma tindrem un fitxer comprimit que contindrà un fitxer ZIP per
cada agent destinatari diferent.

El nom dels fitxers ZIP de cada empresa seguirà el format
``OOOO_DDDD_YYYYMMDDHHMMSS`` on:

* *[OOOO]*: Nom de la base de dades de l'ERP, normalment nom empresa origen
* *[DDDD]*: Codi REE de l'agent destinatari o nom comercial
* *[YYYYMMMDDHHMMSS]*: Any, mes, dia, hora, minut i segon en el qual s'ha
  començat a generar el fitxer ZIP contenidor.


### Enviar XML


##### Formulari per enviar el XML del pas per mail des del Cas
![](../_static/atr/FormulariEmailXML.png)

Es pot utilitzar el PowerEmail per enviar els XML's i historitzar tot
l'intercanvi de informació generat.

* **Des de**: Compte de correu que es vol utilitzar per enviar el mail
* **Receptor (Per a)**: S'omple automàticament amb l'adreça de la pestanya
  Contactes
* **CC**: Compte de correu on es vol enviar una còpia
* **CCO**: Compte de correu on es vol enviar una còpia oculta
* **Passos**: Pas del qual es vol adjuntar l'XML
* Podrem escriure el contingut del mail que creguem necessari a l'àrea de text
  que hi ha a sota

El mail es veurà a la pestanya ``Communication`` per referències posteriors.

---
