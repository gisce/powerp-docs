## Fitxers d'intercanvi per GISCE-TPL

En aquest apartat es descriuen els formats dels fitxers de intercanvi entre el
programa de gestió GISCE-ERP.

Si s'utilitza un programa de facturació d'accessos diferent de GISCE-ERP es
descriuen amb tot detall els formats dels fitxers de importació de rutes i
exportació de lectures des del TPL.

### Especificacions comuns a tots els fitxers

Tots els fitxers respecten les següents especificacions:

- Text codificat amb _UTF-8_.
- Camps delimitats per tabuladors(`'\t', 0x09`).
- Línies delimitades per _newline_ (`'\n', 0x0a`).
- No s'utilitzen cometes ni ningun altre delimitador per cadenes de caràcters.
- Els números no enters es codifiquen amb un punt per separar elsdecimals, mai
  una coma. No s'utilitzen separadors de miliars. Si alguna magnitud fos
  negativa s'indicaria amb un guió com a prefix.

### Codificació dels camps Data/Hora

Els camps data s'emmagatzemen com cadenes de caràcters. Sempre s'inclou la hora,
i es deixen a 0 els segons, minuts i hores si no es té aquesta precisió o si es
irrelevant.    
El format es _"YYYYMMDDhhmmss"_, 4 dígits per l'Any, 2 per al Mes, 2 per al Dia
del mes, 2 per les Hores, 2 pels Minuts i 2 pels Segons.    
Cada element s'emplena amb zeros per l'esquerra fins que ocupi la longitud que
li correspon.

### Codificació del camp "_Configuración Puerto_"

Els paràmetres de configuració del port série i els paràmetres necessaris per
accedir al comptador mitjançant el port série, tant amb cable o amb sonda
òptica, es codifiquen amb una cadena de caràcters. Separant cada un dels camps
amb el caràcter ':', en aquest ordre:

- **_port_name_**: el nom del port de comunicacions. És una cadena de caràcters
  i els possibles valors són: _"com1", "com2", ..., "com19", "com20"_ .
  En els terminals sol ser _"com1"_
- **_baud_rate_**: tasa de transferència, en _bps_. És un enter i els possibles
  valors legals són: `110, 300, 600, 1200, 2400, 4800, 9600, 14400, 19200, 28800, 38400, 57600, 115200, 128000, 256000`

- **_data_bits_**: bits de dades. És un enter. Els possibles valors
  legals són _7 i 8_
- **_parity_**: paritat. És una cadena de caràcters. Els possibles valors
  legals són: _“even”, “none”, “odd”, “mark”, “space”_.
- **_stop_bits_**: bits de parada. És una cadena de caràcters i els possibles
  valors legals són: _“0”, “1”, “1.5”, “2”_.
- **_timeout_**: temps d'espera. És un enter. Es tracta del valor límit,
  en mil·lisegons, que GISCE-TPL esperarà a que el comptador respongui abans
  de considerar que no es pot establir la connexió. Un valor típic i
  raonable és _2000_, que correspon a 2000ms, és a dir, 2 segons.
- **_direccion_de_enlace_**: Un enter.
- **_direccion_del_punto_de_medida_**: Un enter.
- **_contraseña_**: Un enter.
- **_tipo_de_curva_**: _Per sel·leccionar el tipus de corba que es desitja
  decarregar en l'apartat "Configuración" es pot sel·leccionar la corba a
  descarregar_:
    - Dades agregades cada 60 minuts, amb valors absoluts
    - Dades agregades cada 60 minuts, amb valors incrementals.
    - Dades agregades cada 15 minuts, amb valors absoluts.
    - Dades agregades cada 15 minuts, amb valors incrementals.

Com es pot veure:

- El **primer camp** defineix la configuració del **terminal**.
- Els **cinc següents** defineixen la configuració del protocol **RS232**
- Els **tres últims** defineixen la configuració del protocol **IEC870REE**

És imprescindible que els valors corresponguin a la configuració del comptador
per poder descarregar lectures electrònicament.

### Codificació del camp "_Calidad_"

