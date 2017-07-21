# Intercanvi SOA comercialitzadora

El fitxer d'intercanvi SOA té el format estàndard **CSV** amb els camps separats
per **tabulacions** i codificat en **UTF-8**.

El fitxer ha de contenir **tots** els valors. Si no es disposa d'informació per
emplenar-los, s'hauràn de deixar buits. A continuació es detallen els camps
concrets dels que disposa el fitxer:

| Columna | Nom intern del camp                   | Tipus        | Descripció                                                         |
|:-------:|---------------------------------------|--------------|--------------------------------------------------------------------|
| 1       | **csv_cups_codi**                     | varchar(30)  | Codi Universal de Punt de Suministre                               |
| 2       | **csv_cups_distribuidora**            | varchar(10)  | Distribuidora del CUPS                                             |
| 3       | **csv_cups_municipi**                 | integer(10)  | Municipi del CUPS                                                  |
| 4       | **csv_cups_poblacio**                 | varchar(60)  | Població del CUPS                                                  |
| 5       | **csv_cups_carrer**                   | varchar(60)  | Carrer del CUPS                                                    |
| 6       | **csv_cups_numero**                   | varchar(10)  | Número del carrer del CUPS                                         |
| 7       | **csv_cups_escala**                   | varchar(50)  | Escala del CUPS                                                    |
| 8       | **csv_cups_planta**                   | varchar(50)  | Número de planta del CUPS                                          |
| 9       | **csv_cups_pis**                      | varchar(10)  | Pis del CUPS                                                       |
| 10      | **csv_cups_codi_tipus_via**           | varchar(10)  | Codi tipus via del CUPS                                            |
| 11      | **csv_cups_abbr_tipus_via**           | varchar(20)  | Abreviatura del tipus de via del CUPS                              |
| 12      | **csv_cups_tipus_via**                | varchar(20)  | Tipus de via del CUPS                                              |
| 13      | **csv_cups_ref_catastral**            | varchar(20)  | Referència Catastral del CUPS                                      |
| 14      | **csv_cups_aclarador**                | varchar(100) | Aclarador del CUPS                                                 |
| 15      | **csv_cups_poligon**                  | varchar(50)  | Polígon del CUPS                                                   |
| 16      | **csv_cups_parcela**                  | varchar(50)  | Parcela del CUPS                                                   |
| 17      | **csv_cups_cp_cups**                  | varchar(10)  | Codi postal del CUPS                                               |
| 18      | **csv_abonat_codi**                   | varchar(60)  | Codi d'abonat                                                      |
| 19      | **csv_abonat_nif**                    | varchar(32)  | NIF de l'abonat                                                    |
| 20      | **csv_abonat_nom**                    | varchar(128) | Nom de l'abonat                                                    |
| 21      | **csv_abonat_idioma**                 | varchar(10)  | Idioma de l'abonat                                                 |
| 22      | **csv_abonat_direccio_nom**           | varchar(64)  | Direcció de l'abonat (nombre)                                      |
| 23      | **csv_abonat_direccio**               | varchar(128) | Direcció de l'abonat                                               |
| 24      | **csv_abonat_numero**                 | varchar(128) | Número del carrer de la direcció de l'abonat                       |
| 25      | **csv_abonat_planta**                 | varchar(128) | Planta de l'abonat                                                 |
| 26      | **csv_abonat_aclarador**              | varchar(128) | Aclarador de l'abonat                                              |
| 27      | **csv_abonat_cp**                     | varchar(10)  | Codi postal de l'abonat                                            |
| 28      | **csv_abonat_ine_municipi**           | varchar(10)  | INE del municipi de l'abonat                                       |
| 29      | **csv_abonat_poblacio**               | varchar(128) | Població de l'abonat                                               |
| 30      | **csv_abonat_provincia**              | varchar(128) | Província de l'abonat                                              |
| 31      | **csv_abonat_pais**                   | varchar(128) | País de l'abonat                                                   |
| 32      | **csv_abonat_telefon**                | varchar(64)  | Telèfon de l'abonat                                                |
| 33      | **csv_abonat_fax**                    | varchar(64)  | FAX de l'abonat                                                    |
| 34      | **csv_abonat_mail**                   | varchar(64)  | Email de l'abonat                                                  |
| 35      | **csv_abonat_mobil**                  | varchar(64)  | Mòbil de l'abonat                                                  |
| 36      | **csv_polissa_codi_comptador**        | varchar(20)  | Número de comptador                                                |
| 37      | **csv_polissa_codi_contracte**        | varchar(60)  | Número de pòlissa (contracte)                                      |
| 38      | **csv_polissa_tarifa**                | varchar(10)  | Tarifa                                                             |
| 39      | **csv_polissa_data_alta**             | date(10)     | Data d'alta                                                        |
| 40      | **csv_polissa_donar_de_baixa**        | Boolean      | Baixa                                                              |
| 41      | **csv_polissa_data_baixa**            | date(10)     | Data de baixa                                                      |
| 42      | **csv_polissa_potencia**              | float(11)    | Potència                                                           |
| 43      | **csv_polissa_tensio**                | varchar(30)  | Tensió                                                             |
| 44      | **csv_polissa_activitat_cnae**        | varchar(10)  | Activitat CNAE                                                     |
| 45      | **csv_polissa_comercialitzadora**     | varchar(4)   | Comercialitzadora                                                  |
| 46      | **csv_polissa_observacions**          | text(1024)   | Observacions                                                       |
| 47      | **csv_polissa_titular**               | varchar(128) | Titular de la pòlissa                                              |
| 48      | **csv_polissa_estat**                 | varchar(60)  | Estat de la pòlissa, posar "BORRADOR" per pólissa en esborrany.    |
| 49      | **csv_polissa_ref_distriuidora**      | varchar(60)  | Referència distribuïdora                                           |
| 50      | **csv_polissa_tipus_punt_mesura**     | varchar(2)   | Tipus del punt de mesura                                           |
| 51      | **csv_polissa_potencies_per_periode** | varchar(128) | Potència per període                                               |
| 52      | **csv_polissa_data_firma_contracte**  | date(10)     | Data de firma del contracte                                        |
| 53      | **csv_fact_facturacio_tipus**         | varchar(50)  | Tipus facturació. Valors: 'MENSUAL' o 'BIMESTRAL'                  |
| 54      | **csv_fact_facturacio_potencia**      | varchar(64)  | Facturació potència. Valors: 'MAXIMETRO', 'ICP' o 'RECARGO_ICP'    |
| 55      | **csv_fact_unitat_facturacio**        | varchar(10)  | Unitat de facturació                                               |
| 56      | **csv_fact_tarifa_comercialitzadora** | varchar(50)  | Tarifa comercialitzadora                                           |
| 57      | **csv_fact_tipus_pagament**           | varchar(50)  | Tipus de pagament. Valors: 'RECIBO_CSB' o 'TRANSFERENCIA_CSB'      |
| 58      | **csv_fact_grup_pagament**            | varchar(50)  | Grup de pagament                                                   |
| 59      | **csv_fact_desc_bancari**             | varchar(60)  | Descripció bancaria                                                |
| 60      | **csv_fact_compte_bancari**           | varchar(30)  | Compte bancari                                                     |
| 61      | **csv_fact_persona_pagador**          | varchar(7)   | Persona pagadora. Valors: 'TITULAR' o 'OTRO'                       |
| 62      | **csv_pagador_codi**                  | varchar(32)  | Codi pagador                                                       |
| 63      | **csv_pagador_nif**                   | varchar(32)  | NIF del pagador                                                    |
| 64      | **csv_pagador_nom**                   | varchar(128) | Nom del pagador                                                    |
| 65      | **csv_pagador_idioma**                | varchar(10)  | Idioma del pagador                                                 |
| 66      | **csv_pagador_direccio_nom**          | varchar(64)  | Nom de la direcció del pagador                                     |
| 67      | **csv_pagador_direccio**              | varchar(128) | Direcció del pagador                                               |
| 68      | **csv_pagador_numero**                | varchar(128) | Número del pagador                                                 |
| 69      | **csv_pagador_planta**                | varchar(128) | Planta del pagador                                                 |
| 70      | **csv_pagador_cp**                    | varchar(10)  | Codi postal del pagador                                            |
| 71      | **csv_pagador_ine_municipi**          | varchar(10)   | INE del pagador                                                    |
| 72      | **csv_pagador_poblacio**              | varchar(128) | Posició del pagador                                                |
| 73      | **csv_pagador_provincia**             | varchar(128) | Província del pagador                                              |
| 74      | **csv_pagador_pais**                  | varchar(128) | País del pagador                                                   |
| 75      | **csv_pagador_telefon**               | varchar(64)  | Telèfon del pagador                                                |
| 76      | **csv_pagador_fax**                   | varchar(64)  | FAX del pagador                                                    |
| 77      | **csv_pagador_mail**                  | varchar(64)  | Email del pagador                                                  |
| 78      | **csv_pagador_mobil**                 | varchar(64)  | Mòbil del pagador                                                  |
| 79      | **csv_fact_enviament_factura**        | varchar(12)  | Enviament de la factura. Valors: 'POSTAL', 'EMAIL' o 'POST+EMAIL'  |
| 80      | **csv_fact_persona_notificacio**      | varchar(7)   | Persona de notificació. Valors: 'TITULAR', 'PAGADOR' o 'ALTRE'     |
| 81      | **csv_notificacio_nom**               | varchar(128) | Nom de la notificació d'enviament                                  |
| 82      | **csv_notificacio_nif**               | varchar(128) | NIF de la notificació d'enviament                                  |
| 83      | **csv_notificacio_direccio_nom**      | varchar(128) | Nom de la direcció de la notificació d'enviament                   |
| 84      | **csv_notificacio_direccio**          | varchar(128) | Direcció de la notificació d'enviament                             |
| 85      | **csv_notificacio_numero**            | varchar(128) | Número de la notificació d'enviament                               |
| 86      | **csv_notificacio_planta**            | varchar(128) | Planta de la notificació d'enviament                               |
| 87      | **csv_notificacio_cp**                | varchar(10)  | Codi postal de la notificació d'enviament                          |
| 88      | **csv_notificacio_ine_municipi**      | varchar(10)  | Codi INE del municipi de la notificació d'enviament                |
| 89      | **csv_notificacio_poblacio**          | varchar(128) | Població de la notificació d'enviament                             |
| 90      | **csv_notificacio_provincia**         | varchar(128) | Província de la notificació d'enviament                            |
| 91      | **csv_notificacio_pais**              | varchar(128) | País de la notificació d'enviament                                 |
| 92      | **csv_notificacio_telefon**           | varchar(64)  | Telèfon de la notificació d'enviament                              |
| 93      | **csv_notificacio_fax**               | varchar(64)  | FAX de la notificació d'enviament                                  |
| 94      | **csv_notificacio_mail**              | varchar(64)  | Email de la notificació d'enviament                                |
| 95      | **csv_notificacio_mobil**             | varchar(64)  | Mòbil de la notificació d'enviament                                |
| 96      | **csv_propietari_cc_nom**             | varchar(128) | Propietari CC                                                      |
| 97      | **csv_propietari_cc_nif**             | varchar(128) | NIF propietari CC                                                  |
| 98      | **csv_propietari_cc_direccio**        | varchar(128) | Direcció propietari CC                                             |
| 99      | **csv_propietari_cc_numero**          | varchar(128) | Número propietari CC                                               |
| 100     | **csv_propietari_cc_planta**          | varchar(128) | Planta propietari CC                                               |
| 101     | **csv_propietari_cc_cp**              | varchar(10)  | Codi postal propietari CC                                          |
| 102     | **csv_propietari_cc_ine_municipi**    | varchar(10)  | INE propietari CC                                                  |
| 103     | **csv_propietari_cc_poblacio**        | varchar(128) | Població propietari CC                                             |
| 104     | **csv_propietari_cc_provincia**       | varchar(128) | Província propietari CC                                            |
| 105     | **csv_propietari_cc_pais**            | varchar(128) | País propietari CC                                                 |
| 106     | **csv_propietari_cc_telefon**         | varchar(64)  | Telèfon propietari CC                                              |
| 107     | **csv_propietari_cc_fax**             | varchar(64)  | FAX propietari CC                                                  |
| 108     | **csv_propietari_cc_mail**            | varchar(64)  | Email propietari CC                                                |
| 109     | **csv_propietari_cc_mobil**           | varchar(64)  | Mòbil propietari CC                                                |

