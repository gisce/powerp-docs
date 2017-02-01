# Model de qualitat per la qualitat interna i externa
En aquest capítol definirem el model de qualitat per qualitat interna i externa.

Categoritza els atributs de qualitat del software en sis característiques:

* Funcionalitat
* Fiabilitat
* Usabilitat
* Eficiència
* Mantenibilitat
* Portabilitat

Que es subdivideixen en subcaracterístiques,  segons s’indica a la **figura 4**
del document de la norma _UNE-ISO/IEC 9126-1_. Les subcaracterístiques es poden
mesurar mitjançant mètriques internes o externes.

## Funcionalitat

Es la capacitat del producte software per interactuar amb un o més sistemes
especificats. GISCE-ERP_QS permet la recollida de dades, emmagatzematge i
tractament d'aquestes i finalment dona els resultats definits a la "_ORDEN
ECO / 797/2002_", càlcul dels índex de qualitat _TIEPI, NIEPI i
percentil 80 del TIEPI_

### Adequació

Es defineix com la capacitat del producte software per proporcionar un conjunt
apropiat de funcions per tasques i objectius d’usuari especificats. En el cas
de GISCE-ERP_QS proporciona els resultats del càlcul dels índex de qualitat de
la “_ORDEN ECO /797/2002_”, generant els documents en el format que defineix la
mateixa Ordre.

### Exactitud

Es defineix com la capacitat del producte software per proporcionar els
resultats o efectes correctes o acordats amb el grau necessari de precisió.
GISCE-ERP_QS dona els resultats dels index de qualitat zonal i individual de
forma exacte ja s’han comprovat els resultats obtinguts amb el producte
software amb altres programes de fulls de càlcul, i els resultats han estat
els mateixos i son correctes.

### Interoperabilitat

Es la capacitat del producte software per interactuar amb un o més sistemes
especificats. GISCE-ERP_QS està integrat amb la base de dades de GISCE-ERP
essent un mòdul més d’aquest ERP del qual obté les dades de les potencies
instal·lades, clients associats a cada CUPS, i els elements de maniobra a
obrir per simular la incidència. Els transformadors que queden sense tensió
degut a una incidència estan relacionats amb la topologia de la xarxa, que
es analitzada amb el mòdul de GIS de GISCE-ERP.

### Seguretat d’accés

Es la capacitat del producte software per protegir informació i dades de manera
que les persones o sistemes no autoritzats no puguin llegir-los o modificar-los,
al temps que no denega l’accés a les persones o sistemes autoritzats.

El Programa GISCE-ERP incorpora un sistema de usuaris, grups i rols que permet
configurar per cada usuari del sistema els drets que té. Un dels punts més
importants de GISCE-ERP es la parametrització dels drets d’accés a la
informació. Per cada grup d’usuaris es defineixen quins menús no seran
accessibles i quins si. També permet que els que tenen accés a les dades
puguin fer-ho només de consulta, i només es permet el dret d’escriptura als
usuaris que designi el client. Els grups determinen els drets dels usuaris,
i els rols determinen els seus deures.

### Acompliment funcional

Es la capacitat que te el producte software per adherir-se a normes,
convencions o legislació i prescripcions similars relacionades amb la
funcionalitat. GISCE-ERP_QS s’adapta al lo que indica la "_ORDEN ECO
/797/2002_", no només per al càlcul dels índex sinó també per l’adaptació als
valors admissibles de TIEPI i NIEPI que es van actualitzant pels diferents Reals
Decrets que es promulguen.

## Fiabilitat

Es la capacitat del producte software per mantenir un nivell especificat de
prestacions quan s’utilitza sota condicions especificades.

### Maduresa

Es la capacitat del producte software per evitar fallar com resultat de
errades en el software.

### Tolerància a errades

Es la capacitat del producte software per mantenir un nivell especificat de
prestacions en cas d’errades de software o de infringir els seus interfases
especificats. El nivell especificat de prestacions inclou també la capacitat
de seguretat davant d’errades.

