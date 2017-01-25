# Camps indexats


## Linia AT
- name
- descripcio
- origen
- final
- municipi.name
- tensio
- data_pm
- expedients

## Tram AT
- cini
- linia.name
- linia.descripcio
- linia.origen
- linia.final
- linia.municipi.name
- linia.tensio
- data_pm
- name
- origen
- final
- cable.name
 -cable.seccio
- cable.material.name
- Circuit si hi ha el modul de mapeig

## Suport AT
- name
- linia.name
- poste.name
- poste.altura
- poste.esforc

## LBT
- cini
- name
- ct.name
- ct.descripcio
- municipi.name
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
