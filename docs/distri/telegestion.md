# Documentació del mòdul de comptadors i lectures de telegestió

## Glosari
**PUNT FRONTERA**: Punt on acaba la xarxa de distribució i comença una altra xarxa: de transport, de subministrament, etc.

**REGISTRADOR**: Equip de mesura que permet calcular el consum d'energia i potència, així com l'energia bolcada a xarxa. Es col·loquen a qualsevol punt frontera: repetidors, generadors, punts frontera de xarxa de distribució, etc.

**COMPTADOR**: Registrador que està en un punt frontera d’un subministrament i, per tant, sempre està vinculat a un contracte d’electricitat.

**CONCENTRADOR**: Dispositiu de xarxa que permet comunicar-se amb un registrador de telegestió des d'un lloc remot per recollir dades o donar ordres.

**CT**: Centre de transformació, que passa l'electricitat d'alta tensió a mitja o baixa tensió.

**PRIME**: Protocol que fan servir els concentradors i els registradors per a comunicar-se entre ells a través del cablejat elèctric.

## Comptadors de telegestió

El modul de telegestió gestiona la lectura dels fitxers de tancament diaris i
mensuals de comptadors PRIME, la seva validació i posterior inserció de les
lectures de facturació.

Les lectures que es recullen de telegestió es troben separades de les de
facturació. Només es carregaràn a facturació les lectures necessàries.

### Pestanya General

![](_static/telegestion/ComptadorTGGeneral.png)

Amb el módul de telegestió, s'afegeixen els següents camps a l'apartat `TG info`:

* **TG Comptador**: Si aquest camp està marcat, inidica que l'equip és
  telegestionat. Es marca automàticament quan es validen lectures d'aquest
  comptador.
* **Connectat**: Indica si l'equip està connectat al concentrador i està
  preparat per enviar informació. (Només lectura)
* **Mostrar TG**: Botó que ens permet mostrar el llistat de les lectures de
  telegestió rebudes per el comptador. No són les de facturació.
* **Lectura des de TG**: Aquest botó permet crear una lectura de facturació a
  partir de les lectures validades de telegestió que s'hagin obtingut. Es
  demana la data en la qual es vol generar la lectura. Si d'aquest dia no n'hi
  ha cap de vàlida, anirà buscant lectures en dies **anteriors** fins a trobar
  una lectura de telegestió vàlida o una lectura de facturació. En aquest
  darrer cas, voldrà dir que no tenim cap lectura de telegestió vàlida més
  nova.

!!! Info "Nota"
    El nom del producte del comptador de telegestió és important. Per facilitar
    el switching va bé que la marca i el model estiguin separats per un espai

!!! Info "Nota"
    Els productes comptadors de telegestió han de tenir un prefix al camp Codi.
    Aquest prefix ha de ser el mateix que afegeix el comptador als números de
    sèrie. (veure `nota prefix`_ )

**Fitxa producte d'un comptador de telegestió**

![](_static/telegestion/FitxaProducteComptadorTG.png)

### Pestanya Telegestió

![](_static/telegestion/ComptadorTGTelegestio.png)

El mòdul de telegestió afegeix opcions a la fitxa de comptadors, inclosa una
nova pestanya Telegestió. Aquesta pestanya només es mostra en aquells
comptadors que tenen l'opció `TG Comptador` marcada.

![](_static/telegestion/grupo_TG_info.png)

* **ICP actiu**: Si la casella està activada, indica que l'ICP de l'equip de
  mesura està activat. Si s'activa apareixeran 2 camps més a l'apartat de
  `Control de potència`

  * **Potència programada**: Potència màxima que permet l'ICP del comptador
  * **Intensitat**: Indica la intensitat máxima a la qual està programat el
    ICP. Aquest es llegeix automàticament del comptador (Només lectura)

* **Darrera lectura**: Data de la última lectura de telegestió validada per
  aquest comptador
* **Concentrador**: Concentrador al qual està assignat aquest comptador. Un
  comptador s'assigna a un concentrador en el moment que se li validen lectures
  enviades des d'aquest concentrador.
* **Mostrar events TG**: Aquest botó ens obrirà un llistat dels esdeveniments
  del comptador.