D'acord amb el document "_REGLAMENTO DE PUNTOS DE MEDIDA: Protocolo de
comunicaciones entre registradores y concentradores de medidas o terminales
portátiles de lectura_", Revisió _10.04.02_, del _10 d'Abril de 2002_, publicat
a _www.ree.es_.    
Aquest document es refereix al camp com "_octeto de cualificadores_" i als seus
bits com "_bits de calidad_".

Aquest camp es un eter de 8 bits, que s'interpreta com un "_mapa de bits_", amb
el següent significat per cada bit:

| Bit  | Valor |            Descripció                                             |
|:----:|:-----:|:------------------------------------------------------------------|
|0(LSB)|   1   | Reservat; Sense significat                                        |
|  1   |   2   | Fallada en l'alimentació                                          |
|  2   |   4   | Intrussió                                                         |
|  3   |   8   | Paràmetres modificats                                             |
|  4   |   16  | Canvi "lleuger" en la data/hora; p.e. un ajustament de dos minuts |
|  5   |   32  | _Overflow_                                                        |
|  6   |   64  | Canvi "radical" en la data/hora; p.e. un ajustament de dos dies   |
|7(MSB)|  128  | Mesura invàlida.                                                  |

S'ha de tenir sempre en compte, com a mínim, el bit més significatiu (_MSB_)

### Fitxer de Ruta (GISCE-ERP → GISCE-TPL)

Normalment aquest fitxer el genera la aplicació GISCE-ERP, i serveix com a dades
d'entrada per a l'aplicació GISCE-TPL, també pot generar-lo qualsevol altre
programa de gestió.

El _fitxer de ruta_ ha de tenir la extensió "**.ruta**" perquè pogui ser
processat per GISCE-TPL. El nom del fitxer, sense la extensió, es la
identificació que se li mostra a l'usuari a GISCE-TPL.

El fitxer conté:

- Una capçalera d'una línia amb el següent camp.

|        Nom del Camp        | Descripció                                      |
|:--------------------------:|:------------------------------------------------|
| _data_planificada_lectura_ | La data que es té planificada i/o que es vol fer constar en les lectures d'aquesta ruta. S'utilitza globalment per tots els comptadors com a valor per defecte del camp _fecha_lectura_, que es retorna en el _fitxer de lectures_ (tal com es descriu més abaix), excepte quan la lectura s'efectua de forma electrònica, donat que s'utilitzarà la data del tancament que reporta el comptador. Format _AAAAMMDDhhmmss_.  |

- Una línia per cada comptador en la ruta, amb els següents camps.

|        Nom del Camp        | Descripció                                      |
|:--------------------------:|:------------------------------------------------|
| _zona_            | El codi o nom de la zona, que el TPL tracta com alfanumèric. Es mostra a l'usuari a títol informatiu. No té altre funció. |
| _orden_           | La posició del comptador dins de la zona/ruta, que el TPL tracta com alfanumèric. Se li mostra a l'usuari a títol informatiu. No té altre funció. |
| _id_poliza_       | Identificador de la pòlissa, que el TPL tracta com alfanumèric. Es mostra a l'usuari a títol informatiu. No té altre funció. |
| _id_contador_     | Un número enter que ha de ser diferent per cada comptador de la ruta. Identifica internament (no se li mostra a l'usuari) al comptador. Es retorna intacte en el _fitxer de lectures_ que genera el TPL com a resultat de la operació de lectura. |
| _numero_contador_ | Un identificador que ha de ser diferent per cada comptador de la ruta, que TPL tracta com alfanumèric. Es recomana que coincideixi amb el número de sèrie del comptador, que a més a més sol coincidir amb el codi de barres imprés en el frontal del comptador. Se li mostra a l'usuari a títol informatiu. En les lectures electròniques, es compara amb el número de sèrie que dona el comptador, avisant al usuari en cas de ser diferent. En les lectures manuals, aquest camp és el que s'utilitza per identificar el comptador a registrar, a partir de la lectura del seu codi de barres. |

### Fitxer de Lectures (GISCE-TPL → GISCE-ERP)


### Fitxer de corbes (GISCE-TPL → GISCE-ERP)


### Catàleg d'anomalies


### Catàleg de situacions


### Catàleg d'Avisos