- Els camps on a la descripció s'especifiquen valors concrets significa que el
valor només pot estar comprés entre els especificats.

- Tots els números de compte estan relacionats amb el **pagador** del contracte.
Si el titular és el mateix que el pagador, llavors es crearà també en el
titular.

- Per introduïr el cups de la **distribuidora** (csv_cups_distribuidora) és
suficient amb els 4 dígits de REE. Per exemple, el codi de **Unión Fenosa** és
el 0022.

- Per introduïr el cups del **municipi** es fa mitjançant el codi INE.

- Al introduïr la població del CUPS o de l'abonat (csv_cups_poblacio i
csv_abonat_poblacio) per defecte s'obtenen les poblacions del municipi indicat.
Si no es troba la població pot crearse de forma automàtica o bé enviar un error,
segons la configuració de l'ERP.

- El camp **csv_abonat_idioma** pot prendre els següents valors:
    - Castellà: **es_ES**
    - Català: **ca_ES**
    - Gallec: **gl_ES**
    - Anglès: **en_US**

- Si es desitja introduïr varis períodes al camp **csv_polissa_potencies_per_periode**,
s'ha de fer ordenat per períodes i separats per espais. Si aquest camp no es
defineix, per defecte tots els períodes tindràn la potència contractada.
    - Exemple d'una 3.0A: "15 20 20"

- El camp **csv_polissa_tensio** s'ha d'introduïr per el seu valor normalitzat.

- El separador **decimal** de tots els camps ha de ser un **punt**.

- Per informar del **mode de facturació** d'una pòlissa, cal fer-ho mitjançant
el camp **csv_fact_facturacio_tipus**. Pot prendre els valors "MENSUAL" o "BIMESTRAL".
