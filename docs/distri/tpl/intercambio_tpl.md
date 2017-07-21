## Fitxers d'intercanvi per GISCE-TPL

En aquest apartat es descriuen els formats dels fitxers de intercanvi entre el
programa de gestió GISCE-ERP.

Si s'utilitza un programa de facturació d'accessos diferent de GISCE-ERP es
descriuen amb tot detall els formats dels fitxers de importació de rutes i
exportació de lectures des del TPL.

### Especificacions comuns a tots els fitxers

Tots els fitxers respecten les següents especificacions:

- Text codificat amb _UTF-8_.
- Camps delimitats per tabuladors(_'\t', 0x09_).
- Línies delimitades per _newline_ (_'\n', 0x0a_).
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
- **_direccion_de_enlace_**: Un enter.
- **_direccion_del_punto_de_medida_**: Un enter.
- **_contraseña_**: Un enter.
- **_timeout_**: temps d'espera. És un enter. Es tracta del valor límit,
  en mil·lisegons, que GISCE-TPL esperarà a que el comptador respongui abans
  de considerar que no es pot establir la connexió. Un valor típic i
  raonable és _2000_, que correspon a 2000ms, és a dir, 2 segons.
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

+----------------------------+-------------------------------------------------+
|        Nom del Camp        | Descripció                                      |
+============================+=================================================+
| _data_planificada_lectura_ | La data que es té planificada i/o que es vol fer|
|                            | constar en les lectures d'aquesta ruta.         |
|                            | S'utilitza globalment per tots els comptadors   |
|                            | com a valor per defecte del camp _fecha_lectura_|
|                            | , que es retorna en el _fitxer de lectures_ (tal|
|                            | com es descriu més abaix), excepte quan la      |
|                            | lectura s'efectua de forma electrònica, donat   |
|                            | que s'utilitzarà la data del tancament que      |
|                            | reporta el comptador. Format _AAAAMMDDhhmmss_.  |
+----------------------------+-------------------------------------------------+

- Una línia per cada comptador en la ruta, amb els següents camps.

