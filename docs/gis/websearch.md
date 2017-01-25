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
- num_linia': lambda self, data: data and '{0} L{0}'.format(data) or '',
- cable.name
- cable.seccio
- cable.material.name
- voltatge': lambda self, data: data and '{0}V'.format(data) or '',
- data_pm

## CT
- cini
- name
- descripcio
- id_municipi.name
- potencia': lambda self, data: '{0}kVA'.format(data),
- adreca
- data_pm
- tensio_p': lambda self, data: '{0}V'.format(data)
- circuti-> si hi ha el modul de mapeig

## Transformador
- cini
- name
- numero_fabricacio
- id_marca.name
- id_connexioune.name
- potencia_nominal': lambda self, data: '{0}kVA'.format(data),
- id_estat.name
- data_pm

## Escomeses
- name
- id_municipi.name
- blockname.name

## Cups
- name
- id_municipi.name
- polissa_polissa.name
- polissa_comptador
- direccio
- titular Si hi ha el odul giscedat_cups_titular
- zona
- ordre
- et
- linia
- id_escomesa.name

## Interruptors AT
### Seccionador unifilar
- codi
- blockname.name

### Seccionador AT
- codi
- blockname.name

### Fusible AT
- codi
- blockname.name

### Interruptor AT
- codi
- blockname.name

## ADU DSP
- codi
- blockname.name

## Nodes
- Name

## Fusibles BT
- codi
- blockname.name

## Interruptors BT
- codi
- blockname.name
