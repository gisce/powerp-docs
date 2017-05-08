

## Inventari 4666

### Introducció

Aquest mòdul permet la generació dels formularis de la Resolució 4666 relatius
a l’inventari de les instal·lacions en format TXT.

El mòdul permet generar 8 fitxers .txt corresponents als NODES descrits a la
resolució 4666.


!!! note
    Relacionats amb aquest módul hi ha el módul de subestacions, cel·les i
    elements de tall, despatxos, posicions, Catàleg de cables AT,
    Catàleg de cables BT, Expedients i Condensadors.

!!! note
    S'han de unificar els CINI's als publicats a la resolució 4666/2016

!!! note
    A totes les fitxes s'ha inclós el camp `CNMC Tipus Instal·lació` i el
    camp `Bloquejar CNMC Tipus Instal·lació`. Amb aquest camp es poden
    intorduïr els camps **TI-XXX** que es defineixen a la *Taula 3* de la
    resolució 4666. Si es marca la variable de bloqueig, cap automatisme de
    càrrega o modificació automàtica del camp `CNMC Tipus Instal·lació`
    modificarà el valor actual.

!!! note
    Els informes de Maquines i condensadors s'han d'unificar en un sol
    fitxer. S'han separat en dos per facilitar-ne la
    seva traçabilitat

!!! note
    El camps que s'usara com a Tipus d'instal·lacio es el Tipologia CNMC(desplegable)

### Carrega de fitxers de la 4771

Per tal que el ERP pugui fer el calcul del camp estat de la 4666 del 2016 s'ha de
carregar els fitxers presentats en la 4771. El format del ftixer que s'ha de
carregar es format ZIP en el cual a l'arrel del fitxer hi hauran els 8 fitxers
entregats.

![](../_static/cnmc/4666/carrega_4771.png)

El menu de carrega es troba a "_Administració Pública/CNMC/Resolucions/Resolucio
4666/2016/Carregar Fitxer presentat 4771_"

### Carrega de fitxers 4666

Per tal que el ERP pugui fer el calcul del camp estat de la 4666 del any 2017
s'han de carregar els fitxers presentat de la 4666 del 2016. El fromat dels
fitxers que s'han de carregar es format ZIP en le cual a l'arrel del fitxer hi
hauran els 8 fitxers entregats(no incloure el fitxer de transmisions).

** Els fitxers han d'esta en codificacio UTF-8 **

El menu de carrega es troba a "_Administració Pública/CNMC/Resolucions/Resolucio
4666/2016/Carregar Fitxer presentat 4666 n-1_"

![](../_static/cnmc/4666/load_4666.png)
