# Camps de cerca

## Introducció

El GIS disposa de un motor de cerca que permet buscar elements.

En el cas que no s'indiqui es cercara a tots els elements que continguin el text cercat.

Es recomana que en el cas d'obtindre molts resultats realitzar una cerca per tipus d'element.

## Linia AT
- Codi
- Descripció
- Origen
- Final
- Municipi
- Tensió
- Expedient

### Exemples de cerca
- (LAT) Granollers : Mostra totes les LAT de Granollers
- (LAT) Granollers 20000 : Mostra totes les LAT de Granollers donades d'alta el 2000

## Tram AT
- CINI
- Linia Alta Tensió
- Descripció de la línia
- Origen de la línia
- Final de la línia
- Municipi de la línia
- Tensió de la línia
- Data APM
- Codi
- Origen
- Final
- Codi del cable
- Secció del cable
- Material del cable
- Circuit si hi ha el modul de mapeig

### Exemples de cerca
- (Tram AT) 2000 : Trams amb Data APM del any 2000
- (Tram AT) CT-Birba : Trams que surten o finalitzen al CT Birba
- (Tram AT) Al Camprodon : Mostra els trams que tenen material Alumini(Al) i que estan al municipi de Camprodon 

## Suport AT
- Codi
- Línia
- Codi poste
- Altura del poste
- Esforç del poste

## LBT
- CINI
- Codi
- Codi CT
- Descripció del CT
- Municipi
- Número de línia
- Cable
- Secció del cable
- Material del cable
- Voltatge
- Data APM

## CT
- CINI
- CT
- Descripció
- Municipi
- Potència Total del CT
- Adreça
- Data APM
- Tensió primari
- Circuit (si hi ha el modul de mapeig instal·lat)

### Exemple de cerca
 - (CT) Tona: Cerca tots els CTs de Tona
 - (CT) Tona 2003: Cerca tots els CTs de Tona que es van donar d'alta el 2003

## Transformador
- CINI
- Numero de transformador
- Numero de fabricacio
- Marca
- Connexio UNE
- Potencia nominal
- Estat
- Data APM

## Escomeses
- Node Id
- Municipi
- Tipus

## Cups
- CUPS
- Municipi
- Polissa
- Nº de comprador
- Direcció Principal
- Titular (Si hi ha el modul giscedat_cups_titular)
- Zona
- Ordre
- ET
- Linea
- Escomesa

## Interruptors AT
### Seccionador unifilar
- Codi
- Tipus

### Seccionador AT
- Codi
- Tipus

### Fusible AT
- Codi
- Tipus

### Interruptor AT
- Codi
- Tipus

## ADU DSP
- Codi
- Blockname

## Nodes
- IDNode

## Fusibles BT
- Codi
- Tipus

## Interruptors BT
- Codi
- Tipus
