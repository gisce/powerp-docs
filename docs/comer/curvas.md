# Configuració de càrrega de corbes horàries

En aquest apartat es documentarà el procediment necessari a seguir per
tal de tenir configurat l'ERP perquè carregui periòdicament tots els
documents amb les corbes horàries.


## Configurar el client ERP

### Funcionament
Aquesta funcionalitat ens permet descarregar dels portals de les distribuïdores
les corbes CCH generades per els contractes integrats en el sistema de
telegestió. Aquest servei s'ha d'oferir a través del protocol SFTP
(FTP per SSH). Es poden descarregar els diferents tipus de corbes definits per
la CNMC:

* **CCH_FACT**: Corba utilitzada per facturar. Es distribueix en el format
    **F5D** i no pot tenir forats. El format **RF5D** és idèntic al format F5D
    i s'utilitza per les corbes de les factures rectificades
* **CCH_VAL**: Corba validada. Només inclou aquells registres horaris que
    el comptador ha donat per vàlid i es distribueix en el format **P5D**. Pot
    no estar completa i per tant no és utilitzable per facturar mitjançant corba
* **CCH_CONS**: Corba facturada (CCH_FACT) en format CCH_CONS preparada
     per distribuïr-la al consumidor

Les corbes s'emmagatzemen en el servidor *mongodb*, cadascuna en una
col·lecció diferent, i són accessibles des del ERP a través del comptador.

També es poden utilitzar per facturar.

El sistema es configura de la següent forma:

* **Servidors SFTP**: Servidor SFTP definits per les distribuïdores. En
alguns casos, les distribuïdores s'agrupen i utilitzen un sol servidor
compartit
* **Proveïdors**: Cada proveïdor referencia un servei SFTP concret i
defineix quins fitxers dels disponibles es vol descarregar. Es registra la
data del darrer fitxer descarregat per poder portar-ne el control.


### Instal·lar el mòdul

Ens cal el mòdul anomenat "giscedata_telegestio_comer" per portar a terme
aquesta tasca. Per tal de comprovar si el mòdul està instal·lat o instalar-lo
ens hem de dirigir a **_Administració > Administració de mòduls > Mòduls_**.
Aquí buscarem el mòdul i l'instal·larem si és necessari.


### Configurar connexions sftp

Per tal de que l'ERP sàpiga on anar a buscar els arxius de corbes hem de crear
registres que l'hi indiquin. Anant a **_Infraestructura > Telegestió comer >
Config > SFTP Connections_** podrem crear entrades per cada sftp de cada
distribuïdora que ens interessi.
Haurem d'indicar:

* **Descripció**: Nom descriptiu del servidor
* **Servidor**: Direcció del servidor sftp
* **Port**: Port en el qual està escoltant el servidor
* **Usuari**: Usuari d'accés subministrat per la Distrïbuidora
* **Password**: Paraula clau d'accés al servidor

En alguns casos, es pot fer necessari utilitzar claus privades per accedir
als servidor tal com permet el protocol SSH i per extensió SFTP.

* **Binari de la clau Privada**: Clau privada utilitzada per a l'intercanvi
de claus
* **Password de la clau privada**: Si és el cas, password de la clau privada

Els camps directori arrel i el directori de lectura no s'utilitzen de moment

![Configuració SFTP](_static/curvas/sftp_config.png)


### Configurar proveïdors

En aquest pas hem de crear registres nous per totes les empreses distibuïdores
de les quals rebem corbes horàries. Per fer-ho anem a **_Infraestructura >
Telegestió comer > Config > TG Comer Provider_** i creem els nous registres

La configuració es realitza de la següent forma:

* **Description**: Descripció del proveïdor
* **Enabled**: Especifica si aquest proveïdor està habilitat. Només es
descarreguen els seus fitxers si el proveïdor està habilitat
* **Utility**: Distribuïdor del qual es descarreguen els fitxers.
* **Utility sftp service**: Configuració SFTP utilitzada de les configurades en
el punt anterior

Per cada tipus de fitxer a descarregar s'han de definir diversos paràmetres. Els
més delicats són el nom dels fitxers i la data d'accés.

Per cada apartat:

* **Enabled**: Habilita aquest tipus de fitxer
* **File syntax**: Format del fitxer (veure [Format del nom de fitxer](#nom-dels-fitxers-de-corbes) )
* **Remote Folder**: Fitxer on començar la cerca recursiva. per defecte l'arrel del servidor FTP (*/*)
* **Acces date**: Data del fitxer descarregat més recent

Es defineixen 4 apartats:

* **F5D Settings**: Fitxers CCH_FACT en format F5D.
* **P5D Settings**: Fitxers CCH_VAL en format P5D.
* **CCHCONS Settings**: Fitxers CCH_CONS en format CCH_CONS.
* **RF5D Settings**: Sobreescriuen les corves CCH_FACT

La descàrrega s'automatitzarà mitjançant un cron o tasca programada del
servidor, normalment un cop al dia. Cada cop es descarregaràn els fitxers dels
apartats "habilitats" de tots els proveïdors "habilitats" que tinguin el format
definit i amb data de fitxer en el servidor SFTP posterior a la emmagatzemada.

Els fitxers s'emmagatzemaràn localment en el servidor per al seu posterior
procés en l'adreça definida per la variable de configuració _tg_comer_cch_dir_
tal com es comenta a [aquí](#creacio-de-nova-variable-de-configuracio)

![Configuració Proveïdor](_static/curvas/provider_config.png)


#### Nom dels fitxers de Corbes

Els fitxers de corbes tenen un nom definit per la CNMC. El sistema de
descàrrega de corbes utilitza expressions regulars per decidir quins fitxers es
descarrega i a quina col·lecció els emmagatzema.
 En l'exemple es pot veure la definició més habitual:

 `F5D_0999_0888_(\d{8})`

On *F5D_* serà el format, *0999* la distribuïdora (codi REE), *0888* la nostra
comercialitzadora (codi REE) i *(\d{8})* indica 8 caràcters numèrics, que
equival a la data del fitxer en format YYYYMMDD.

Es farà una cerca recursiva en el servidor SFTP buscant els fitxers que
compleixin aquest format

!!! tip
    En un servidor SFTP compartit, es poden utilitzar les expressions regulars
    per descarregar els fitxers de totes les distribuïdores amb una sola
    configuració de proveïdor. Per exemple:

    `P5D_(\d{4})_0888_(\d{8})`

    En aquest cas es descarregaran tots els fitxers P5D de la nostra
    comercialitzadora (0888) independentment de la distribuidora, que sempre
    serà un codi de quatre caràcters numèrics *(\d{4})*

#### Data de descàrrega

Per no descarregar el mateix fitxer més d'un cop, s'emmagatzema la data del
últim fitxer descarregat. Només es descarregaran els fitxers més nous d'aquesta
data


### Creació de nova variable de configuració

Hem de crear una nova variable de configuració anomenada *tg_comer_cch_dir* amb
el la ruta on volem que es guardin els fitxers descarregats dels
servidors sftp.
**_Administració > Configuració > Propietats > Configuration Variables_**

!!! warning

    Els fitxers descarregats no s'esborrán
