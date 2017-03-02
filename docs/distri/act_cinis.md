# Índex

1. [CINI Línies d'Alta Tensió](#1-cini-linies-dalta-tensio)
2. [CINI Línies de Baixa Tensió](#2-cini-linies-de-baixa-tensio)
3. [Transformadors](#3-transformadors)
4. [Centres transformadors](#4-centres-transformadors)
5. [Posicions](#5-posicions)
6. [Parcs de Distribució](#6-parcs-de-distribucio)
7. [Subestacions](#7-subestacions)
8. [Cel·les i elements de tall (Fiabilitat)](#8-celles-i-elements-de-tall-fiabilitat)

El document de referència de CINI serà la
[circular 4/2015](https://www.boe.es/boe/dias/2015/07/31/pdfs/BOE-A-2015-8624.pdf)

!!! Note
    Tots els CINI es poden bloquejar marcant la casella “Bloquejar CINI”,
    i tots els càlculs que aquí es descriuen deixaràn de tenir efecte i
    es mantindrà el CINI que li assigni l’usuari.

!!! Note
    Si al fer el càlcul del CINI, una de les posicions del CINI,
    no es pot calcular perquè el camp del que s’ha d’obtenir el valor
    està buit o fora del rang esperat, la posició apareixerà en **blanc**.

P.e. en aquest cas la 5a posició apareix en blanc perquè falta entrar
el valor del tipus de element de la CNMC, en la taula corresponent.

![exemle-5a-posicio-buida](_static/act_cini/lat_5a_posicio_buida.png)

# 1. CINI Línies d'Alta Tensió

El CINI de cada tram d’Alta Tensió és calculat a partir de les dades del
propi tram i de les dades de la **línia d’AT** que té vinculada:

![seleccio-lat-en-trams](_static/act_cini/lat_trams_linia.png)

**Primera posició**: 2    
**Segona posició**: 0    
**Tercera posició**:

- S’obté del camp “**Tensió màxima de disseny**” del tram d’Alta Tensió.

![tensio-maxima-en-trams](_static/act_cini/lat_trams_tensio_max.png)

Si el camp de la “**Tensió màxima de disseny**” del tram d’AT és buit o zero,
s’obté del camp “**Tensió**” de la **línia d’Alta Tensió**
associada al tram d’AT:

![canvi-lat-en-tram](_static/act_cini/lat_trams_linia_tensio_max_0.png)

![canvi-tensio-en-tram-lat](_static/act_cini/lat_trams_tensio_max.png)

**Quarta posició**:

- Tensada sobre postes, un circuito = **1**: si el valor del camp
  **tipus de línia d’AT = Aeria** i el valor del camp **Circuits = 1**.
- Tensada sobre postes, doble circuito = **2**: si el valor del camp
  **tipus de línia d’AT = Aeria** i el valor del camp **Circuits = 2**.
- Tensada sobre postes, más de dos circuitos = **3**: si el valor del camp
  **tipus de línia d’AT = Aeria** i el valor del camp **Circuits > 2**.
- Subterránea, un circuito = **7**: si el valor del camp
  **tipus de línia d’AT = Subterranea** i el valor del camp **Circuits = 1**
- Subterránea, doble circuito = **8**: si el valor del camp
  **tipus de línia d’AT = Subterranea** i el valor del camp **Circuits = 2**
- Subterránea, doble circuito = **9**: si el valor del camp
  **tipus de línia d’AT = Subterranea** i el valor del camp **Circuits > 2**
- No es contemplen altres casos per les **línies d’Alta Tensió**.

![](_static/act_cini/lat_aeria_circuits.png)

**Cinquena posició**:

-El número de conductors s’obté del camp **conductors** del tramd’Alta Tensió:

![](_static/act_cini/lat_conductors_simplex.png)

**Sisena posició**:

- La secció s’obté del camp **Secció** del **Conductor** associat
  al tram d’Alta Tensió.

![](_static/act_cini/lat_trams_conductor.png)

![](_static/act_cini/lat_conductor_seccio.png)


**Setena posició**:

- La tensió s’obté del camp **Tensió** de la **línia** vinculada al
  tram d’Alta Tensió, igual que a la **tercera posició**.

# 2. CINI Línies de Baixa Tensió

**Primera posició**: 2
**Segona posició**: 0
**Tercera posició**:

- La tensió s’obté del camp **Voltatge** de **l’element de Baixa Tensió**.

![](_static/act_cini/lbt_elements_voltatge.png)

**Quarta posició**:

- En les línies de **baixa tensió**, el **número de circuits**
  té un valor fix de **1**.
- Tensada sobre postes, un circuito = **1**: si el valor del camp
  **Tipus de línia de BT = Aèria** i el camp **Posada en façana = desactivat**.
- Apoyada sobre fachada, un circuito = **4**: si el valor del camp
  **Tipus de línia de BT = Aèria** i el camp **Posada en façana = activat**.
- Subterránea, un circuito = **7**: si el valor del camp
  **Tipus de línia de BT = Subterrània**

![](_static/act_cini/lbt_posada_facana_aeria.png)

**Cinquena posició**:

- **Símplex = 1**: el número de conductors en les
  **línies de Baixa Tensió** és de **1**.

**Sisena posició**:

- La secció s’obté del camp **Secció** del **Cable** associat
  **l’element de Baixa Tensió.**

![](_static/act_cini/lbt_element_cable.png)

![](_static/act_cini/lbt_cable_seccio.png)

**Setena posició**:

- La tensió s’obté del camp **Voltatge** de **l’element de Baixa Tensió**,
  igual que a la **tercera posició**.

# 3. Transformadors

**Primera posició**: 2    
**Segona posició**: 7    
**Tercera posició**:

- La tensió s’obté de la **connexió activa** de la
  pestanya **connexions del transformador**.
- S’obté del camp **(V) P1** si **P2 Con** està desactivat.
- Si **P2 Con** està activat, llavors agafa la tensió = **(V) P2**.

![](_static/act_cini/trafo_conn_vP1.png)

**Quarta posició**:
- La tensió s’obté de la **connexió activa** de la
  pestanya **connexions del transformador**.
- S’obté a partir dels camps **(V) B1, (V) B2** i **(V) B3**,
  dels quals obtindrà la que sigui superior.

![](_static/act_cini/trafo_conn_b1-3.png)

**Cinquena posició**:

- en subestació = **1**: si el camp **Centre Transformador** del
  **transformador** és una **subestació**
- en un centre de transformació = **2**: si el **Centre Transformador**
  del **transformador** és un **CT**.

![](_static/act_cini/trafo_placa_ct.png)

**Sisena posició**:

- La potència s’obté del camp **Potència nominal (KVA) del transformador**.

![](_static/act_cini/trafo_placa_potencia.png)

**Setena posició**:

- Trafo en funcionament = **0**: el camp **estat del transformador**,
  el valor del camp **codi = 1**
- Trafo de reserva = **1**: el camp **estat del transformador**,
  el valor del camp **codi = 7**
- Trafo móvil = **2**: No està contemplat.
- Qualsevol altre valor en el camp **estat del transformador**,
  que no està contemplat, **deixarà en blanc** la setena posició.

![](_static/act_cini/trafo_estat_func.png)

![](_static/act_cini/trafo_estat_reserv.png)

El CINI dels transformadors que es troben en el magatzem serà: **I2900600**.

# 4. Centres transformadors

**Primera posició**: 2    
**Segona posició**: 2    
**Tercera posició**: 4    
**Quarta posició**: 5    
**Cinquena posició**:

 **1.** Busca el valor del camp codi de la categoria CNE del tipus de CT.

![](_static/act_cini/ct_tipus_caseta.png)

![](_static/act_cini/ct_tipus_caseta_dins.png)

![](_static/act_cini/ct_tipus_caseta_cne.png)

Intemperie = **1** si el valor del camp **codi = I**
Caseta = **2** si el valor del camp **codi = C**
Local = **3** si el valor del camp **codi = L**
Subterraneo = **4** si el valor del camp **codi = S**
Movil = **4** , no aplica.

**Sisena posició:**

- S’obté a partir del camp **Tensió de primari [V]** /1000.

Adopta el valor que coincideix amb la tensió indicada del CINI,
i si no coincideix adopta el codi de la immediatament superior.

**Setena posició**:

La potència del centre transformador es calcularà com la suma de tots
els transformadors en estat **funcionament**.  Els de reserva, i els
de client i qualsevol altre estat no es tindran en compte.

Segons indica la circular 4771, a la pàgina 37859:

*“Si la potencia del centro de transformación de la tabla tipologías no*
*coincide con las indicadas, se seleccionará la inmediatamente superior.*
*Para Centros de transformación con dos máquinas de diferente potencia,*
*la potencia a seleccionar será la semisuma de las potencias*
*de las dos máquinas. De no coincidir con las potencias indicadas*
*en la Tipología, se elegirá el Tipo de maquina con la potencia*
*inmediatamente superior.*

*En caso de centros de transformación con tres o más máquinas se clasificará*
*como TI-000 (Instalación no asimilable).*

*Los centros de reparto, los centros de medida y los centros de seccionamiento*
*se  declararán como TI-000 (instalación no asimilable), asignándoles su CINI*
*correspondiente. Si dichos centros dispusieran de más de 4 posiciones,*
*la diferencia entre el número total de posiciones de ese centro y las 4*
*posiciones consideradas, deberán ser declaradas en el nodo*
*«posiciones equipadas con interruptor en subestaciones».*

*Todas las posiciones deben constar de interruptor.”*

!!! Note
    **Exemple:**
    Si el CT te una màquina de 315 kVA, com que els barems CNMC són 250KVA
    o 400KVA, hem d’agafar el valor immediatament superior (400 KVA),
    per tant el valor adoptat serà la H.

Quan hi hagin **dues màquines** el càlcul de la potència de la màquines
es farà fent la semisuma de les potencies de les dues màquines.

!!! Note
    **Exemple:**
    Si el CT te una màquina de 400 kVA i una de 630 kVA,
    1030/2= 515 el valor adoptat serà S 2x630 kVA

!!! Note
    **Exemple:**
    Si el CT te una màquina de 500 kVA i una de 1000 kVA,
    1500/2= 750 el valor adoptat serà T 2x1000 kVA.
    (és l’immediatament superior)

# 5. Posicions

**Primera posició**: 2    
**Segona posició**: 8    
**Tercera posició**:

- S’obté del camp “Tensió a aplicar” de la tensió de la posició:

![](_static/act_cini/posicio_tensio.png)

![](_static/act_cini/posicio_tensio_aplicar.png)

**Quarta posició**:

- Posición con interruptor = **2**: si al camp “**Tipus interruptor**”
  de la posició = **Interruptor automàtic**
- Posición sin interruptor = **3**: si al camp “**Tipus interruptor**”
  de la posició = **Sense interruptor**

![](_static/act_cini/posicio_tipus_interruptor.png)

**Cinquena posició**:

- Els valors per calcular el cinquè camp s’obtenen dels següents camps:
	- Camp **Tecnologia** de la posició
	- **Interior**: si el camp **Tipus** de la
    **subestació de la posició, l’id = ‘L’, ‘C’ o ‘S’**
	- **Intempèrie**: si el camp **Tipus** de la
    **subestació de la posició, l’id = ‘I’**

![](_static/act_cini/posicio_se-tec.png)

![](_static/act_cini/posicio_se_tipus.png)

![](_static/act_cini/posicio_caseta-tipus_id.png)

**Sisena posició**:

- S’obté del camp “**funció**” de la posició. Si el valor del camp
  posició linia = **Altre**, la sisena posició del CINI **quedarà en blanc**.

![](_static/act_cini/posicio_funcio.png)

**Setena posició**:

- S’obté del camp “**Tensió a aplicar**” de la tensió de la posició,
  de igual forma que a la **tercera posició**.

# 6. Parcs de distribució

**Primera posició**: 2     
**Segona posició**: 8     
**Tercera posició**:

- S’obté del camp “**Tensió a aplicar**” de la tensió del parc:

![](_static/act_cini/parcs_tensio.png)

![](_static/act_cini/parcs_tensio_aplicar.png)

**Quarta posició**: 1    
**Cinquena posició**:

- S’obté del camp “**Tecnologia**” del parc:

![](_static/act_cini/parcs_tecno.png)

**Sisena posició**:

- S’obté del camp “**Configuració**” del parc:

![](_static/act_cini/parcs_config.png)

**Setena posició**:

- S’obté del camp “**Tensió a aplicar**” de la tensió del parc,
  de igual forma que a la **tercera posició**.

# 7. Subestacions

**Primera posició**: 2     
**Segona posició**: 1    
**Tercera posició**:

- S’obté del camp “**Tensió primari**” de la subestació.

![](_static/act_cini/se_tensio_primari.png)

**Quarta posició**:

- S’obté del camp “**Tensió secundari**” de la subestació:

![](_static/act_cini/se_tensio_secundari.png)

**Cinquena posició**:

- S’obté del camp “**Tecnologia**” de la subestació:
    1. Si **tecnologia = Convencional**
    2. Si **tecnologia = Blindada**
    3. Si **tecnologia = Mòbil**

![](_static/act_cini/se_tecnologia.png)

**Sisena posició**:

- Es sumen les potències nominals dels transformadors
  que estan en funcionament.    
  Es consideren en funcionament tots els transformadors
  que tinguin un codi d’estat = **1**.

![](_static/act_cini/se_estat.png)

- Si no hi ha cap transformador en funcionament o la suma de potències és 0,
  es posarà el valor **Z** a la sisena posició.    
- Per cada transformador, la potència s’obté del camp
  **Potència nominal (KVA) del transformador**.

![](_static/act_cini/se_trafo_potencia.png)

**Setena posició**: posició no utilitzada = 0

# 8. Cel·les i elements de tall (Fiabilitat)

**CINI: I26** - element de fiabilitat    
**3a posició**: tensió normalitzada

![](_static/act_cini/celes_tensio.png)

**4a posició**: sempre 0 zero    
**5a posició**:

![](_static/act_cini/celes_tipus_element.png)

- Aquesta posició es calcula a partir del valor del camp
  **Tipus CNMC CINI** del catàleg de Tipo elemento.

![](_static/act_cini/celes_tipus_element_list.png)

Que es troba al menú:

![](_static/act_cini/celes_list_elements_menu.png)

**6a posició**:

- Per defecte sempre posarà **1**
    - A no ser que estigui marcat **Telemando**, llavors posarà **2**.

![](_static/act_cini/celes_telemando.png)

**7a posició**:

1. Subestació
2. Centre de transformació.

    ![](_static/act_cini/celes_inst_ct.png)

3. Tram de línia

    ![](_static/act_cini/celes_inst_sopAT.png)
