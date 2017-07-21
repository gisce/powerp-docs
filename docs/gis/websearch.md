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
- (LAT) Girona: Mostra totes les LAT de Girona
- (LAT) Girona ET Riu Güell: LATs que començin o acabin a la ET Riu Güell

## Tram AT
- CINI
- Linia Alta Tensió
- Descripció de la línia
- Origen de la línia
- Final de la línia
- Municipi de la línia
- Tensió de la línia
- Data APM(permet buscar per any)
- Codi(Permet "TZ-001-25" o 2TZ-001 25")
- Origen
- Final
- Codi del cable
- Secció del cable
- Material del cable
- Circuit

### Exemples de cerca
- (Tram AT) CT Riu Güell : Trams que surten o finalitzen al CT Güell
- (Tram AT) Al Girona: Mostra els trams que tenen material Alumini(Al) i que estan al municipi de Girona 

## Suport AT
- Codi(Permet "LA-001-1" o "LA-001 1")
- Línia
- Codi poste
- Altura del poste
- Esforç del poste

### Exemples de cerca
- (Suport AT) SMC-012 : Suports de la linia SMC-012
- (Suport AT) SMC-012 PFUZ : Suports de la linia SMC-012 que tenen poste PFUZ 

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
- Voltatge(Cal afegir la V de volts al final)
- Data APM(En format yyyy-mm-dd, permet usar "-" o "/" com a separador)(permet buscar per any)

### Exemples de cerca
- (LBT) CT-001 : Mostra les LBT del CT-001

## CT
- CINI
- CT
- Descripció
- Municipi
- Potència Total del CT (Cal afegir kVA al final)
- Adreça
- Data APM(permet buscar per any)
- Tensió primari (Cal afegir V al final)
- Circuit

### Exemple de cerca
- (CT) Salt: Cerca tots els CTs de Salt
- (CT) Salt 2003: Cerca tots els CTs de Salt que es van donar d'alta el 2003

## Transformador
- CINI
- Numero de transformador
- Numero de fabricacio
- Marca
- Connexio UNE
- Potencia nominal (Cal afegir kVA al final)
- Estat
- Data APM(permet buscar per any)

### Exemples de cerca
- (Transformador)  A.E.G: Transofrmadors de la marca A.E.G

## Escomeses
- Node Id
- Municipi
- Tipus(No permet cercar si es CONTA-S CONTA-SS  o CONTA-Q)

### Exemples de cerca
- (Escaomesa) Seva : Escomeses de Seva
- (Escomesa) CONTA-AT: Escomeses de tipus CONTA-AT

## CUPS
- CUPS
- Municipi
- Polissa
- Nº de comprador
- Direcció Principal
- Titular
- Zona
- Ordre
- ET
- Linea
- Escomesa

### Exemples de cerca
- (CUPS) Rius: Tots els CUPS amb un titular que es digui Rius
- (CUPS) Girona: Tots els cups del municipi de Girona

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
