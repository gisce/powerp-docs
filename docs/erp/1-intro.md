..# Entorn de desenvolupament

## Treballant amb 'Launchpad'

Documentació per als desenvolupadors de OpenERP que es troba en la pàgina:
[https://doc.odoo.com/5.0/es/developer/1_1_Introduction/2_launchpad/](https://doc.odoo.com/5.0/es/developer/1_1_Introduction/2_launchpad/)

### Registre i Configuració

Abans de poder fer un commit amb '_launchpad_', primer s'ha de crear un "login".

Accedeix a [https://launchpad.net](https://launchpad.net) --> _log in /
register_ a la part superior dreta.

Entra amb la teva direcció e-mail i espera a rebre un e-mail amb les
instruccions necessaries per crear el login.

Aquest login només és necessari si s'ha de fer un commit com openerp-commiter
o en la teva pròpia branca.

Pots seguir aquest link: [https://help.launchpad.net/YourAccount/NewAccount](https://help.launchpad.net/YourAccount/NewAccount)

Qualsevol contribuidor interessat en ser _commiter_ ha de mostrar el seu interés
per treballar en el projecte OpenERP i la seva capacitat per fer-ho d'una manera
adequada, ja que la sel·lecció d'aquest grup és a través de la meritocràcia.
Es poden proposar correccions d'errors o característiques al nostre sistema de
_bug tracker_.
També és poden suggerir mòduls adicionals i/o funcionalitats en el nostre
sistema _bug tracker_.

Pots afegir-te o contribuir amb l'equip d'OpenERP a través del següent link:
[https://help.launchpad.net/Teams/Joining](https://help.launchpad.net/Teams/Joining)

Els contribuidors són persones que volen ajudar a millorar el projecte, agregar
funcionalitats i millorar l'estabilitat. Qualsevol pot contribuïr en el projecte
amb el seu coneixement, informat d'errors, proposant millores i publicant solucions.

L'equip de la communitat es troba a l launchpad: [https://launchpad.net/~openerp-community](https://launchpad.net/~openerp-community)

Els membres dels equips de qualitat i desenvolupament són automàticament membres
de la comunitat.

### Bazaar (bzr)

#### Instal·lant Bazaar

Bazaar és el controlador de versions del codi font per _launchpad_.

Per instal·lar-lo en qualsevol distribució Ubuntu, s'ha d'editar el fitxer
"_/etc/apt/sources.list_" amb la comanda:

    sudo gedit /etc/apt/sources.list

Agregant un dels grups de línies mostrats a continuació:

    (for ubuntu intrepid 8.10)
    deb http://ppa.launchpad.net/bzr/ubuntu intrepid main
    deb-src http://ppa.launchpad.net/bzr/ubuntu intrepid main

    or (for ubuntu jaunty 9.04)
    deb http://ppa.launchpad.net/bzr/ubuntu jaunty main
    deb-src http://ppa.launchpad.net/bzr/ubuntu jaunty main

    or (for ubuntu karmic 9.10)
    deb http://ppa.launchpad.net/bzr/ubuntu karmic main
    deb-src http://ppa.launchpad.net/bzr/ubuntu karmic main

_intrepid, jaunty i karmic_ són noms de les versions d'Ubuntu. Cal reemplaçar-lo
amb el nom corresponent de la versió que s'utilitza.

A continuació cal executar la següent comanda:

    sudo apt-get install bzr

Per funcionar correctament, cal que _bzr_ tingui, com a mínim, versió 1.3. Pots
visualitzar la versió instal·lada utilitzant la següent comanda:

    bzr --version

Si no com a mínim la versió 1.3, pots revisar aquesta web:
[http://bazaar-vcs.org/Download](http://bazaar-vcs.org/Download)

Per qualsevol distribució Debian, la versió 1.5 es pot obtenir d'aquesta pàgina:
[http://backports.org/debian/pool/main/b/bzr/bzr_1.5-1~bpo40+1_i386.deb](http://backports.org/debian/pool/main/b/bzr/bzr_1.5-1~bpo40+1_i386.deb)

Si es té qualsevol problema amb Bazaar, cal llegir primer les
[F.A.Q.](https://doc.odoo.com/5.0/es/contribute/bazaar_faq/#bazaar-faq-link)
abans de realitzar qualsevol pregunta.

#### Treballant amb branques

Combinant _Bazaar_ amb _Launchpad_, s'obté una bona eina per compartir i col·laborar
amb el codi. Essencialment es pot pujar el codi de la branca en un espai compartit
i ningú pot comprometre les dades de la branca.

Això vol dir que es pot utilitzar Bazaar de la mateixa manera que s'utilitzaria
SVN, per exemple, un allotjament centralitzat que varies persones poden colaborar.
Té un benefici agregat, ja que qualsevol pot afegir la seva pròpia branca personal
i si es desitja tornar a pujar al _Launchpad_.

Aquesta és la forma oficial i propostes per contribuïr a OpenERP i OpenObject.

Per descarregar les últimes versions de les fonts i crear les teves pròpies
branques locals de OpenERP, cal fer el següent:

    bzr branch lp:openerp
    cd openerp
    ./bzr_set.py

Això descarrega tots els components de OpenERP (Servidor, Client i _Plugins_) i
crearà els enllaços dels mòduls en el teu servidor per poder-los utilitzar
directament. Pots modificar el fitxer _bzr_set.py_ per sel·leccionar el que vols
descarregar exactament. Ara, podries editar un fitxer i guardar-lo en la teva
branca personal amb les següents comandes:

    EDIT addons/account/account.py
    cd addons
    bzr ci -m "Testing Modifications"

Una vegada que el teu codi sigui suficientment correcte, seguint la [guia de
codificació](https://doc.odoo.com/5.0/es/contribute/15_guidelines/coding_guidelines/#coding-guidelines-link),
es pot pujar la branca al _Launchpad_. Primer cal crear-se el compte de
_Launchpad_, registrar la clau pública i subscriure's al equip [OpenERP-Community](https://launchpad.net/~openerp-community).
Llavors ja es pot pujar el teu codi. Podem executar les següents comandes:

    cd addons
    bzr push lp:~openerp-community/openobject-addons/YOURLOGIN_YOURBRANCHNAME
    bzr bind lp:~openerp-community/openobject-addons/YOURLOGIN_YOURBRANCHNAME

Després de realitzar això, el teu codi es publicat al _Launchpad_, al [OpenObject
project](https://code.launchpad.net/openobject), i els _commiters_ poden traballar
amb ell, revisar-lo i proposar-lo per una integració amb el codi oficial. La
última línia et permet relacionar el teu codi amb el que es troba el _Launchpad_,
en finalitzar, el teu codi passarà a ser aplicat al _Launchpad_ directament (a
no ser que s'utilitzi el paràmetre `--local`):

    bzr pull    # Get modifications on your branch from others
    EDIT STUFF
    bzr ci    # commit your changes on your public branch

Si els teus canvis arreclen un error públic en _Launchpad_, pots utilitzar
el següent codi per marcar l'error com a corregit pel teu codi:

    bzr ci --fixes=lp:453123   # Where 453123 is a bug ID

Una vegada la teva branca està feta, cal marcar-la com a "_mature_" en la
interfície web de _Launchpad_ i demanar que es posi en la nova versió oficial.

## Configuració

Hi ha dos configuracions, una pel client i una pel servidor. Respectivament:

- ~/.openerprc
- ~/.openerp_serverrc

Aquests fitxers segueixen la convenció per al _ConfigParser_ de Python.

Les linies que comencen per "#" o ";" són comentaris.

El fitxer de configuració del client es genera automaticament al iniciar-lo per
primera vegada.
La configuració per al servidor, en canvi, es pot crear automaticament utilitzant
la següent comanda:

    openerp-server.py -s

En cas de no trobar els fitxers de configuració, el client i el servidor utilitzen
la configuració per defecte.

### Configuració del Servidor

Configuracions disponibles:

+-------------------+--------------------------------------------------------------+
| interface         | Adreça a la que es vincula el servidor                       |
+-------------------+--------------------------------------------------------------+
| port              | Port al que el servidor escolta                              |
+-------------------+--------------------------------------------------------------+
| database          | Nom de la Base de Dades a utilitzar                          |
+-------------------+--------------------------------------------------------------+
| user              | Nom del Usuari per connectar a la Base de Dades              |
+-------------------+--------------------------------------------------------------+
| translate_in      | Fitxer per traduir OpenERP al teu llenguatge                 |
+-------------------+--------------------------------------------------------------+
| translate_out     | Fitxer per exportar el llenguatge del OpenERP                |
+-------------------+--------------------------------------------------------------+
|                   | Especifica els moduls per exportar. S'ha d'utilitzar en      |
| translate_modules | combinació amb el paràmetre de la línia de comandes:         |
|                   | `--i18n-export`                                              |
+-------------------+--------------------------------------------------------------+
| language          | Especificació del llenguatge utilitzat per OpenERP.          |
+-------------------+--------------------------------------------------------------+
| verbose           | Habilita la sortida per debugar                              |
+-------------------+--------------------------------------------------------------+
| init              | Inicialitza un mòdul (Per tots els mòduls, utilitzar _'all'_)|
+-------------------+--------------------------------------------------------------+
| update            | Actualitza un mòdul (Per tots els mòduls, utilitzar _'all'_) |
+-------------------+--------------------------------------------------------------+
| upgrade           | Millora/Instala/Desinstala moduls                            |
+-------------------+--------------------------------------------------------------+
| db_name           | Especifica el nom de la Base de Dades                        |
+-------------------+--------------------------------------------------------------+
| db_user           | Especifica el nom del usuari de la Base de Dades             |
+-------------------+--------------------------------------------------------------+
| db_password       | Especifica la contrasenya de la Base de Dades                |
+-------------------+--------------------------------------------------------------+
| db_host           | Especifica el host (adreça IP) de la Base de Dades           |
+-------------------+--------------------------------------------------------------+
| db_port           | Especifica el port per al host de la Base de Dades           |
+-------------------+--------------------------------------------------------------+
| pg_path           | Especifica el camí al executable _pg_                        |
+-------------------+--------------------------------------------------------------+

Per crear el teu propi fitxer de configuració, inicia el servidor amb el paràmetre
de la línia de comandes `-s` o `--save`.

Si vols iniciar el servidor amb una configuració alternativa, utilitza el
paràmetre de la línia de comandes `-c <config file>` o `--config=<config file>`.

A continuació pots veure una configuració bàsica:

```
[options]
verbose = False
xmlrpc = True
database = terp
update = {}
port = 8069
init = {}
interface = 127.0.0.1
reportgz = False
```

I d'una configuració completa:

```
[printer]
path = none
softpath_html = none
preview = True
softpath = none

[logging]
output = stdout
logger =
verbose = True
level = error

[help]
index = http://www.openerp.com/documentation/user-manual/
context = http://www.openerp.com/scripts/context_index.php

[form]
autosave = False
toolbar = True

[support]
recipient = support@openerp.com
support_id =

[tip]
position = 0
autostart = False

[client]
lang = en_US
default_path = /home/user
filetype = {}
theme = none
toolbar = icons
form_tab_orientation = 0
form_tab = top

[survey]
position = 3

[path]
pixmaps = /usr/share/pixmaps/openerp-client/
share = /usr/share/openerp-client/

[login]
db = eo2
login = admin
protocol = http://
port = 8069
server = localhost
```

### Configuració del client

Configuracions disponibles:

+----------------------------------------------------------------------------------+
| Secció _login_                                                                   |
+==================+===============================================================+
| login            | Nom per autentificar-se al OpenERP server                     |
+------------------+---------------------------------------------------------------+
| server           | Adreca utilitzada per el servidor                             |
+------------------+---------------------------------------------------------------+
| port             | Port utilitzat per el servidor                                |
+------------------+---------------------------------------------------------------+

+----------------------------------------------------------------------------------+
| Secció _path_                                                                    |
+==================+===============================================================+
| share            | Camí utilitzat per trobar els fitxers compartits d'OpenERP    |
+------------------+---------------------------------------------------------------+
| pixmaps          | Camí utilitzat per trobar els fitxers _pixmap_ d'OpenERP      |
+------------------+---------------------------------------------------------------+

+----------------------------------------------------------------------------------+
| Secció _tip_                                                                     |
+==================+===============================================================+
| autostart        | Definir si s'han de mostrar o no consells al iniciar el client|
+------------------+---------------------------------------------------------------+
| position         | Número del consell que mostrarà el client                     |
+------------------+---------------------------------------------------------------+

+----------------------------------------------------------------------------------+
| Secció _form_                                                                    |
+==================+===============================================================+
| autosave         | El client guardarà automàticament els canvis realitzats       |
|                  | en els registres                                              |
+------------------+---------------------------------------------------------------+

+----------------------------------------------------------------------------------+
| Secció _printer_                                                                 |
+==================+===============================================================+
| preview          | Previsualitza els reports avans d'imprimir-los                |
+------------------+---------------------------------------------------------------+
| softpath         | Camí al previsualitzador de pdf                               |
+------------------+---------------------------------------------------------------+
| softpath_html    | Camí al previsualitzador de html                              |
+------------------+---------------------------------------------------------------+
| path             | Comanda utilitzada per imprimir                               |
+------------------+---------------------------------------------------------------+


+----------------------------------------------------------------------------------+
| Secció _logging_                                                                 |
+==================+===============================================================+
|                  | Canals per mostrar al log. La llista de valors a mostrar és:  |
|                  |                                                               |
|                  | - @common@                                                    |
|                  | - @common.message@                                            |
|                  | - @view@                                                      |
| logger           | - @view.form@                                                 |
|                  | - @common.options@                                            |
|                  | - @rpc.request@                                               |
|                  | - @rpc.result@                                                |
|                  | - @rpc.exception@                                             |
+------------------+---------------------------------------------------------------+
| level            | Nivell del log a mostrar                                      |
+------------------+---------------------------------------------------------------+
| output           | Fitxer utilitzat per el logger                                |
+------------------+---------------------------------------------------------------+
| verbose          | Fixa el nivell del logger a INFO                              |
+------------------+---------------------------------------------------------------+

+------------------------------------------------------------------------------------+
| Secció _client_                                                                    |
+==================+=================================================================+
| default_path     | Camí per defecte utilitzat pel client quan guarda/carrega dades |
+------------------+-----------------------------------------------------------------+


Exemple de configuració:

```
[login]
login = admin
port = 8069
server = 192.168.1.4

[printer]
path = none
preview = True
softpath = none

[logging]
output = stdout
logger =
verbose = True
level = ERROR

[form]
autosave = False

[client]
default_path = /home/user
```


## Opcions de línia de comandes

#### Opcions generals
+---------------------------------+----------------------------------------------------+
| --version                       | Mostra la versió del programa i surt               |
+---------------------------------+----------------------------------------------------+
| -h, --help                      | Mostra aquest missatge d'ajuda i surt              |
+---------------------------------+----------------------------------------------------+
| -c _CONFIG_,                    | Especifica un fitxer de configuració alternatiu    |
|                                 |                                                    |
| --config=_CONFIG_               |                                                    |
+---------------------------------+----------------------------------------------------+
| -s, --save                      | Guarda la configuració a ~/.terp_serverrc          |
+---------------------------------+----------------------------------------------------+
| -v, --verbose                   | Activa debugging                                   |
+---------------------------------+----------------------------------------------------+
| --pidfile=_PIDFILE_             | Fitxer on es guardarà el pid del servidor          |
+---------------------------------+----------------------------------------------------+
| --logfile=_LOGFILE_             | Fitxer on es guardarà el log del servidor          |
+---------------------------------+----------------------------------------------------+
| -n _INTERFACE_,                 | Especifica l'adreça TCP IP                         |
|                                 |                                                    |
| --interface=_INTERFACE_         |                                                    |
+---------------------------------+----------------------------------------------------+
| -p _PORT_, --port=_PORT_        | Especifica el port TCP                             |
+---------------------------------+----------------------------------------------------+
| --net_interface=_NETINTERFACE_  | Especifica l'adreça TCP IP per netrpc              |
+---------------------------------+----------------------------------------------------+
| --net_port=_NETPORT_            | Especifica el port TCP per netrpc                  |
+---------------------------------+----------------------------------------------------+
| --no-netrpc	                  | Desactiva netprc                                   |
+---------------------------------+----------------------------------------------------+
| --no-xmlrpc                     | Desactiva xmlrpc                                   |
+---------------------------------+----------------------------------------------------+
| -i _INIT_, --init=_INIT_        | Inicia un mòdul (utilitzar "all" per tots els      |
|                                 | mòduls)                                            |
+---------------------------------+----------------------------------------------------+
| --without-demo=_WITHOUT_DEMO_   | Carrega dades de demo per un mòdul                 |
|                                 | (utilitzar "all" per tots els mòduls)              |
+---------------------------------+----------------------------------------------------+
| -u _UPDATE_, --update=_UPDATE_  | Actualitza un mòdul (utilitzar "all" per tots els  |
|                                 | mòduls)                                            |
+---------------------------------+----------------------------------------------------+
| --stop-after-in                 | Atura el servidor després de que s'inicialitzi     |
+---------------------------------+----------------------------------------------------+
| --debug                         | Habilita el mode debug                             |
+---------------------------------+----------------------------------------------------+
| -S, --secure                    | Engega el servidor per HTTPS en comptes d'HTTP     |
+---------------------------------+----------------------------------------------------+
| --smtp=_SMTP_SERVER_            | Especifica el servidor SMTP per enviar un mail     |
+---------------------------------+----------------------------------------------------+
| -price_accuracy=_PRICE_ACCURACY_| Especifica el price accuracy                       |
+---------------------------------+----------------------------------------------------+

#### Opcions relacionades amb la base de dades
+------------------------------------+----------------------------------------------------+
| -d _DB_NAME_, --database=_DB_NAME_ | Especifica el nom de la base de dades              |
+------------------------------------+----------------------------------------------------+
| -r _DB_USER_, --db_user=_DB_USER_  | Especifica el nom d'usuari de la base de dades     |
+------------------------------------+----------------------------------------------------+
| -w _DB_PASSWORD_,                  | Especifica la contrasenya de la base de dades      |
|                                    |                                                    |
| --db_password=_DB_PASSWORD_        |                                                    |
+------------------------------------+----------------------------------------------------+
| --pg_path=_PG_PATH_                | Especifica el path del pg executable               |
+------------------------------------+----------------------------------------------------+
| --db_host=_DB_HOST_                | Especifica el host de la base de dades             |
+------------------------------------+----------------------------------------------------+
| --db_port=_DB_PORT_                | Especifica el port de la base de dades             |
+------------------------------------+----------------------------------------------------+


#### Opcions per a la internacionalització (traducció)

Utilitzar aquestes opcions per traduir l'OpenERP a un altre idioma.

+-------------------------------+----------------------------------------------------+
| -l _LANGUAGE_,                | Especifica  l'idioma de l'arxiu de traduccions.    |
|                               | Utilitzar amb --i18n-export i --i18n-import        |
| --language=_LANGUAGE_         |                                                    |
+-------------------------------+----------------------------------------------------+
| --i18n-export=_TRANSLATE_OUT_ | Exporta tots els strings per traduir a un arxiu    |
|                               | CSV i surt                                         |
+-------------------------------+----------------------------------------------------+
| --i18n-import=_TRANSLATE_IN_  | Importa un fitxer CSV amb traduccions i surt       |
+-------------------------------+----------------------------------------------------+
| --modules=_TRANSLATE_MODULES_ | Especifica els mòduls per exportar. Utilitzar en   |
|                               | combinació amb --i18n-export                       |
+-------------------------------+----------------------------------------------------+

## Servidor OpenERP i Client Web - Start/Stop

#### OpenERP 4.2

Primer s'ha de comprovar que totes les dependències necessàries estan instal·lades.
Després es crea el terp de la base de dades. Ens hem d'assegurar que el nostre
usuari té les credencials correctes per crear bases de dades amb PostgreSQL. per
més informació en aquest tema consulta el manual de PostgreSQL:

`createdb terp --encoding=unicode`

Un cop hem creat la base de dades, podem iniciar l'OpenERP. El contingut de la
base de dades es crearà automàticament al primer inici:

`./tinyerp-server.py`

#### OpenERP 5.0 i superior

- Comprovem que totes les dependències necessàries estan instal·lades.
- Assegurar-nos que estem en un usuari que té permisos d'administrador en el
  PostgreSQL. Consulta el manual de PostgreSQL per més informació sobre això.
- Inicia el servidor d'OpenERP

`./openerp-server.py`

Finalment connecta al servidor amb el client GTK i utilitza la opció de Crear
Base de dades per crear la teva base de dades

## Aturant el servidor

La forma més fàcil d'aturar el servidor en un sistema Linux és enviar una senyal
SIG INT al servidor.

- Busca el Process ID

    `ps ax | grep -i tiny`

- Utilitza la comanda kill amb el pid

    `kill -2 pid`


# Aproximació al desenvolupament modul·lar

## OpenObject Servidor i Mòduls

L'OpenERP té les següents característiques:

- És un sistema client/servidor que treballa sobre una xarxa IP.
- El llenguatge de programació és Python.
- Utilitza tecnologies orientades a objectes (Object-Oriented).
- Emmagatzema les dades amb una base de dades relacional de PostgreSQL.
- Els Business Objects estan modelats amb un sistema ORM (Object Relational
  Mapping).
- Ofereix tres Human Machine Interfaces (HMI): un client GTK, un client QT i un
  client web (eTiny).
- Utilitza XML per a diferents propòsits: descriure dades, vistes, reports,
  transport de dades (XML-RPC).

### Arquitectura tècnica

#### Servidor/client, XML-RPC

L'OpenERP està basat en una arquitectura client/servidor. El servidor i el client
es comuniquen utilitzant el protocol XML-RPC. XML-RPC és un protocol molt senzill
que permet al client fer crides de procediments remots. La funció que es crida,
els seus arguments i el resultat són enviats per HTTP i codificats utilitzant XML.

Per a més informació sobre XML-RPC, si us plau mira el següent: http://www.xml-rpc.com/

Des de la versió 4.2, hi ha un nou protocol entre el client i el servidor que ha
estat anomenat net-rpc. Aquest està basat en la funció cPickle de python i és
més ràpid que el XML-RPC.

#### Client

La lògica de l'OpenERP és purament en el costat del servidor. El client és molt
senzill; la seva feina és la de preguntar dades (formularis, llistes, arbres)
del servidor i retornar-les. Amb aquesta aproximació, quasi tots els
desenvolupaments són fets al costat del servidor. Això fa de que l'OpenERP sigui
més fàcil de desenvolupar i mantenir.

El client no entén què envia. Fins i tot les accions com "Fer click al botó
d'imprimir" són enviades al servidor per preguntar com reaccionar.

L'operació del client és molt senzilla; quan l'usuari realitza una acció (guardar
un formulari, obrir un menú, imprimir, ...) aquest envia l'acció al servidor.
Després el servidor envia la nova acció a executar al client.

Hi ha tres tipus d'acció:

- Obrir una finestra (formulari o arbre)
- Imprimir un document
- Executar un assistent (wizard)

#### Arquitectura

![](_static/arquitectura_client_servidor.png)

Explicació dels mòduls:


Server - Base distribution

Utilitzem un mecanisme de communicació distribuïda dins del servidor del OpenERP. El nostre motor soporta les plantilles distribuides més comuns: petició/resposta  (request/reply), publicació/subscripció (publish/subscribe), monitorització (monitoring), disparador/devolució (triggers/callback),...

Hi poden haver diferents Business Objects en diferents ordinadors o els mateixos objectes poden estar en múltiples ordinadors per a dur a terme balanç de càrrega en múltiples ordinadors.

Server - Object Relational Mapping (ORM)

Aquesta capa proveeix funcionalitats addicionals per sobre de PostgreSQL:

 - Consistència: comprovació de validacions potent,
 - Treball amb objectes (mètodes, referències,...)
 - Seguretat de files (per usuari, grup, rol)
 - Accions complexes en un grup de recursos
 - Herència

 Server - Web-Services

 Aquest mòdul de servei web ofereix una interfície comuna per tots els serveis web.

  - SOAP
  - XML-RPC
  - net-rpc

  Els Business Objects poden ser accessibles també mitjançant el mecanisme de objectes distribuits. Poden ser modificats des de l'interfície del client amb les vistes contextuals.

  Server - Workflow Engine

  Els fluxos de treball (workflows) són gràfics representats per Business Objects que descriuen la dinàmica de la companyia. Els fluxos de treball també són usats per seguir processos que evolucionen al llarg del temps.

  Un exemple de un flux de treball usat en l'OpenERP:

  Un ordre de venta genera una factura i un ordre d'enviament.

  Server - Report Engine

  Els informes en l'OpenERP poden ser renderitzats de les maneres seguents:

   - Informes personalitzats: aquests poden ser directament creats mitjançant la interfície del client sense necessitat de programar. Són representats per business objects (ir.report.custom)
   - Informes personalitzats d'alta qualitat usant openreport: no requereixen programació però has d'escriure dos petits fitxers XML:
      - Una plantilla que indica les dades que planejes
      - una fulla d'estils XSL:RML
   - Informes codificats directament
   - Plantilles de OpenOffice Writer

  Quasi tots els informes estàn produits en PDF:

  Server - Business objects

  Quasi tot és un Business Objects en l'OpenERP. Descriuen les dades del programa (fluxos de treball, factures, usuaris, informes personalitzats, ...). Els Business Objects són descrits usant els mòduls ORM. Són persistents i poden tenir múltiples vistes (descrits per l'usuari o calculades automàticament).

  Els Business Objects estàn estructurats en el directori /module.

  Client - Wizards

  Els Wizards són gràfics d'accions/finestres que l'usuari pot efectuar durant una sessió.

  Client - Widgets

  Els Widgets són probablement, encara que l'origen sembla difícil de traçar, "WIndow gaDGETS" en el món IT, que vol dir que són gadgets abans de tot, que implementen funcionalitats elementals a través d'una eina virual portàtil.

  Tots els widgets comuns estàn soportats:

   - Entrades
   - Caixes de text
   - Nombres de coma flotant
   - Dates (amb calendari)
   - Caselles de verificació
   - ...

  També hi ha widgets especials:

   - Botons i crides a accions
   - Widgets de referències
      - 1:1 (one2one)
      - n:1 (many2one)
      - n:m (many2many)
      - 1:n en llista (one2many en llista)
      - ...

  Els Widgets tenen apariències diferents en les diferents vises. Per exemple, el widget de la data en el quadre de cerca representa dos dates normals per un rang de dates (des de...fins...).

  Alguns Widgets poden tenir diferents representacions depenent del context. Per exemple, el widget 1:n (one2many) pot ser representat com un formulari amb pàgines múltiples o com una llista de múltuples columnes.

  Els esdeveniments en els mòduls de Widgets són processats mitjançant un mecanisme de retorn (callback). Un mecanisme de retorn és un process on un element defineix el tipus d'esdeveniments que pot manipular, els mètodes del qual han de ser cridats quan un esdeveniment es "disparat" (triggered). Una vegada l'element es disparat, el sistema sap que l'esdeveniment està lligat a un mètode específic, i seguidament el crida. Per tant, fa un retorn (callback).




# Arquitectura oberta a Objectes - MVC
