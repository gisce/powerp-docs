# Configuració de càrrega de corbes horàries


    En aquest apartat es documentarà el procediment necessari a seguir per
    tal de tenir configurat l'ERP perquè carregui periòdicament tots els
    documents amb les corbes horàries.


## Configurar el client ERP


### Instal·lar el mòdul

    Ens cal el mòdul anomenat "giscedata_telegestio_comer" per portar a terme
    aquesta tasca. Per tal de comprovar si el mòdul està instal·lat o instalar-lo
    ens hem de dirigir a **_Administració > Administració de mòduls > Mòduls_**.
    Aquí buscarem el mòdul i l'instal·larem si és necessari.


### Configurar connexions sftp

    Per tal de que l'ERP conegui on anar a buscar els arxius de corbes hem de crear
    registres que l'hi indiquin. Anant a **_Infraestructura > Telegestió comer >
    Config > SFTP Connections_** podrem crear entrades per cada sftp de cada
    distribuidora que ens interessi. Haurem d'indicar la direcció del servidor i el
    seu port juntament amb l'usuari i la contrassenya per connectar-se. Si se'ns ha
    indicat que és necessària alguna altra clau de seguretat o algun directori
    específic de lectura ho hem d'indicar aquí.

### Configurar porveïdors

    En aquest pas hem de crear registres nous per totes les empreses distibuidores
    de les quals rebem corbes horàries. Per fer-ho anem a **_Infraestructura >
    Telegestió comer > Config > TG Comer Provider_** i creem els nous registres.
    Hem d'indicar a quina distribuidora pertany, relacionar-l'ho amb la connexió sftp
    corresponent que hem creat en el pas anterior. Després podem decidir quins tipus
    de fitxers ens interessa carregar i a quin directori s'ha d'accedir per fer la
    lectura d'aquests fitxers concrets. No podem deixar la data d'accès en blanc per
    tant se n'hi hauria d'introduir una d'anterior a la actual.

### Creació de nova variable de configuració

    Hem de crear una nova variable de configuració anomenada _tg_comer_cch_dir_ amb
    el valor essent la ruta on volem que es guardin els fitxers descarregats dels
    servidors ftp. 
    **_Administració > Configuració > Propietats > Configuration Variables_**