### Capacitat de recuperació

Es la capacitat del producte software per restablir un nivell de prestacions
especificat i de recuperar les dades directament afectades es cas d’errada.
Es comprovarà despres d’una errada

### Acompliment de la fiabilitat

Es la capacitat del producte software per adherir-se a normes, convencions o
legislació relacionades amb la fiabilitat.

## Usabilitat

Es la capacitat del producte software per esser entès, après, usat i ser
atractiu per a l’usuari, quan s’utilitza en les condicions especificades.

### Capacitat per ser après

Es la capacitat del producte software que permet a l’usuari aprendre sobre la
seva aplicació.

### Capacitat per ser operat

Es la capacitat del producte software que permet a l’usuari operar-lo i
controlar-lo. El programa no permet adequacions particulars per part de
l’usuari, ja que les seves funcionalitats venen definides per la “_ORDEN ECO
/797/2002_” i no permet fer-li modificacions o personalitzacions ja que no
són necessàries.

### Capacitat d’atracció

Es la capacitat del producte software per a ser atractiu a l’usuari.

### Acompliment de la  usabilitat

Es la capacitat del producte software per adherir-se a normes, convencions,
guies d’estil o legislació relacionades amb la usabilitat.

## Eficiència

Es la capacitat del producte software per proporcionar prestacions apropiades,
relatives a la quantitat de recursos usats, sota condicions determinades.

Es poden considerar recursos altres productes de software, la configuració del
software i el hardware del sistema.

### Comportament temporal

Es la capacitat del producte software per proporcionar temps de resposta,
temps de procés i potencia apropiats, sota condicions determinades

### Utilització de recursos

Es la capacitat del producte software per usar les quantitats i tipus de
recursos adequats quan el software realitza la seva funció sota condicions
determinades. S’hi inclouen els recursos humans.

### Acompliment de la eficiència

Es la capacitat del producte software per adherir-se a normes, convencions
relacionades amb la eficiència.

## Mantenibilitat

La capacitat del producte software per ser modificat. Les modificacions podrien
incloure correccions, millores o adaptació del software a canvis en l’entorn,
i requisits i especificacions funcionals.

### Capacitat per ser analitzat

Defineix la capacitat del producte software per diagnosticar-li deficiències o
causes dels errors en el software, o per identificar les parts que ha de ser
modificades.

### Capacitat per ser canviat

Es la capacitat del producte software que permet que una determinada modificació
sigui implementada.

Les modificacions només les implanta el servei tècnic de GISCE.

### Estabilitat

Es la capacitat del producte software per evitar efectes inesperats deguts a
modificacions del software.

### Capacitat per ser provat

Es la capacitat del producte software que permet que  el software modificat
sigui validat.

### Acompliment de la mantenibilitat

Es la capacitat del producte software per adherir-se a normes o convencions
relacionades amb la mantenibilitat.

## Portabilitat

Es la capacitat del producte software per ser transferit d’un entorn a un altre.
L’entorn pot ser organitzatiu de hardware i software.

### Adaptabilitat

La capacitat del producte software per ser adaptat a diferents entorns
especificats, sense aplicar accions o mecanismes diferents dels proporcionat
per aquest propòsit pel propi software considerat.

### Instalabilitat

Es la capacidad del producto software para ser instalado en un entorno
especificado. Las diferentes actualizaciones del módulo GISCE-ERP_QS se
realizan con el sistema de actualizaciones de GISCE-ERP, siendo un módulo
más integrado en el ERP.

### Coexistència

Es la capacitat del producte software per coexistir amb un altre software
independent, en un entorn comú, compartint recursos comuns.

### Capacitat per reemplaçar

Es la capacitat del producte software per ser usat en lloc d’un altre
producte software, pel mateix propòsit, en el mateix entorn.

### Acompliment de la portabilitat

Es la capacitat del producte software per adherir-se a normes o convencions
relacionades amb la portabilitat.
