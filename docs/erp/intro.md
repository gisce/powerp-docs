# Entorn de desenvolupament

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

## Opcions de línia de comandes

## Servidor OpenERP i Client Web - Start/Stop

## Apagant el servidor

# Aproximació al desenvolupament modul·lar


# Arquitectura oberta a Objectes - Mvc
