# Camps indexats

## Linia AT
- Codi (name)
- Descripció (descripcio)
- Origen (origen)
- Final (final)
- Municipi (municipi.name)
- Tensió (tensio)
- Expedient(expedients)

## Tram AT
- CINI (cini)
- Linia Alta Tensió (linia.name)
- Descripció de la línia (linia.descripcio)
- Origen de la línia (linia.origen)
- Final de la línia (linia.final)
- Municipi de la línia (linia.municipi.name)
- Tensió de la línia (linia.tensio)
- Data APM (data_pm)
- Codi (name)
- Origen (origen)
- Final (final)
- Codi del cable (cable.name)
- Secció del cable (cable.seccio)
- Material del cable (cable.material.name)
- Circuit si hi ha el modul de mapeig

## Suport AT
- Codi (name)
- Línia (linia.name)
- Codi poste (poste.name)
- Altura del poste (poste.altura)
- Esforç del poste (poste.esforc)

## LBT
- CINI (cini)
- Codi (name)
- Codi CT (ct.name)
- Descripció del CT (ct.descripcio)
- Municipi (municipi.name)
- Número de línia (num_linia)
- Cable (cable.name)
- Secció del cable (cable.seccio)
- Material del cable(cable.material.name)
- Voltatge (voltatge)
- Data APM (data_pm)

## CT
- CINI (cini)
- CT (name)
- Descripció (descripcio)
- Municipi (id_municipi.name)
- Potència Total del CT (potencia)
- Adreça (adreca)
- Data APM (data_pm)
- Tensió primari (tensio_p)
- Circuit (si hi ha el modul de mapeig instal·lat)

## Transformador
- CINI (cini)
- Numero de transformador (name)
- Numero de fabricacio (numero_fabricacio)
- Marca (id_marca.name)
- Connexio UNE (id_connexioune.name)
- Potencia nominal (potencia_nominal)
- Estat (id_estat.name)
- Data APM (data_pm)

## Escomeses
- Node Id (name)
- Municipi (id_municipi.name)
- Tipus (blockname.name)

## Cups
- CUPS (name)
- Municipi (id_municipi.name)
- Polissa (polissa_polissa.name)
- Nº de comprador (polissa_comptador)
- Direcció Principal (direccio)
- Titular (Si hi ha el modul giscedat_cups_titular)
- Zona (zona)
- Ordre (ordre)
- ET (et)
- Linea (linia)
- Escomesa (id_escomesa.name)

## Interruptors AT
### Seccionador unifilar
- Codi (codi)
- Tipus (blockname.name)

### Seccionador AT
- Codi (codi)
- Tipus (blockname.name)

### Fusible AT
- Codi (codi)
- Tipus (blockname.name)

### Interruptor AT
- Codi codi
- Tipus (blockname.name)

## ADU DSP
- Codi (codi)
- Blockname (blockname.name)

## Nodes
- IDNode (Name)

## Fusibles BT
- Codi (codi)
- Tipus (blockname.name)

## Interruptors BT
- Codi (codi)
- Tipus (blockname.name)
