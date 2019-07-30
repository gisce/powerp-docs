# Linies extra

## Concepte

## Topoligia

### Base de dades

account_id            | 1264
amount_invoiced       | 9.040000
price_unit            | 9.040000
price_subtotal        | 9.040000
polissa_id            | 5764
term                  | 1
price_term            | 9.040000
date_to               | 2015-10-30
tipus                 | altres
name                  | Derechos de enganche
date_line_from        | 2015-10-30
product_id            | 289
total_amount_invoiced | 9.040000
total_amount_pending  | 0.000000
date_from             | 2015-10-30
date_line_to          | 2015-10-30
quantity              | 1.000
notes                 | Creada desde la factura de proveedor con id: 260                                                                              +
                      | Fichero XML:
amount_pending        | 0.000000


### Camps funció



## Facturació de linies extra
Tenint en compte que la facturació es pot fer de manera manual o automatica,
la facturació de linies extra divergeix en aquestes dos maneres.

## Factura manual

Al realitzar una factura manual a través de l'assistent de factura manual, s'ha
de seleccionar que es vol incloure les linies extra, un cop seleccionada la
opció si tenim la variable de configuració ***fact_autofill_manual_wizard***
activada es posaran automaticament les dates per incloure les linies extra
pendents.

![](_static/lineas_extra/config_autofill_manual.png)

En cas de posar les dates manualment, es facturaran les linies extra que
tinguin la **data d'inici** (***date_from***) o la **data final** (***date_to***)
dins el periode que es vol facturar.

![](_static/lineas_extra/manual_invoice_1.png)

![](_static/lineas_extra/manual_invoice_2.png)

![](_static/lineas_extra/manual_invoice_3.png)

!!! warning "Atenció"
    Cal tenir en compte que les dates inclouran totes les linies extra, peró a la hora de generar la factura es fara una segona validació i només facturara les que compleixin les condicións estipulades a l'apartat de
    **Condicións de facturació**.

## Facturacio automatica

### Condicións de facturació

Quan es genera una factura de manera **automàtica** o **manual**, l'**ERP**,
fa una cerca de les linies extra relacionades amb el contracte amb les següents condicions:

- Linies extra on la **data de la factura**(***date_invoice***) està **entre**
la **data desde**(***date_from***) i la **data fins**(***date_to***), es
a dir amb data de factura entre els periodes de les linies extra.

- Linies extra amb **data fins**(***date_to***) anterior a
la **data de la factura**(***date_invoice***) amb **pendent a
facturar**(***total_amount_pending***) **diferent** de **0**, es a dir
totes aquelles linies extra que no s'han acabat de facturar i fora de plaç.


Un cop obtinguedes les **linies extra** corresponents a les cerques
anteriors, es fa un segon filtre segons les dades de la factura on anaven
a ser incloses i s'afegiran a la factura si compleixen les següents condicions:

- En cas de que sigui una **factura normal** (***tipo_rectificadora = N***), el
**diari** (***journal_id***) de la **factura**, ha de coincidir amb algun dels
**diaris** (***journal_ids***) de **linia extra**.

- En cas de que sigui una factura **rectificadora**
(***tipo_rectificadora = R***), el **diari** (***journal_id***) de
la **factura referenciada** (***factura.ref***),
ha de coincidir amb algun dels **diaris** (***journal_ids***)
de **linia extra**.


**Mètodes**: ***fact_via_lectures()*** &rarr; ***compute_extra_lines()***

!!! warning "Atenció"
    Només es facturaran les linies extra on el total pendent
    arrodonit a 2 decimals sigui diferent de 0.

## Generació de linies de la factura i facturació per termes

En referencia a l'apartat anterior, un cop filtrades les linies extra a
facturar, es generen les linies de la factura en funció de la informació
especificada en la linia extra i el que tocaria facturar.

El preu de la línia de la factura, es calculara en funció de la quantitat, el
pendent a facturar i el preu per terme:

    - Si el pendent a facturar és inferior al preu per terme o unitat, s'afegira
    a la línia de la factura tot el que queda per facturar.

    - Si la **data de la factura** (***date_invoice***) és **posterior o igual**
    a la **data de finalització de la línia extra** (***date_to***), s'afegira
    tambe a la factura tot el pendent a facturar.

    - En la resta de casos, afegeix a la factura una linia amb...

    !!! warning "Atenció"
        Els impostos de la linia de la factura, es calcularan en funció
        dels impostos definits a la línia extra.
