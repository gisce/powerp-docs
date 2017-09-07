# Liquidació de peatges

El sistema suporta tots els sistemes de liquidació vigents:

* Facturació peatges desglosats
* Facturació últim recurs
* Tancament liquidacions per consum
* Facturació a tarifa d'accés per frau

A través del menú de **Liquidacions** podem llistar les diferents liquidacions.

![](_static/liquidacion_peajes/liquidacio_menu_general.png)

!!!note
    L'únic sistema que es genera de forma automàtica és el de liquidació per
    facturació de peatges. Veure [Generar les liquidacions després de facturar](#generar-les-liquidacions-despres-de-facturar)

## Llistar liquidacions

Podem veure totes les liquidacions que tenim fetes, anant al menú general de **Liquidacions**
i apretant al sistema de liquidacions que volguem veure.

Per exemple: Les liquidacions de facturació per peatges

![](_static/liquidacion_peajes/listado_peajes.png)

En el llistat podem veure totes les liquidacions que tinguem i filtrar per **mes**,
**any** i **estat** de la liquidació.

!!!note
    Al finalitzar l'any es generen totes les liquidacions en estat **esborrany**
    pel pròxim any, per tant ens sortirant totes les liquidacions encara que no
    tinguem facturat encara aquell període.

## Estats d'una liquidació

blockdiag {
  b[label = "Borrador"];
  l[label = "Para liquidar"];
  e[label = "Enviado"];
  c[label = "Cerrado"];
  r[label = "Rectificado"];
  co[label = "Corregido"];
  b -> l -> e -> c;
       l -> r -> co -> e;
       l -> r -> co -> e [folded];
}

## Formulari d'una liquidació

En el formulari d'una liquidació ens surt totes les tarifes que hem facturat amb
les seves corresponents quantitats: número de clients, energia facturada, euros
facturats, etc.

![](_static/liquidacion_peajes/formulario_liquidacion.png)

També podem fer vàries accions:

* **(1) Previsualitzar l'XML**: Ens servirà per generar l'XML que hem d'enviar a la CNMC
* **(2) Validació**: Ens passa les mateixes validacions que fa la CNMC
* **(3) Per liquidar**: Podem marcar la liquidació "Per liquidar" i així avançar en
  el [fluxograma d'estats d'una liquidació](#estats-duna-liquidacio)
* **(4) Informe de liquidació**: En el cas que no pugem directament l'XML podem generar
  aquest informe per tal d'entrar les dades.
* **(5) Exportar liquidació (CSV)**: Ens permet exportar en format CSV la liquidació

## Generar XML

Es pot generar l'XML des del formulari d'una liquidació amb el botó **Previsualitzar l'XML**.
Ens mostra l'XML que generarà i només hem d'apretar el botó resaltat a la següent captura de
pantalla:

![](_static/liquidacion_peajes/exportar_xml.png)

## Relació factures amb el període de liquidació

Totes les factures d'energia de peatges, tenen un camp que vincula la factura amb
el **període de liquidació CNMC**

![](_static/liquidacion_peajes/liquidacio_field.png)

Aquest camp s'omple automàticament (si no es força amb un altre valor) al període
de liquidació vigent (dia 16 d'un mes fins al dia 15 del mes següent).

En el cas d'una factura anul·ladora/rectificadora. En el moment de generar-la ens
demanarà a quin període de liquidació la volem assignar.

![](_static/liquidacion_peajes/liquidacio_refund.png)

## Generar les liquidacions després de facturar

Es pot trobar l'assistent per generar la liquidació a través del menú
**Liquidacions > Generar liquidacions a partir de les factures**

![](_static/liquidacion_peajes/liquidacio_menu.png)

L'assistent ens demana quin període volem generar

![](_static/liquidacion_peajes/generar_liquidaciones.png)

Aquest asistent agafarà totes les factures que compleixin les següents condicions:

* Estiguin vinculades al diari **ENERGIA.X** (sigui normal, anul·ladora o rectificadora)
* Estiguin vinculades amb el **període de liquidació** que volem generar
* Tinguin l'estat **obert** o **pagat**

Un cop acabada l'agrupació de factures ens mostrarà que ja ha acabat la liquidació
i la podem veure apretant el botó **Mostrar liquidació**

![](_static/liquidacion_peajes/liquidacion_generada.png)

!!!note
    Podem anar regenerant la liquidació tantes vegades com volguem mentres estigui
    en estat **esborrany** que ens confirmarà si volem tornar a generar.

## Generar Liquidacions Suplements Territorials ETU/35/2017

Les liquidacions per als Suplements Territorials de la ETU/35/2017 es realitzen
mitjançant un fitxer separat a la resta de liquidacions per informar a la CNMC
únicament d'aquests suplements.

Aquestes liquidacions consten de dos fitxers:

- Liquidacions Mensuals, anomenats sota el format "STM\__aaaamm_._eeee_.xml"
    - S'han d'enviar mensualment, juntament amb els altres fitxers de liquidacions
- Liquidacions Anuals, anomenats sota el format "STA\__aaaa_._eeee_.xml"
    - S'ha d'enviar una sola vegada quan s'hagin cobrat totes les línies amb
      Suplement Territorial (aproximadament al Septembre de 2018)

Per generar aquests fitxers cal tenir instal·lat el mòdul: **giscedata_liquidacions_etu35_2017**

Aquest mòdul ens facilita dos assistents diferents, un per les liquidacions Mensuals
i un per les liquidacions Anuals. Podem trobar els assistents en l'ERP en la direcció
"**Menú OpenERP > Liquidacions**"

![](_static/liquidacion_peajes/liquidacion_menu_etu.png)

### Liquidacions Mensuals ETU/35/2017

Aquestes liquidacions s'han de generar una vegada cobrades les diferents factures
amb els Suplements Territorials del mes corresponent, de la mateixa manera que es
liquida l'energia facturada (fins a 15 dies de la facturació).

Utilitzant l'assistent especificat en l'apartat anterior, únicament ens fa falta
saber quin mes volem liquidar. Aquest assistent utilitza el lot de facturació per
sel·leccionar les factures amb Suplements per un mes en concret.
Podem escriure el mes amb el format "_mm/aaaa_" o bé podem polsar el botó de lupa
i sel·leccionar el lot de facturació corresponent.

![](_static/liquidacion_peajes/wizard_etu_mes.png)

Una vegada sel·leccionat el mes adequat, podem polsar el botó "_Crear_" i ens
generarà el fitxer XML amb el format especificat per la CNMC.

![](_static/liquidacion_peajes/wizard_etu_crear.png)

Una vegada generat, els camps amb el nom del fitxer i fitxer generat
s'actualitzaràn permetent mostrar el fitxer en la carpeta que es troba, obrir-lo
o bé guardar-lo en un directori específic.

![](_static/liquidacion_peajes/wizard_etu_generat.png)

!!! note
    En cas de perdre el nom del fitxer, es disposa del camp "_Nom del Fitxer_"
    que no es pot modificar.
