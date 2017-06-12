# Circular 1/2005

El mòdul permet al GISCE-ERP la generació dels informes referents a la
circular 1/2005 de la CNMC. Aquests informes venen definits per la mateixa **CNMC**.

* [Anexo I: Instrucciones para completar la información solicitada en los
  formularios del Anexo II](https://sede.cnmc.gob.es/sites/default/files/2016-11/20161111_AnexoI_Circ_1_2005.pdf)
* [Anexo II: Formularios de envío de información de la  CNE](https://sede.cnmc.gob.es/sites/default/files/2016-11/20161111_AnexoII_Circ_1_2005.pdf)
* [Anexo III: Tablas Circular 1/2005](https://sede.cnmc.gob.es/sites/default/files/2016-09/AnexoIII_Circ_1_2005.xls)

## Actualment, aquest mòdul és capaç de generar els següents informes:


### **1:** Informe de sol·licituds de canvi de MR a ML i de comercialitzadora.

**Informe trimestral.**

1. Omplim el camp de la secció 'tipus de fitxer' amb el valor '1' del desplegable.
2. Omplim els camps de la secció 'periode del trimestre' amb la data inicial i
   data final del trimestre.
3. Premem el botó 'exportar' per generar l'informe.
4. Quan s'ha generat l'informe apareix la secció 'nom del fitxer' on podrem
   escollir obrir o guardar l'informe.

En l'exemple hi ha les dates per generar l'informe del primer trimestre de l'any:

![](../../_static/cnmc/1_2005/wizard_informe_1.png)

* Les dades s'extreuen dels canvis de comercialitzadora en les modificacions
  contractuals entre les data inicial i data final especificades en la secció
  'periode del trimestre', quan dues modificacions contractuals consecutives
  tenen diferent comercialitzadora.
* Només es tenen en compte els canvis de comercialitzadora de 'CUR' a 'NO CUR'
  i de 'NO CUR' a 'NO CUR'.
* Les dades s'agrupen per diferent tipus de punt de mesura.



### 2NA1 Informe de sol·licituds acceptades de canvi de comercialitzadora en funció del retràs fins a la data de canvi efectiu.

**Informe trimestral.**

1. Omplim el camp de la secció 'tipus de fitxer' amb el valor '2NA1' del
   desplegable.
2. Omplim els camps de la secció 'periode del trimestre' amb la data inicial i
   data final del trimestre.
3. Premem el botó 'exportar' per generar l'informe.
4. Quan s'ha generat l'informe apareix la secció 'nom del fitxer' on podrem
   escollir obrir o guardar l'informe.

En l'exemple hi ha les dates per generar l'informe del primer trimestre de l'any:

![](../../_static/cnmc/1_2005/wizard_informe_2.png)

* Les dades s'extreuen dels canvis de comercialitzadora en les modificacions
  contractuals entre les data inicial i data final especificades en la secció
  'periode del trimestre', quan dues modificacions contractuals consecutives
  tenen diferent comercialitzadora.
* Només es tenen en compte els canvis de comercialitzadora de 'CUR' a 'NO CUR',
  de 'NO CUR' a 'NO CUR' i de 'NO CUR' a 'CUR'.
* Les dades s'agrupen per diferents comercialitzadores d'entrada i sortida,
  tipus de punt de mesura i tarifa d'accés.


### 5A Informe de classifació dels consumidors en funció del número de canvis efectuats de MR a ML.

**Informe semestral.**

1. Omplim el camp de la secció 'tipus de fitxer' amb el valor '5A' del desplegable.
2. Omplim els camps de la secció 'periode del trimestre' amb la data inicial i
   data final del trimestre.
3. Premem el botó 'exportar' per generar l'informe.
4. Quan s'ha generat l'informe apareix la secció 'nom del fitxer' on podrem
   escollir obrir o guardar l'informe.

En l'exemple hi ha les dates per generar l'informe del primer semestre de l'any:

![](../../_static/cnmc/1_2005/wizard_informe_5a.png)

* Les dades s'extreuen dels canvis de comercialitzadora en les modificacions
  contractuals entre les data inicial i data final especificades en la secció
  'periode del trimestre', quan dues modificacions contractuals consecutives
  tenen diferent comercialitzadora.
* Només es tenen en comtpe els canvis de comercialitzadora de 'CUR' a 'NO CUR'.
* Les dades s'agrupen per diferent tipus de punt de mesura.


### 5B Informe de classifació dels consumidors en funció del número de canvis efectuats de comercialitzadora.

**Informe semestral.**

1. Omplim el camp de la secció 'tipus de fitxer' amb el valor '5B' del desplegable.
2. Omplim els camps de la secció 'periode del trimestre' amb la data inicial i
   data final del trimestre.
3. Premem el botó 'exportar' per generar l'informe.
4. Quan s'ha generat l'informe apareix la secció 'nom del fitxer' on podrem
   escollir obrir o guardar l'informe.

En l'exemple hi ha les dates per generar l'informe del primer semestre de l'any:

![](../../_static/cnmc/1_2005/wizard_informe_5b.png)

* Les dades s'extreuen dels canvis de comercialitzadora en les modificacions
  contractuals entre les data inicial i data final especificades en la secció
  'periode del trimestre', quan dues modificacions contractuals consecutives
  tenen diferent comercialitzadora.
* Només es tenen en compte els canvis de comercialitzadora de 'NO CUR' a
  'NO CUR'.
* Les dades s'agrupen per diferent tipus de punt de mesura.

### 7NA Informe de classificació dels consumidors en funció del comercialitzador, tipus de punt de subministre, tipus de tarifa d'accés i la provincia on s'ubica el punt de subministrament.

**Informe trimestral.**

1. Omplim el camp de la secció 'tipus de fitxer' amb el valor '7NA' del desplegable.
2. Omplim el camp de la secció 'trimestre' amb la data final del trimestre.
3. Omplim els camps de la secció 'periode d'energia' amb la data inicial i la
   data final dels quatre últims trimestres anteriors al trimestre escollit en
   el camp de la secció 'trimestre'.
4. Premem el botó 'exportar' per generar l'informe.
5. Quan s'ha generat l'informe apareix la secció 'nom del fitxer' on podrem
   escollir obrir o guardar l'informe.

En l'exemple hi ha les dates per generar l'informe del primer trimestre de
l'any, amb els quatre últims trimestres anteriors al primer trimestre de l'any
com a periode d'energia:

![](../../_static/cnmc/1_2005/wizard_informe_7.png)

* Les dades dels consumidors s'extreuen de les modificacions contractuals, on
  la data especificada a la secció 'trimestre' es troba entre les data inicial i
  data final de la modificació contractual.
* L'energia s'extreu de les factures, amb data inicial i final entre les data inicial
  i data final respectivament de la secció 'periode d'energia'.
* Ambdues es relacionen i s'agrupen per diferents comercialitzadores, tipus de
  punt de mesura, tarifa d'accés i provincia.

#### Tarifes compatibles

Només s'informarà de l'energia facturada d'aquelles factures que tinguin alguna de les
següents tarifes.

Tarifa  | Codi
:-------|:-----
2.0A    | 1
2.0DHA  | 2
3.0A    | 3
3.0A LB | 3
3.1A    | 4
3.1A LB | 4
6.1A    | 5
6.1B    | 17
6.2     | 6
6.3     | 7
6.4     | 8
2.1A    | 10
2.1DHA  | 11
2.0DHS  | 12
2.1DHS  | 13

Qualsevol altre tarifa, com per exemple tarifes de generació, seràn ignorades i no
s'informarà l'energia consumida d'aquestes factures.