+------------------------+-----------------------------------------------------+
|      Nom del Camp      |  Descripció                                         |
+========================+=====================================================+
|         _zona_         | El codi o nom de la zona, que el TPL tracta com     |
|                        | alfanumèric. Es mostra a l'usuari a títol informatiu|
|                        | . No té altre funció.                               |
+------------------------+-----------------------------------------------------+
|         _orden_        | La posició del comptador dins de la zona/ruta, que  |
|                        | el TPL tracta com alfanumèric. Se li mostra a       |
|                        | l'usuari a títol informatiu. No té altre funció.    |
+------------------------+-----------------------------------------------------+
|       _id_poliza_      | Identificador de la pòlissa, que el TPL tracta com  |
|                        | alfanumèric. Es mostra a l'usuari a títol informatiu|
|                        | . No té altre funció.                               |
+------------------------+-----------------------------------------------------+
|      _id_contador_     | Un número enter que ha de ser diferent per cada     |
|                        | comptador de la ruta. Identifica internament (no se |
|                        | li mostra a l'usuari) al comptador. Es retorna      |
|                        | intacte en el _fitxer de lectures_ que genera el TPL|
|                        | com a resultat de la operació de lectura.           |
+------------------------+-----------------------------------------------------+
|    _numero_contador_   | Un identificador que ha de ser diferent per cada    |
|                        | comptador de la ruta, que TPL tracta com alfanumèric|
|                        | . Es recomana que coincideixi amb el número de sèrie|
|                        | del comptador, que a més a més sol coincidir amb el |
|                        | codi de barres imprés en el frontal del comptador.  |
|                        | Se li mostra a l'usuari a títol informatiu. En les  |
|                        | lectures electròniques, es compara amb el número de |
|                        | sèrie que dona el comptador, avisant al usuari en   |
|                        | cas de ser diferent. En les lectures manuals, aquest|
|                        | camp és el que s'utilitza per identificar el        |
|                        | comptador a registrar, a partir de la lectura del   |
|                        | seu codi de barres.                                 |
+------------------------+-----------------------------------------------------+
|        _id_tarifa_     | GISCE-TPL ignora aquest valor.                      |
+------------------------+-----------------------------------------------------+
|      _nombre_tarifa_   | El nom de la tarifa (p.e. _"2.0DHA", "6.1", ..._),  |
|                        | que el TPL tracta com alfanumèric. Es mostra a      |
|                        | l'usuari com a títol informatiu. No té altre funció.|
+------------------------+-----------------------------------------------------+
|        _potencia_      | La potència contractada, que el TPL tracta com a    |
|                        | camp alfanumèric. Es mostra a l'usuari com a títol  |
|                        | informatiu. No té altre funció.                     |
+------------------------+-----------------------------------------------------+
|     _nombre_abonado_   | Nom i cognoms o nom fiscal del abonat. Es mostra al |
|                        | usuari a títol informatiu. No te cap altre funció.  |
|       _direccion_      | Generalment correspondrà a la direcció completa (amb|
|                        | número, escala, pis, etc) de l'habitatge o local en |
|                        | la que es subministra el servei. Es mostra al usuari|
|                        | a títol informatiu. No te cap altre funció.         |
+------------------------+-----------------------------------------------------+
|       _poblacion_      | Complementa el camp direcció que s'acaba de         |
|                        | descriure. El TPL tracta aquest camp com alfanumèric|
|                        | . Es mostra al usuari a títol informatiu. No te cap |
|                        | altre funció.                                       |
+------------------------+-----------------------------------------------------+
|  _situacion_contador_  | Indicació per facilitar a l'usuari la localització  |
|                        | del comptador. Es mostra al usuari a títol          |
|                        | informatiu. No te cap altre funció. El TPL          |
|                        | l'interpreta de la següent forma.: Si es un número  |
|                        | enter, s'utilitza aquest número com a clau per      |
|                        | recuperar la descripció del _catàleg de situacions_.|
|                        | En qualsevol altre cas es considera literalment com |
|                        | la informació que s'ha de mostrar al usuari.        |
+------------------------+-----------------------------------------------------+
|     _aviso_contador_   | Indicació per mostrar al usuari una advertència     |
|                        | relevant a ternir en compte quan s'ha d'anar a      |
|                        | llegir aquest comptador. Es mostra al usuari a títol|
|                        | informatiu. No te cap altre funció. El TPL          |
|                        | l'interpreta de la següent manera: si es un nombre  |
|                        | enter, s'utilitza com a clau per recuperar la       |
|                        | descripció en el _catàleg d'avisos_. En qualsevol   |
|                        | altre cas es considera literalment com la informació|
|                        | que s'ha de mostrar al usuari.                      |
+------------------------+-----------------------------------------------------+
| _configuracion_puerto_ | Un valor alfanumèric que correspon a la codificació |
|                        | dels paràmetres de configuració del _port sèrie     |
|                        | RS232_ i als paràmetres necessaris per la lectura   |
|                        | electrònica a través del _cable serie_ i/o la _sonda|
|                        | òptica_. El TPL descodifica aquest camp segons      |
|                        | s'explica en la                                     |
|                        | [secció  corresponent](../tpl/descarga_cierres_y_   |
|                        |_curvas#configuracio-de-la-descarrega) d'aquest      |
|                        | document.                                           |
+------------------------+-----------------------------------------------------+

I en la mateixa línia, per cada magnitud a llegir en el comptador (i el nombre
de magnituds ha de ser 1, 2, 3, 4, 5, 6, 18 o 24), aquests tres camps:

+---------------------+--------------------------------------------------------+
|    Nom del Camp     |  Descripció                                            |
+=====================+========================================================+
|     _id_periodo_    | Identificador del periode al que correspon la lectura. |
|                     | El TPL tracta aquest valor com alfanumèric, i es       |
|                     | retorna intacte en el _fitxer de lectures_ que genera  |
|                     | el TPL com a resultat de la operació de lectura. No se |
|                     |  li mostra al usuari.                                  |
+---------------------+--------------------------------------------------------+
|  _nombre_periodo_   | Identifiador alfanumèric que indica al usuari el       |
|                     | periode al que correspon la lectura. El TPL tracta     |
|                     | aquest valor com alfanumèric, i es retorna intacte en  |
|                     | el _fitxer de lectures_ que genera el TPL com a        |
|                     | resultat de la operació de lectura. Únicament se li    |
|                     | mostra al usuari en el cas de les tarifes _"2.0A" i    |
|                     | "2.0DHA"_, quan hi ha entre 1 i 6 magnituds a recollir.|
+---------------------+--------------------------------------------------------+
| _lectura_anterior_  | En general el TPL tracta la lectura com un número enter|
|                     | , excepte quan els tres primers caràcters del camp     |
|                     | _nombre_periodo_ son _"MAX" o "EXC"_. En aquests dos   |
|                     | casos es permeten decimals.                            |
+---------------------+--------------------------------------------------------+

GISCE-TPL decideix el procediment per solicitar les lectures d'un comptador en
base al número de magnituds relacionades amb aquest que apareixen en
el _fitxer de ruta_:

- **Entre 1 i 6 lectures** (el cas de les tarifes "2.0A" i "2.0DHA"): es
  demanen al operador les lectures, mostrant clarament per cada lectura,
  la etiqueta _nombre_periodo_, la lectura anterior i la diferència entre
  la lectura anterior i la actual.
- **18 lectures** (cas de les tarifes "3.0A"): es demanen al operador les
  lectures, no es mostra ni el valor de la lectura anterior, ni la diferència
  entre l'actual i l'anterior, ni els camps _nombre_periodo_, i es demanen
  les lectures en una taula de 3 columnes per 6 files, on les lectures es
  distribueixen de dalt a baix i d'esquerra a dreta:
    - Les tres columnes corresponen, d'esquerra a dreta, als valors "Activa",
      "Reactiva", "Maxímetre" de cada periode.
    - Les files es veuen etiquetades amb els noms dels periodes, no amb el
      valor del camp _nombre_periodo_, sempre com _"P1", "P2", ..., "P6"_.
- **24 lectures** (cas de les tarifes "6.1"): les primeres 18 lectures es
  distribueixen com el cas que s'acaba d'esplicar; Les 6 restants es mostren
  com les lectures d'"excessos", en una altra taula, d'una columna i sis files,
  amb les mateixes etiquetes (_"P1", "P2", ..., "P6"_) per les files.

### Fitxer de Lectures (GISCE-TPL → GISCE-ERP)

Normalment aquest fitxer el genera l'aplicació GISCE-TPL, com a resultat del
treball del usuari a partir del _fitxer de ruta_. En aquest cas, el fitxer té
el mateix nom que el _fitxer de ruta_, substituïnt la extensió per "**.lectura**".

Perquè GISCE-TPL pogui processar el _fitxer de lectures_ ha de tenir la
extensió "**.lectura**" i ha de trobar-se dins del terminal en la mateixa
ubicació que el _fitxer de ruta_.

Normalment el _fitxer de lectura_ es processa amb GISCE-ERP per incorporar a la
base de dades les lectures recollides i poder, així, realitzar les tasques com
la facturació, el perfilat, generació d'informes, etc.

El fitxer conté una línia per cada comptador per al que l'operari ha recollit
lectures i/o entrat un comentari o una anomalia indicant el motiu per el que no
ha estat possible efectuar la lectura, si aquest ha estat el cas. Les línies es
van afegint al fitxer a mesura que l'usuari va processant comptadors, i en
l'ordre que els va processant. Això vol dir que no necessariament hi haurà
lectures per tots els comptadors que es van relacionar en el corresponent
_fitxer de ruta_.

També existeix la possibilitat de que un comptador hagi estat llegida més d'una
vegada. La norma general (i això es el que fa GISCE-ERP interpretar aquest
fitxer) es que la lectura vàlida es la última que apareix en el fitxer.

El fitxer consisteix en una llista per cada comptador llegit, amb els
següents camps:

+-----------------------+------------------------------------------------------+
|      Nom del camp     |  Descripció                                          |
+=======================+======================================================+
|      _id_contador_    | Tal com hi apareix al _fitxer de ruta_.              |
+-----------------------+------------------------------------------------------+
|     _fecha_lectura_   | El valor del camp _fecha_planificada_lectura_ excepte|
|                       | quan la lectura s'hagi recollit de forma electrónica;|
|                       | En aquest cas el valor correspon a la data i hora que|
|                       | el comptador ha registrat per al _tancament_ que s'ha|
|                       | llegit electrònicament.                              |
+-----------------------+------------------------------------------------------+
|    _fecha_registro_   | El valor correspon a la data i hora que s'han        |
|                       | registrat (entrades manualment o descarregades       |
|                       | electrònicament) les lectures del comptador amb      |
|                       | GISCE-TPL. Aquest valor es basa en el rellotge del   |
|                       | terminal; únicament serà fiable si la zona horària,  |
|                       | la data i la hora del terminal estan correctament    |
|                       | configurades.                                        |
+-----------------------+------------------------------------------------------+
| _lectura_electronica_ | Un codi de caràcter, que sempre serà "y" o "n" (per  |
|                       | "yes" i "no"), que indica si la lectura s'ha recollit|
|                       | manualment o bé si s'ha descarregat de forma         |
|                       | electrònica..                                        |
+-----------------------+------------------------------------------------------+
|   _codigo_anomalia_   | La clau de l'anomalia que l'usuari hagi pogut        |
|                       | escollir del _catàleg d'anomalies_.                  |
+-----------------------+------------------------------------------------------+
| _etiqueta_solicitada_ | Un codi de caràcter, que sempre serà "y" o "n" (per  |
|                       | "yes" i "no"), que indica si l'usuari ha sol·licitat |
|                       | que es reemplaci l'etiqueta del comptador (p.e.      |
|                       | perquè falta o està deteriorada)                     |
+-----------------------+------------------------------------------------------+
|    _observaciones_    | Un text lliure amb els comentaris que l'usuari hagi  |
|                       | cregut oportuns anotar. Alguns caràcters es          |
|                       | codifiquen de forma especial:                        |
|                       |                                                      |
|                       | - El caràcter tabulador _"\t"_ es reemplaça per _"~"_|
|                       | - El caràcter seqüència _"\r\n"_ és _"$"_            |
|                       | - El caràcter seqüència _"\n\r"_ és _"$"_            |
|                       | - Els caràcters _"\r" i "\n"_ restants, són _"$"_    |
+-----------------------+------------------------------------------------------+

I en la mateixa línia, per cada magnitud a llegir en el comptador (encara que
la lectura estigui en blanc), aquests quatre camps:

+----------------------+-------------------------------------------------------+
|     Nom del Camp     |  Descripció                                           |
+======================+=======================================================+
|     _id_periodo_     | Tal com apareix en el _fitxer de ruta_                |
+----------------------+-------------------------------------------------------+
|   _nombre_periodo_   | Tal com apareix en el _fitxer de ruta_                |
+----------------------+-------------------------------------------------------+
|  _lectura_anterior_  | Tal com apareix en el _fitxer de ruta_                |
+----------------------+-------------------------------------------------------+
|   _lectura_actual_   | El valor de la magnitud recollit per l'usuari, amb les|
|                      | seguents consideracions:                              |
|                      |                                                       |
|                      | - El número enter o amb decimals segons el criteri    |
|                      |   establert en la descripció del camp _nombre_periodo_|
|                      | - L'usuari ha donat per vàlid el valor tal i com s'ha |
|                      |   guardat. Els valors es _normalitzen_ (per exemple s'|
|                      |   arrodoneixen al número de decimals que correspongui)|
|                      |   i es mostren _normalitzats_ just abans de que       |
|                      |   l'usuari registri les lectures del comptador i      |
|                      |   aquestes siguin emmagatzemades en el _fitxer de     |
|                      |   lectures_.                                          |
|                      | - Excepte en les lectures recollides electrònicament, |
|                      |   on existeix la possibilitat d'error humà. Es        |
|                      |   proveeix de les mesures preventives que s'han       |
|                      |   explicat prèviament.                                |
+----------------------+-------------------------------------------------------+


### Fitxer de corbes (GISCE-TPL → GISCE-ERP)

Per cada corva recollida, GISCE-TPL emmagatzema un fitxer de corva.

El nom del fitxers es composa per:

- El _nom de la ruta_
- Un caràcter guió baix `_` (_underscore_)
- El camp _número_comptador_ (de la mateixa manera que apareix en el _fitxer
  de ruta_)
- La extensió "**.curva**"

Per exemple la corva que es recull per al comptador amb número _123456_ a la
ruta CT-082. tindrà per nom "_CT-082_123456.curva_".

El contingut té els següents camps:

Una línia de capçalera amb els camps:

+----------------------+-------------------------------------------------------+
|     Nom del Camp     |  Descripció                                           |
+======================+=======================================================+
|   _numero_contador_  | El número del comptador com apareix al fitxer de ruta |
+----------------------+-------------------------------------------------------+
|   _numero_de_serie_  | El número de serie que ha reportat el comptador       |
+----------------------+-------------------------------------------------------+
|  _version_firmware_  | Versió del firmware que ha assenyalat el comptador    |
+----------------------+-------------------------------------------------------+
|   _fecha_protocolo_  | Data del estàndard del protocol IEC870REE que         |
|                      | implementa el comptador, tal com ha assenyalat aquest |
+----------------------+-------------------------------------------------------+
| _version_protocolo_  | Versió del protocol IEC870REE que implementa el       |
|                      | comptador, tal com ha assenyalat aquest               |
+----------------------+-------------------------------------------------------+
|      _modelo_        | El model que ha assenyalat el comptador               |
+----------------------+-------------------------------------------------------+
|     _fabricant_      | El codi de fabricant que ha assenyalat el comptador   |
+----------------------+-------------------------------------------------------+

Segona línia a la capçalera, amb els camps:

+------------------------+-----------------------------------------------------+
|     Nom del Camp       |  Descripció                                         |
+========================+=====================================================+
| _fecha_y_hora_lectura_ | La data i hora en la que s'han descarregat les dades|
+------------------------+-----------------------------------------------------+
| _fecha_y_hora_inicial_ | Inici del interval del qual s'han solicitat dades al|
|                        | comptador                                           |
+------------------------+-----------------------------------------------------+
|  _fecha_y_hora_final_  | Final del interval del qual s'han solicitat dades al|
|                        | comptador                                           |
+------------------------+-----------------------------------------------------+
|    _tipo_de_curva_     | Una cadena de dos caràcters que especifica el tipus |
|                        | de curva que s'ha solicitat del comptador.          |
|                        | El primer caràcters és `1` o `2`, per al periode    |
|                        | d'integració 1 (60 minuts) o el periode d'integració|
|                        | 2 (15 minuts). El segon caràcter es una `A` si són  |
|                        | valors absoluts, o una `I` si són valors            |
|                        | incrementals. Per tant els quatre possibles valors  |
|                        | són:                                                |
|                        |                                                     |
|                        | - `1A`                                              |
|                        | - `2A`                                              |
|                        | - `1I`                                              |
|                        | - `2I`                                              |
+------------------------+-----------------------------------------------------+

Zero o més línies de dades, una per cada conjunt de valors de la curva que ha
entregat el comptador:

+--------------------------------+---------------------------------------------+
|          Nom del Camp          |  Descripció                                 |
+================================+=============================================+
|           _data_hora_          | La data i hora de inici del interval        |
|                                | d'integració al que corresponen els totals  |
|                                | d'aquesta línia                             |
+--------------------------------+---------------------------------------------+
|        _activa_entrante_       | Totals integrats d'activa entrant           |
+--------------------------------+---------------------------------------------+
|    _calidad_activa_entrante_   | Byte de qualitat associat al camp anterior  |
+--------------------------------+---------------------------------------------+
|        _activa_saliente_       | Totals integrants d'activa sortint          |
+--------------------------------+---------------------------------------------+
|    _calidad_activa_saliente_   | Byte de qualitat associat al camp anterior  |
+--------------------------------+---------------------------------------------+
|     _reactiva_cuadrante_1_     | Totals integrats de reactiva en el primer   |
|                                | cuadrant                                    |
+--------------------------------+---------------------------------------------+
| _calidad_reactiva_cuadrante_1_ | Byte de qualitat associat al camp anterior  |
+--------------------------------+---------------------------------------------+
|    _reactiva_cuadrante_2_      | Totals integrats de reactiva en el segon    |
|                                | cuadrant                                    |
+--------------------------------+---------------------------------------------+
| _calidad_reactiva_cuadrante_2_ | Byte de qualitat associat al camp anterior  |
+--------------------------------+---------------------------------------------+
|    _reactiva_cuadrante_3_      | Totals integrats de reactiva en el tercer   |
|                                | cuadrant                                    |
+--------------------------------+---------------------------------------------+
| _calidad_reactiva_cuadrante_3_ | Byte de qualitat associat al camp anterior  |
+--------------------------------+---------------------------------------------+
|    _reactiva_cuadrante_4_      | Totals integrats de reactiva en el quart    |
|                                | cuadrant                                    |
+--------------------------------+---------------------------------------------+
| _calidad_reactiva_cuadrante_4_ | Byte de qualitat associat al camp anterior  |
+--------------------------------+---------------------------------------------+

### Catàleg d'anomalies

Una primera part, la _llista de categories_, amb una línia per categoria amb
dos camps:

+------------------------+-----------------------------------------------------+
|      Nom del Camp      | Descripció                                          |
+========================+=====================================================+
|     _id_categoria_     | Un enter, diferent per cada categoria               |
+------------------------+-----------------------------------------------------+
| _descripcion_anomalia_ | El nombre de la categoria. No ha de contenir retorns|
|                        | de línia (`\n` o `\r`) ni tabuladors (`\t`).        |
+------------------------+-----------------------------------------------------+

Una línia en blanc separa la primera part de la segona i última part.
La _llista d'anomalies_. Té una anomalia per línia amb tres camps:

+------------------------+-----------------------------------------------------+
|      Nom del Camp      |  Descripció                                         |
+========================+=====================================================+
|      _id_categoria_    | Un enter, ha de coincidir per força amb el camp     |
|                        | **_id_categoria_** d'alguna de les categories       |
|                        | definides en la primera part d'aquest fitxer.       |
+------------------------+-----------------------------------------------------+
|       _id_anomalia_    | Un valor alfanumèric que ha de ser diferent per cada|
|                        | anomalia. Inclus si estan en diferents categories.  |
+------------------------+-----------------------------------------------------+
| _descripcion_anomalia_ | El nom de la anomalia. No ha de contenir retorns de |
|                        | línia (`\n` o `\r`) ni tabuladors (`\t`).           |
+------------------------+-----------------------------------------------------+

### Catàleg de situacions

Una línia per cada situació, amb dos camps en aquest ordre:

+----------------+-------------------------------------------------------------+
|  Nom del Camp  | Descripció                                                  |
+================+=============================================================+
| _id_situacion_ | Un enter, diferent per cada registre.                       |
+----------------+-------------------------------------------------------------+
| _descripcion_  | No ha de contenir retorns de línia (`\n` o `\r`) ni         |
|                | tabuladors (`\t`).                                          |
+----------------+-------------------------------------------------------------+

### Catàleg d'Avisos

Una línia per cada avís, amb aquests dos camps:


+----------------+-------------------------------------------------------------+
|  Nom del Camp  | Descripció                                                  |
+================+=============================================================+
| _id_aviso_     | Un enter, diferent per cada registre.                       |
+----------------+-------------------------------------------------------------+
| _descripcion_  | No ha de contenir retorns de línia (`\n` o `\r`) ni         |
|                | tabuladors (`\t`).                                          |
+----------------+-------------------------------------------------------------+
