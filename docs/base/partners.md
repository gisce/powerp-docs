# Clients/Empreses

Els abonats de GISCE-ERP es defineixen com Empreses, tant si són Clients o Proveïdors.
En el sistema ERP un Client pot tenir diferents pólisses. S'hi pot accedir a totes
des de la pestanya **pòlisses** del formulari del client.

## Donar d'alta un Client/Empresa

Es pot donar d'alta una empresa des de dos llocs diferents:

* Des de la llista d'Empreses: "_Menú → Empreses → Empreses_" i llavors es
  sel·lecciona el botó **Nou**.
* Des del formulari d'una pòlissa amb el botó **Nou Registre** en el camp _Client_.

En els dos casos s'ha d'emplenar la informació corresponent a:

* Pestanya General
  * Nom del Client
  * Codi (En el cas de que sigui una Comercialitzadora s'ha de posar el seu codi REE)
  * Direcció de contacte (Hi pot haver més d'una direcció segons el tipus
    (Contacte, Facturació, Entrega, Altres, Descàrrec))
* Pestanya Informació Extra
  * NIF/CIF
* Pestanya Propietats (en el cas de que sigui una Comercialitzadora)
  * Compte a cobrar: 400
  * Compte a pagar: 440
  * Plaç de pagament: 20 dies
  * Impost predefinit: IVA 16% (el que no indica "soportado")
  * Tipus de pagament: A definir per cada empresa

## Donar de baixa un Client/Empresa

Els contactes o empreses relacionats amb la companyia normalment no es donaràn
mai de baixa, ja que són informació important. En el cas de que sigui un abonat,
el que s'ha de fer és [donar de baixa la pòlissa](polizas.md#donar-de-baixa-una-polissa)
d'aquest abonat.

## Canviar l'IVA de facturació a una Comercialitzadora

Per canviar l'IVA de facturació a una comercialitzadora s'ha d'anar a la pestanya
_Propietats_ i canviar el camp _Impost per Defecte_.