* **Excepcions de validació**: En aquesta llista es poden afegis les excepcions
  de validació que no es tindran en compte. Al validar una lectura de
  telegestió, es poden generar un seguit d'excepcions que provocarà que la
  lectura no sigui vàlida. Si l'excepció és dins la llista, no es tindrà en
  compte i validarà la lectura. Podem veure la llista de les
  [possibles excepcions](#configuracio-excepcions)

![](_static/telegestion/pestanya_telegestion.png)

## Concentradors de telegestió

El mòdul de telegestió afegeix al sistema els concentradors de dades de telegestió.
Són els concentradors instal·lats a la xarxa elèctrica. Es donen d'alta
automàticament quan es llegeix el primer fitxer enviat per ells i s'associen als
comptadors instal·lats de forma automàtica.

En el llistat de concentradors es pot veure el número de comptadors que gestiona
cadasacun i el tipus de connexió a internet que utilitza cada concentrador.

![](_static/telegestion/ConcentratorListView.png)

La fitxa del concentrador s'omple quan arriba un fitxer amb forma S12. Des de
la fitxa també es pot accedir al llistat de comptadors associats a ell
mitjançant el botó comptadors.

![](_static/telegestion/ConcentratorMetersButton.png)

### Camps de connectivitat

Per els concentradors connectats mitjançant Mòdem existeix la pestanya **Modem 3G**
on es troben diferents camps d'informació del Mòdem. És important tenir configurat
el camp `Modem IP` que és on es guarda l'adreça de connexió al concentrador.

![](_static/telegestion/ConcentratorModemTab.png)

Si tenim configurat aquest camp correctament, els camps que indiquen les adreces
de connexió al portal web del concentrador i als serveis web s'ompliran.
El camp WEB de la part superior de la vista disposa d'un botó en forma de fletxa
que ens obrirà el navegador i ens portarà directament al portal web del concentrador.

![](_static/telegestion/ConcentratorGeneralTab.png)

## Procediment de càrrega de lectures

La gestió de lectures de consum de comptadors mitjançant telegestió es realitza
habitualment seguint tres passos:

1.  **Càrrega de dades**: Els concentradors deixen les dades de lectures,
    corbes i esdeveniments en un servidor FTP en format XML. GISCE-ERP recull
    aquests fitxers, els processa i els carrega a la base de dades. Aquesta
    operació la podem realitzar manualment des de la configuracio dels FTP
    prement el [boto de connexió ftp](#configuracio-connexions-ftp). Si es
    produeix un error, es registra al
    [llistat d'errors de lectura](#registre-de-lectura-tg-reader-errors)

2.  **Validació de lectures**: Per preparar les lectures abans d'ésser passades
    a la facturació, cal validar-les. Per fer-ho podem anar a l'opció del menú
    [Validar Tancaments](#validar-tg-tancaments) o fer-ho des d'un comptador
    en concret. Si hi ha algun error es genera un cas en el CRM,
    secció [Telegestió i CRM](#telegestio-i-crm)

3.  **Lectura TG**: Per poder facturar, necessitem carregar les lectures al
    sistema de facturació, igual que si ho haguéssim llegit manualment o amb
    TPL. Per fer-ho anem al comptador en qüestió i premem al botó de lectures de
    la fitxa o directament des del botó
    [Lectura des de TG](#lectura-des-de-tg-boto). Per entrar totes les lectures
    de tots els comptadors d'un lot de facturació podem prémer en el botó
    [importar lectures del lot](#importar-lectures-des-del-lot-de-facturacio).

!!! Info "Nota"
    Es pot configurar el sistema de telegestió per no carregar les lectures de
    reactiva i així no facturar-la. No obstant, si la potència contractada és
    superior a 15 kW, s'insertaran **sempre** les lectures de reactiva.

blockdiag {
    ftp -> carga -> validación -> lectura
    carga -> "TG Errores de lectura" [label = "errores", textcolor="#FF0000"]
    validación -> "CRM (Telegestión)" [label = "errores", textcolor="#FF0000"]
}

Actualment, GISCE-ERP és capaç de llegir els següents fitxers XML
estandaritzats:

* **S02**: Perfils
* **S04**: Tancaments mensuals
* **S05**: Tancaments diaris
* **S09**: Esdeveniments de comptador
* **S12**: Configuració del concentrador
* **S13**: Esdeveniments de comptador espontanis

## Gestió i configuració de Telegestió

Tots els menús d'accés a telegestió es troben centralitzats dins el menú
infraestructura.

![](_static/telegestion/MenuInfraestructuraTG.png)

### Configuració de la càrrega reactiva

Hi ha dos maneres de configurar com volem la càrrega reactiva:

Configuració individualitzada per polissa (prioritaria):

 - **Generar sempre la càrrega reactiva (always):** sempre generarem càrrega reactiva.
 - **Càrrega reactiva sempre 0 (zero):** la càrrega reactiva sera sempre 0
 excepte per potències superiors a 15 KW.
 - **Sense càrrega reactiva (never):** No generarà càrrega reactiva excepte per potències superiors a 15 KW.
 - **Ús de la variable de configuració (Per defecte):** fara ús de la variable de
 configuració `tg_reactive_insert`.

![](_static/telegestion/Reactive_charge_field_conf.png)

Configuració per variable global (es fara servir per les polisses no
  configurades):

 - **always:** sempre generarem càrrega reactiva.
 - **zero:** Generarà càrrega reactiva 0 excepte si te una potència contrectada
  superior a 15 KW.
 - **never:** No generarà càrrega reactiva excepte si te una potència contrectada
  superior a 15 KW.

![](_static/telegestion/tg_reactive_insert_var.png)

### Configuració > Connexions FTP

Els concentradors de telegestió deixen les dades en format XML en un servidor
FTP. GISCE-ERP accedeix a aquest FTP per accedir a les dades i importar-les.
Des d'aquesta opció de menú podem gestionar més d'un FTP.

GISCE-ERP mai esborra els fitxers importats, només els mourà per evitar
tornar-los a carregar.

![](_static/telegestion/FitxaFTPTG.png)

* **Descripció**: Descripció de l'FTP
* **Codi**: Codi de l'FTP per si es volen tenir codificats
* **Direcció IP**: Direcció IP del servidor FTP des del servidor ERP
* **Directori Arrel**: Directori en el qual es crearan les carpetes amb els
  fitxers ja processats.
* **Accés anònim**: Si el servidor s'accedeix amb l'usuari anònim
* **Usuari i Clau**: Usuari i clau d'accés al servidor FTP. Ha de permetre
  llegir, escriure i crear carpetes
* **Directori(s) Lectura**: Directori o directoris en els quals es buscaran
  fitxers per carregar, Els directoris han d'anar separats per punt i coma (;).
* **Llegir fitxers (Botó)**: Mitjançant aquest botó, es provoca una lectura
  dels fitxers de l'FTP. Carregarà tots els fitxers que trobi i inserirà les
  lectures i errors que vagi trobant. Si un fitxer no el processa, podrem veure
  l'error corresponent al registre de lectura.

!!! Tip "Consell"
    Els directoris han de començar i acabar sempre amb la barra de directori
    ("/"), p.e. **/root/upload/**
!!! Tip "Consell"
    Els caracters ``,``, ``*``, ``?``, ``<``, ``>``, ``:``, ``\``, ``'``, ``"``
    i ``|`` no estan permesos en el nom d'un directori

El procediment de lectura va de la següent forma:

* Els concentradors han de deixar els fitxers a les carpetes de l'FTP
  configurades a ``Directori Lectura`` per a que GISCE-ERP els trobi.
* Tots els fitxers que processi, els mourà a la carpeta configurada a
  ``Directori Arrel`` del propi FTP dins una carpeta amb el nom ``YYYYMM`` on
  YYYY és l'any i ``MM`` el mes de la data del fitxer importat.
* Els fitxers que no pugui importar **no** els mourà. Si ningú els treu,
  donaran error el següent cop que es llegeixin

### Configuració d'excepcions

**Configuració > Excepcions**

Quan es validen les lectures es fan tot un seguit de comprovacions per
assegurar-se que les lectures són correctes. En alguns casos, es vol que certes
validacions no es facin perquè es sap a priori que un comptador en concret té
alguna particularitat. P.e. Alguns comptadors poden tenir el totalitzador (P0)
malament perquè es tenen en compte períodes que per la tarifa actual no
s'utilitzen. En aquest cas sempre donarà error de totalitzador, però podem
marcar-lo per a què no tingui en compte aquesta validació i validarà
correctament.

Les excepcions que es gestionen actualment són:

* **(OL) Over Limit**: Consum excessiu. En una lectura *diària* s'ha consumit
  més que si s'hagués consumit la potència contractada durant 24 hores
  seguides.
* **(NR) Negative Read**: Lectura negativa.
* **(EE) Export Energy**: Exportació d'energia. Les lectures indiquen que
  aquest comptador està exportant energia. Es pot donar si el comptador ha
  estat instal·lat amb la polaritat invertida.
* **(ER) Export reactive**: Exportació de reactiva. Les lectures indiquen que
  aquest comptador està generant reactiva en els quadrants 2 i 3
* **(NC) No Communication**: No hi ha comunicació amb el comptador. Fa més de 2
  dies que no tenim lectura d'aquest comptador.
* **(BT) Bad Totalizer**: Totalitzador incorrecte. El període ``P0``
  (totalitzador) no és la suma dels altres períodes.
* **(CC) Comparison Month vs Day**: La lectura mensual absoluta no coincideix
  amb la lectura diaria del mateix dia.

!!! Tip "Consell"
    L'excepció **(NC) No Communication** depèn del paràmetre de configuració
    **tg_last_read_advice** que per defecte és de 2 dies. Es pot configurar per
    a què utilitzi un altre període.

**Configuració > Excepcions Comptador**

En el llistat **Configuració>Excepcions Comptador** podem indicar els
comptadors que validen sempre les seves lectures, encara que tinguin errors.
Això ens serveix per comptadors de proves, comptadors no associats a cap
polissa, comptadors de supervisió, comptadors no donats d'alta a l'ERP, etc...

* **Nº de Sèrie**: Número de sèrie del comptador tal com el veu el concentrador
  (amb prefix)
* **Notes**: Ens permet posar una nota explicativa amb la raó de la seva
  inclussió en aquesta llista

### Configuració > TG Categories Error i Configuració > Errors

Els concentradors de telegestió inclouen en els fitxers XML els errors que
troben al comunicar-se amb els comptadors i relacionats amb la seva própia
operació. Aquests errors estandaritzats es classifiquen amb codis de categoria
i codis d'error.

GISCE-ERP només emmagatzema els errors que estan donats d'alta en aquestes
taules. Si el fitxer XML conté un error que no està donat d'alta, no es
registrarà.

Aquestes taules les gestiona el propi ERP. Els futurs errors que apareguin en
la norma s'aniran afegint en aquestes llistes en properes actualitzacions.

* **Codi**: Codi numèric de l'error.
* **Descripció**: Descripció de l'error.
* **Categoria**: Si es tracta d'un error, a quina categoria pertany.

!!! Info "Nota"
    Aquests errors són específics del concentrador i no estan relacionats amb
    l'ERP. S'ha de tenir en compte que l'error es genera en el moment de generar
    el fitxer. Es podria donar el cas que el problema ja estigui solucionat
    actualment. Consulti el manual de l'equipament o contacti amb el fabricant.

### Casos Telegestió

Permet un accés directe als casos generats pel sistema de telegestió (veure
[Telegestió i CRM](telegestion.md#telegestio-i-crm)). Replica la mateixa
estructura dels casos del CRM , creant accessos directes als casos oberts i
als casos propis per facilitar-ne la gestió.

## Registre de lectura

En el registre de lectures dels fitxers es mostren els fitxers que s'han intentat
carregar i ens informa del resultat de la lectura. Si s'ha llegit correctament
tot el fitxer, si s'ha llegit parcialment amb algun error o si ha sigut totalment
erroni.

Els fitxers erronis poden ser fitxers en un format no soportat o directoris
a l'arrel del nostre FTP.
Els fitxers que tenen l'estat d'error parcial és perquè contenen valors
incorrectes en un o més camps. En aquest cas s'ignoren els grups
d'informació amb errors i es llegeix la resta.

![](_static/telegestion/partial_file_readings.png)

Si entrem a veure l'error parcial que resulta de la càrrega del fitxer
trobarem quin model de informe és el que dòna l'error, a quin o quins comptadors
passa, el missatge d'error i la línia o línies conflictives del fitxer.

![](_static/telegestion/partial_reading_error_info.png)

**Registre de lectura > TG reader Errors**

Llista els errors de lectura trobats per comptador. Aquests errors venen del
propi fitxer enviat pel concentrador, p.e. comptador no trobat

## TG Cierres

Registre dels tancaments diaris i mensuals amb accessos directes a:

* **TG cierres totals**: Tancaments només del període P0 (totalitzadors)
* **TG cierres vàlids**: Només tancaments validats

Les lectures que encara no han estat validades es llisten de color **blau** i
les validades de color **negre**

!!! Info "Nota"
    El comptador de registres d'aquests llistats no s'actualitzen, ja que el
    càlcul d'aquest valor és molt lent. Per tant, encara que hi hagi milers de
    lectures, sempre sortirà com 1/80

![](_static/telegestion/CierresTG.png)

Des del llistat podem seleccionar un conjunt de lectures i marcar-les com a
vàlides o invàlides utilitzant el botó **Acció**. Se'ns obrirà seguidament un
formulari on es permet escollir validar o invalidar les lectures de telegestió.
Aquesta acció **NO realitza les comprovacions per validar lectures.**

!!! Warning "Atenció"
    Cal tenir molt present que aquest procediment **NO valida les lectures**,
    només en marca el registre horari com a vàlid o invàlid. És recomanable
    utilitzar aquest procediment en registres individuals i només pels casos de
    necessitat, dels quals es coneix el motiu. Per validar lectures cal
    utilitzar el mètode descrit en l'apartat:
    [Validar TG Tancaments](#validar-tg-tancaments).

**Formulari de validació d'un tancament**

![](_static/telegestion/MarcarTancamentValid.png)

Podem veure la informació completa en el **detall d'un tancament**:

![](_static/telegestion/FitxaCierreTG.png)

En el detall hi trobem:

* **Comptador**: Nom complet del comptador tal i com ens l'envia el
  concentrador.
* **Nom CnC**: Nom del concentrador al qual estava associat el comptador en el
  moment de realitzar la lectura. Pot canviar en el temps i així tenim
  traçabilitat.
* **Tipus**: Indica si el tancament és Mensual i Diari.
* **Valor**: **Absolut** (lectura del comptador) o **Incremental** (consum des
  de la última incremental generada). Les incrementals només poden ser de tipus
  mensual
* **Període**: Període al que correspon la lectura. 0 és un totalitzador del 1
  al 6.
* **Des de i A**: Interval temporal que comprèn la lectura
* **In**: Activa entrant, o energia importada
* **Out**: Activa sortint, o energia exportada
* **R1,R2,R3 i R4**: Els 4 quadrants de reactiva
* **Max**: Valor del maxímetre i data de registre del mateix (només per les
  mensuals)
* **Vàlid**: Si està validat i quan es va validar

!!! Info "Nota"
    Els números de sèrie dels comptadors a GISCE-ERP són numèrics. A telegestió,
    els números de sèrie en els concentradors afegeixen un prefix segons el
    producte. p.e. per comptadors ZIV afegeixen el prefix **ZIV**. Aquest
    prefix es pot configurar en la gestió de productes omplint el camp ``Codi``
    del producte associat al comptador de telegestió. (veure la [Fitxa producte
    d'un comptador de telegestió](#fitxa-producte-dun-comptador-de-telegestio))

## Lectura des de TG (Botó)

Ens permet importar les lectures de telegestió d'un comptador si en sabem el
número de sèrie. Funciona igual que si el cridéssim des de la fitxa del
comptador.

* **Comptador**: Nº de sèrie del comptador
* **Data límit**: Data de la qual volem les lectures
* **Forçar**: Entra la lectura encara que hi hagi una lectura posterior. Si no
  **no** deixa entrar la lectura

**Formulari per introduïr data de importació de lectura**

![](_static/telegestion/ImportarLecturesTG.png)

## Validar TG Tancaments

La **Validació** consisteix en:

* S'eliminen els períodes que s'utilitzaran (del 3 a 6 ambdos inclosos). Es fa
  així per facilitar el canvi entre tarifes DH i no DH
* Es comprova que la lectura sigui superior a la darrera vàlida rebuda. La
  primera lectura que es reb d'un comptador, es marca com a vàlida
  automàticament.
* Es comprova que el consum entre dues lectures no sigui superior al màxim
  teòric (potència * 24 * dies entre lectures)
* Es comprova que el comptador no estigui exportant energia (es pot haver
  connectat al revés)
* Es comprova que no es generi reactiva en els quadrants 2 i 3
* Es comprova que la lectura no estigui duplicada (es molt normal que pasi). Si
  ja tenim una lectura del mateix dia, del mateix període i del mateix tipus i
  valor, es comprova que la lectura sigui la mateixa (amb un error de +/- 1).
  Si és així, s'elimina directament, si no, es genera un avís
* Es comprova que la lectura no sigui negativa
* Un cop validades totes les lectures, es comprova que el període P0
  (*totalitzador*) sigui realment la suma de tots els altres períodes i que el
  marge d'error no sigui superior al número de períodes.
* Un cop validades totes les lectures, es comprova que les lectures mensuals
  coincidesquin amb les lectures diaries absolutes corresponents al mateix dia
  de tancament.
* Opcionalment es poden validar el valors de reactiva per fer comprovacions de
  **cosinus fi**

El procediment per validar les lectures és a través del wizard que es troba en
**Infraestructura > Validar Cierres TG**.

![](_static/telegestion/BotoValidacio.png)

Podem validar les lectures amb aquest botó. Si no entrem cap número de
comptador, es validaran **totes** les lectures pendents de validar.

* **Comptador**: Nº de sèrie del comptador del qual en volem validar les
  lectures

![](_static/telegestion/ValidarTancamentsBotoTG.png)

## Importar lectures des del Lot de Facturació

En comptes d'haver d'anar comptador per comptador per carregar les lectures,
podem fer una càrrega massiva de tots els comptadors d'un lot de facturació.
Per això hem d'anar al lot mentre està en estat **esborrany** i prèmer el botó
**Crear lectures TG**. En aquest cas no ens demana la data de la lectura, ja
que agafarà la data de l'**últim dia del període del lot** de facturació.

Es crearà un procés en background que anirà carregant les lectures dels
comptadors que siguin de telegestió.

![](_static/telegestion/LotImportarLectures.png)

!!! Info "Nota"
    Quan s'importen les lectures d'un comptador de telegestió, s'agafa la
    lectura validada del dia que es demana o la de l'anterior més proper que en
    tingui. Per tant es pot donar el cas que les lectures no siguin del dia de
    final de lot. En aquesta cas, es facturarà la energia fins aquest dia i la
    resta, p.e la potència, pel període complet.

## Telegestió i CRM

Tots els errors i validacions manuals que s'hagin de fer estan integrades en el
**CRM** de forma que es pugui fer un seguiment de les passes que s'han anat
fent. D'aquesta forma evitem generar ordres de treball paral·leles en el cas
d'haver de, per exemple, arribar a realitzar un canvi de comptador per part del
departament tècnic.

El cas s'assigna automàticament a l'usuari que ha realitzat la acció que ha
provocat el cas.

Per accedir als casos que s'han generat deguts a telegestió podem accedir al
menú del CRM com qualsevol altre cas i seleccionar la secció **Telegestió (TG)**
: **CRM & SRM > All Cases > Casos per secció**

També hi podem accedir des del menú de telegestió, on a l'apartat
corresponent ja tenim els casos filtrats per la secció de telegestió:
**Infraestructura > Telegestió > Casos Telegestió**

Els casos de telegestió tenen tots dues referències per donar un accés ràpid a
les dades. Aquestes referències les trobem a solapa **Informació extra**

![](_static/telegestion/crm_cas_obert_referencies.png)

La primera referència es per accedir a la pòlissa i la referència 2 per accedir
al contador associat al cas. Si cliquem sobre la carpeta ens obrirà la
referència pertinent.

Per posar un exemple d'ús de les referències, el següent punt explica [com anar
a les lectures d'un comptador des d'un cas](telegestion.md#lectures-dun-comptador-des-dun-cas)

**Lectures d'un comptador des d'un cas**

Per anar a les lectures d'un contador a partir d'un cas en concret, primer hem
d'escollir el cas , obrir-lo i anar a la pestanya de **Informació extra**.
Després cliquem sobre la carpeta de la referència 2.

![](_static/telegestion/crm_exemple_contador_obrir_carpeta.png)

Ens apareix una nova finestra amb les dades del comptador.

![](_static/telegestion/crm_pantalla_contador_sola.png)

Ara cliquem sobre **Mostrar en TG**

![](_static/telegestion/crm_pantalla_contador.png)

Preguntarà de quin comptador volem visualitzar les lectures.

![](_static/telegestion/crm_contador_seleccionado.png)

Ens obrirà una nova pestanya al ERP amb les lectures de fons i ja podem
tancar la finestra actual del contador.

![](_static/telegestion/crm_lectura_contador.png)

## Automatització de tasques

S'han creat dues tasques planificades **Administració > Configuració >
Planificació > Accions planificades** per ajudar a la telegestió.

**TG Reader scheduler**

Aquesta planificació importa cada dia les lectures de l'FTP.

**TG Validate scheduler**

Permet programar la validació automàtica de totes les lectures.

## Corbes de Carrega Horaries (CCH)

Les corbes de càrrega horàries cal entregar-les a l'operador del sistema i a la
comercialitzadora o client directe a mercat. Es fa mitjançant els següents fitxers:

**Fitxers**

| Fitxer                     | Entrega                                        |
|----------------------------|------------------------------------------------|
| P5D                        | Setmanalment                                   |
| F5D                        | Mensualment                                    |


### Fitxers P5D

Les corbes de càrrega horàries validades (CCH_VAL) cal entregar-les com a
màxim **setmanalment** amb els fitxers P5D.
L'ERP realitza un enviament diari.

**Generació dels fitxers P5D de forma manual**

L'assistent per generar els fitxers P5D de forma manual es troba al menú
`Infraestructura > Telegestió > Exportar CCH_VAL (P5D)`.

![](_static/telegestion/MenuWizardExportarP5D.png)

![](_static/telegestion/wizardExportP5D.png)

### Fitxers F5D

Les corbes de càrrega horàries facturades (CCH_FACT) cal entregar-les com a
màxim el dia **7 del mes següent** amb els fitxers F5D.

Els Fitxers F5D no poden tenir forats, i no s'envien fins que estan tots els
CCH_FACT disponibles. El procés per generar totes les corbes i omplir els
forats s'executa automàticament un cop s'ha tancat el lot de facturació. Amb
això es creen tots els registres CCH_FACT necessaris en segon pla. Una vegada
disposem de totes aquestes dades, el procés automatitzat que s'executa durant
la nit generarà els fitxers F5D i en el cas que hi hagi servidor FTP
configurat a l'ERP també els pujarà.

Si per algun motiu la generació dels fitxers no funciona, es crearà un cas amb
informació a `Infraestructura > Telegestió > Casos Telegestió > Tots els casos`.

![](_static/telegestion/CasGeneracioF5D.png)

Per aquest tipus de situacions, es pot generar i enviar els F5D, de la següent
forma:

**Generació i enviament dels fitxers F5D de forma manual**

L'assistent per generar els fitxers F5D de forma manual es troba al menú
`Facturació > General > Lots de facturació`. Dins d'un lot de facturació:
`Exportar Fitxer Corbes del Lot`.

![](_static/telegestion/MenuLotsdeFacturacio.png)

![](_static/telegestion/BotoWizardExportarF5D.png)

Primer de tot, ens ofereix l'opció de sobreescriure els fitxers F5D si ja
existeixen, molt útil si tenim fitxers incorrectes. La segona opció indica
si volem que els fitxers que es generin es pugin o no al servidor FTP, tal
com es mostra a la següent imatge. Per últim l'opció de marcar l'última
corba és per guardar fins quina data s'han creat els fitxers F5D per cada
comptador, d'aquesta manera quan es tornin a generar seguiran des de la
data on s'havia arribat.

![](_static/telegestion/ExportarFitxerCorbesLot.png)

!!! Info "Nota"
    Es poden configurar servidors SFTP per tal de pujar-hi automàticament els
    fitxers F5D i P5D.

### Estat de pujada dels fitxers P5D i F5D

Per comprovar l'estat de l'enviament d'aquests fitxers es pot accedir des de
`Infraestructura > Telegestió > SFTP Estat de pujada`.

![](_static/telegestion/MenuEstatPujadaSFTP.png)

![](_static/telegestion/LlistaEstatPujadaFitxers.png)

Es pot forçar l'enviament manual dels fitxers tant P5D com F5D.

### Variables de configuració

Existeixen diverses variables de configuració per tal de personalitzar el
comportament de les corbes de càrrega horàries. Per accedir al menú que
permet modificar-les, cal anar a: `Administració > Configuració > Propietats`

![](_static/telegestion/VariablesConfiguracio.png)

* **change_to_remote_managed_with_cch_deadline_working_days**: Canvia el termini
  màxim de dies laborables dels que es disposa per poder entregar les CCH.

* **tg_max_days_back**: S'utilitza per els contractes que no són operatius amb CCH.
  Indica la màxima quantitat de dies que serà possible retrocedir quan es creïn
  noves lectures. En els contractes operatius amb CCH aquest valor és fixe i només
  permet tres dies de retrocés.

* **tg_f5d_create_zip_file**: Crea un fitxer zip amb tots els F5D.

* **tg_f5d_last_day**: Marge de temps en dies, en el que superat, si no s'han generat
  els F5D es crearà un cas de telegestió amb aquest avís per tal de notificar l'usuari.

* **tg_cch_fact_invoice_length**: Si es té activat utilitza les dates inici i final
  de les factures per realitzar la generació dels F5D.

  Valor                      | Descripció
  ---------------------------|------------------------------------
  tg_f5d_create_zip_file     | `1` crea el zip, `0` no crea el zip
  tg_cch_fact_invoice_length | `1` activat, `0` desactivat

## Sistema de tele gestió

### Tipus de peticions

Existeixen dos tipus de peticions diferents, les síncrones i les asíncrones.

**Síncrones**

Els dispositius que reben una petició síncrona la responen el més aviat possible omplint
l’informe amb les dades que estiguin disponibles en el moment. Per aquest motiu, si la
petició es procesa correctament, es rep la resposta en poc temps. Un cop rebuda la resposta
es podrà visualitzar des del mateix assistent.

A la següent imatge podem veure l'assistent un cop s'ha demanat un informe síncron i se n'ha
rebut la resposta. Tenim l'opció d'obrir el fitxer directament per veure'n el contingut o
desar-l'ho.

![](_static/telegestion/stg_peticions_sincrona.png)

**Asíncrones**

Les peticions asíncrones treballen de manera diferent i són les més fiables quan el nostre
objectiu és obtenir dades útils i vàlides. Com bé indica el seu nom aquestes peticions no
responen immediatament amb la informació requerida sino que envien una confirmació per
informar que s'ha rebut la petició. Un cop arribats a aquest punt el concentrador al qual
s'ha fet la petició es posarà a treballar per recollir tota la informació necessària dels
comptadors que té connectats. Quan el concentrador hagi generat l'informe més complet que
l'hi hagi sigut possible l'enviarà directament al servidor FTP per tal que sigui llegit.

### Informes disponibles

Actualment el sistema de tele gestió suporta els següents informes:

* **Instant data (S01)**: És un informe que s’ha de demanar de manera síncrona a un comptador.
    Conté la informació sobre la lectura instantània actual d’aquest.
* **Meter events (S09)**: Conté els esdeveniments dels comptadors.
* **Meter parameters (S06)**: Conté els paràmetres de dels comptadors.
* **Concentrator parameters (S12)**: Conté els paràmetres del concentrador.
* **Daily absolute (S05)**: Conté els tancaments diaris.
* **Monthly billing (S04)**: Conté els tancaments mensuals.
* **Daily incremental (S02)**: Conté les corbes horàries.

### Camps de la petició

1. **Identificador del dispositiu**: Mostra el nom del comptador o concentrador al qual es farà
la petició.
2. **Informe**: Llista on es pot seleccionar quin dels informes llistats a l'apartat anterior
[Informes disponibles](#informes-disponibles) es vol demanar al dispositiu.
3. **Dates**: Delimiten el període de temps del qual volem rebre la informació.
4. **Font**: Llista per seleccionar l'origen del qual volem que s'extreguin les dades.
5. **Info**: Text informatiu sobre l'estat de la petició.

![](_static/telegestion/stg_assistent_camps.png)

Per el camp **Font** existeixen tres opcions diferents:

* **DC Condicional**: Intenta obtenir la informació directament de la base de dades del
concentrador i si no la troba consulta al comptador.
* **DC Force**: Retornarà solament la informació disponible a la base de dades del concentrador
la qual cosa la converteix en la font més ràpida.
* **Meter Force**: Força la obtenció de tota la informació exclusivament dels comptadors.

![](_static/telegestion/stg_assistent_font_dades.png)

### Assistents

El sistema de tele gestió està format per diferents components els quals podem utilitzar des
de l’aplicació client de l’ERP.
Al moment d’encendre els diferents assistents, es realitza una consulta al STG per saber quins
informes són suportats i crear la llista des la qual es podrà seleccionar l’informe a enviar.

**Assistent de comptador**

S’accedeix a aquest assistent des de la vista d’un comptador concret o des de la llista de
comptadors. Ens serveix per fer peticions directament i concretament al comptador seleccionat.

![](_static/telegestion/stg_boto_assistent_comptador.png)

![](_static/telegestion/stg_assistent_comptador.png)

**Assistent d'un concentrador**

S’accedeix a aquest assistent des de la vista d’un concentrador concret o des de la llista de
concentradors. Ens serveix per fer peticions directament i concretament al concentrador
seleccionat.

![](_static/telegestion/stg_boto_assistent_concentrador.png)

![](_static/telegestion/stg_assistent_concentrador.png)

**Assistent de tots els concentradors**

S’accedeix a aquest assistent des de la llista de concentradors o des d’un concentrador concret.
Aquest assistent ens serveix per fer peticions massives a tots els concentradors de tele gestió
per aquesta raó, a diferència dels altres assistents aquest no indica el nom del dispositiu al
que es farà la petició.

![](_static/telegestion/stg_boto_assistent_tots_concentradors.png)

![](_static/telegestion/stg_assistent_tots_concentradors.png)

## Informe de disponibilitat de comptadors

Aquest informe posa a la nostra disposició la informació de connexió dels diferents comptadors
de telegestió del nostre sistema. Aquestes dades les aconseguim configurant els concentradors
perquè generin i enviïn un informe PRIME S24 cada hora el qual conté l'estat de la connexió de
tots els seus comptadors en el moment concret de la generació. Acumulant aquestes dades, l'ERP
és capaç de fer-ne un històric per processar-lo posteriorment.

Aquí podem veure un exemple de l'[**Informe**](_static/telegestion/ReportMetersAvailability.pdf) generat per cinc comptadors diferents.

**Contingut de l'informe**

!!! Nota "Nota"
    Per cada comptador que s'hagi seleccionat al generar l'informe es repeteixen els punts
    2, 3 i 4 de la següent llista.

1. Període de temps que abasta l'informe. S'indica amb les dates inicial i final a la part
superior de l'informe.

2. Nom de telegestió del comptador al qual correspon la taula següent.

3. Una taula de targetes de colors en la qual cada targeta fa referència a una hora concreta
d'un dia de la setmana.
    * Files: Cada fila representa un dia de la setmana. De dilluns fins diumenge.
    * Columnes: Cada columna és una hora del dia. L'hora 0 és les 12 de la nit.

4. Una llegenda indicant l'escala de colors utilitzada en les targetes de la taula. Cada color té
assignat un rang de valors. Aquests valors són la quantitat de connexions establertes correctament
per el comptador durant el període de temps que abasti l'informe.

    !!! Tip "Exemple"
        Si tenim un color amb el rang 0 fins a 10, les targetes que estiguin pintades d'aquest color
        indicaran una baixa disponibilitat del comptador durant l'hora corresponent. Concretament
        indica que el comptador només s'ha trobat connectat aquesta hora un màxim de 10 dies
        diferents dintre el període de temps que abasti l'informe.

![](_static/telegestion/ReportMetersAvailabilitySample.png)
