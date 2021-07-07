## RepartiBé

### Menú, localització i funcionalitats

#### Menú de correos - Repartibé

![alt text](_static/repartimbe/menu_correos.png "Localització del menú")

#### Llistat de remeses

![alt text](_static/repartimbe/llistat_remeses.png "Llistat remeses")

#### Formulari remesa

![alt text](_static/repartimbe/form_remesa.png "Form remesa")

#### Línies d'una remesa

![alt text](_static/repartimbe/link_linies.png "Ir a las lineas de una remesa")

**Verd &rarr; entregada || Vermell &rarr; No entregada**
![alt text](_static/repartimbe/llistat_linies_remesa.png "Llistat linies remesa")

### Circuit i funcionament

#### Primer pas - Crear remesa amb factures impagades
Per crear una nova remesa, s'ha de fer a traves del llistat de remeses del menú de correus mitjançant el botó new.

![alt text](_static/repartimbe/crear_remesa_listado.png "Nueva remesa 1")

![alt text](_static/repartimbe/nueva_remesa.png "Nueva Remesa 2")


Per afegir les factures impagades, ho farem des del llistat de factures (factures o invoices), encara que serà obligatori que les invoices seleccionades tinguin una factura d'energia associada.

![alt text](_static/repartimbe/filtrar_facturas_impagadas.png "Filtrar Facturas Impagadas")

![alt text](_static/repartimbe/action_afegir_linies.png "Action añadir facturas")

Un cop seleccionada l'acció, apareixera la primera pantalla de l'assistent, on podrem seleccionar la ramesa a la que s'afegiran les factures (Només es podran afegir a remeses en esborrany).

![alt text](_static/repartimbe/afegir_wiz_1.png "Añadir facturas - Selección remesa")

![alt text](_static/repartimbe/afegir_wiz_2.png "Añadir facturas - Información")

![alt text](_static/repartimbe/afegir_wiz_3.png "Añadir facturas - Pantalla final")

Un cop finalitzat el procés, la remesa seleccionada ja tindra les linies
corresponents a les factures que hem afegit.

![alt text](_static/repartimbe/link_linies.png "Ir a las lineas de una remesa")

![alt text](_static/repartimbe/lineas_remesa.png "Lineas de una remesa")


#### Segon pas - Generar fitxer d'enviament
Per generar el fitxer d'enviament, cal accedir a la remesa per la qual es vol
generar i utilitzar l'acció corresponent.

![alt text](_static/repartimbe/wiz_export_1.png "Asistente exportación pantalla 1")

A la primera pestanya, apareixerà una casella de verificació
(**Següent estat**), si aquesta esta marcada, s'avançaran els estats de les
factures que apareixin en els fitxers generats i les linies corresponents es
marcaran com a exportades auttomaticament.

En cas que per algun error no es pugui generar el fitxer per alguna factura,
aquestes no apareixeran a cap dels fitxers, no avançara l'estat d'impagat ni es marcara com a exportat, al la pantalla final informara d'aquests errors.

Cal tenir en compte que les linies ja exportades o amb factures ja pagades no apareixeran en el fitxer generat, ni s'avançara l'estat encara que la casella
estigui marcada.

![alt text](_static/repartimbe/wiz_export_2.png "Asistente exportación pantalla 2")

A la pantalla final s'haura de descarregar els dos fitxers generats (xls i pdf)

**Atenció, assegureu-vos de descarregar el fitxer sino després sera dificil generar-lo de nou!!**

![alt text](_static/repartimbe/export_file_xls.png "Fichero xls")

![alt text](_static/repartimbe/export_file_pdf.png "Fichero pdf")

Un cop exportats amb la casella marcada, les factures afectades i les línies hauran canviat d'estat.

**Facturas afectadas**

![alt text](_static/repartimbe/move_facturas.png "Facturas Pendiente cambiado")

**Lineas de la remesa afectadas**

![alt text](_static/repartimbe/move_lines.png "Líneas Pendiente cambiado")

#### Tercer pas - Importar fitxers de recepció

Per importar els fitxers de recepció, cal fer-ho a través de l'assistent
que es troba en el menú de correos.

![alt text](_static/repartimbe/wiz_imp_loc.png "Asistente importación Localizacion")

A la primera finestre de l'asistent permet seleccionar el fitxer:

![alt text](_static/repartimbe/wiz_imp_1.png "Asistente importación 1")

Suposem el seguent fitxer de retorn relacionat amb les factures anteriors, on el
codi 1 es carta entregada i el 6 carta rebutjada, en el primer cas la linia
pasara a estat entregat i la factura canviara el seu estat a avís, per el contrari el segon cas el client a rebutjat la carta per tant l'estat de la factura pasara a pendent carta 2 per seguir el procés. En els dos casos a les linies s'actualitzara l'estat de recepció i la data de canvi d'estat i és consideraran entregades ja que els dos l'hauran rebut.

![alt text](_static/repartimbe/rec_file.png "Fichero respuesta")

En cas que hi hagués hagut algun error, s'informaria a la pantalla final.

![alt text](_static/repartimbe/wiz_imp_2.png "Asistente importación pantalla final")

**Facturas Actualitzades**

![alt text](_static/repartimbe/factura_avis_codi_1.png "Avis")
![alt text](_static/repartimbe/factura_pendent_2_codi_6.png "carta 2")


**Linies Actualitzades**

![alt text](_static/repartimbe/lines_updated_after_import.png "Asistente importación pantalla final")

Arribat a aquest punt, ja tindriem totes les factures de la remesa exportades
i entregades i caldria donar-la per tancada.

En el cas de la factura que s'ha quedat en estat **pendent carta 2** hauriem
d'afegir-la a una nova remesa i tornar a començar el process per la segona
carta en aquest cas.
