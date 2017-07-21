# Documentació dels mòduls de dins de CNMC

Continguts:

* [INF/DE/0066/44](#modul-per-generar-el-fixer-csv-segons-cnmc-infde006644-per-distribuidora)
* [Circular 1/2005](resoluciones/circular_1-2005.md#circular-12005)
* [Circular 4/2014](resoluciones/circular_4-2014.md#circular-42014)
* [Circular 4/2015](resoluciones/circular_4-2015.md#circular-42015)
* [Circular 2/2016](resoluciones/circular_2-2016.md#generacio-de-informes-sobre-reclamacions-de-consumidors)
* [Inventari 4131 (2014)](resoluciones/4131.md)
* [Inventari 4666](resoluciones/4666.md#inventari-4666)
* [Plans d'inversió 4667](resoluciones/4667.md)


## Mòdul per generar el fixer CSV segons CNMC INF/DE/0066/44 per distribuïdora

### Introducció

Per poder fer una auditoria de canvis de comercialitzadora, la CNMC demana un
CSV amb el format definit a INF/DE/0066/14

### Generació

Per generar el fitxer, hem d'executar l'assistent que trobarem a
**Administració pública > CNMC > Informe INF/DE/0066/14**

![](../_static/cnmc/inf_de_0066_14/menu.png)

Només caldrà introduïr l'any del qual es vol fer l'informe, que per defecte ja
és 2013 i prèmer el botó **Exportar**.

Des de **Fitxer** es podrà obrie el CSV i descarregar-lo a disc

![](../_static/cnmc/inf_de_0066_14/assistent.png)

### Dades utilitzades

Per omplir el fitxer es tenen en compte totes les pólisses creades dins l'any
escollit que tinguin la corresponent modificació contractual de tipus `alta`.

Així doncs, el fitxer generat serà correcte si les altes a la comercialitzadora
es registren com a modificació contractual de la pòlissa de tipus `alta`
correctament.

| Nom del camp               | Valor del camp                                 |
|----------------------------|------------------------------------------------|
| **CODIGO_INFORMANTE**      | Camp `Codi R2` de la companyia                 |
| **CODIGO_CUPS**            | CUPS                                           |
| **FECHA_ACTIVACION**       | Data inici de la modificació contractual nova  |


!!! note
    Codi R2 (R2-xxx) de la CNMC gestionable en el camp `Ref2` de la fitxa de
    l'empresa comercialitzadora accessible des del menú `Empreses`

--------------------------------------------------------------------------------

## Fitxers d'intercanvi

Pels usuaris de GISCE-ERP que no utilitzin el mòdul de facturació de distribució
es defineixen uns fitxers d'intercanvi per actualitzar dades referents als
formularis amb següent format.

### Format CUPS CSV

* Sense capçalera
* Columnes separades per punt i coma (**;**) i sense cometes.
* El separador de decimals de les **energies i la potencia** serà un
 **punt (.)**

Camp                             | Descripció
:--------------------------------|:----------------------------------------------
CUPS                             | Codi universal del punt de subministrament
Energia activa anual consumida   | Energia activa anual facturada el 2014
Energia reactiva anual consumida | Energia reactiva anual facturada el 2014
Potencia facturada               | Potencia facturada el mes 12 any circular o si la pòlisa està de baixa, l'últim mes facturat
Número de lecturas any circular  | Número de lectures d'activa efectuadas en l'any de la circular.

### Format Comptadors CSV

* Sense capçalera
* Columnes separades per punt i coma (**;**) i sense comentes.


Camp            | Descripció
:---------------|:----------------------------------------------
Número de sèrie | Número de sèrie del comptador
CINI            | Codi CINI del comptador
