# Visor web
## Autentificació

 El primer que ens trobem al entrar es la pantalla d'autentificació

 ![](_static/login.png)

 Per accedir s'ha d'introduir el nostre usuari i contrasenya i prémer retorn o el boto de login. El usuari i la contrasenya es el mateix que per al ERP.

## Interfície

 ![](_static/interficie.png)

 La interfície es composa dels següents elements:

 1. Control de cerca
 2. Selector de capes
 3. Control de zoom
 4. Control d'ubicació
 5. Exportació
 6. Quadre de coordenades

### Control de cerca

 Esta situat a la parte superior esquerra i ens permet cercar elements al GIS.

### Selector de capes

 El selector de capes es l'eina que ens permet selecionar quines capes volem veure, al passar el per sobre el control o clicar sobre d'ell es mostrara un llistat de les capes disponibles.

 ![](_static/capes.png)

 En aquest control es poden diferenciar en dos tipus:

 - Cartografia:
    -  Només podem seelcionar una capa base a l'hora i aquest sera el fons per el nostre GIS, per exemple un mapa cartografic o ortofotografies.

 - Capes sobreposades:
    - Aquestes capes son les que podem sobreposar a la nostra capa base i en poem selecionar múltiples a l'hora.
#### Capes de telegestio

  Aquest grup de capes ens permet veure informacio sobre la telelgesio.

  - Amb CCH: Apareixen els comptadors amb el camp “TG Contador” actiu ,  “Conectado” actiu i “Póliza Telegestionada” “Operativa con CCH”
    - Envia lectures: Mostra tots els comptadors que la ultima lectura valida es de fa menys de tres dies
    - No comunica:Mostra tots els comptadors que la ultima lectura valida es de tres dies o més

  ![](_static/comptador_cch.png)

  - Sin CCH: Apareixen el comptadors amb el camp “TG Contador” actiu ,  “Conectado” actiu i “Póliza Telegestionada” “No operativa” o “Sin CCH”
    - Envia lectures: Mostra tots els comptadors que la ultima lectura valida es de fa menys de tres dies.
    - No comunica: Mostra tots els comptadors que la ultima lectura valida es de tres dies o més

  ![](_static/comptadors_no_cch.png)

  - Sense concentrador: Apareixen els comptadors amb el camp “TG Contador” actiu i “Conectado” desactivat

  ![](_static/comptador_no_concentrador.png)

  Camps de la bombolla:

  ![](_static/comptador_popup.png)

  - **Titol**: Numero de serie , marca i model
  - Ultima data de tancament valida
  - Nom del titular
  - Adreça del CUPS
  - Concentrador




### Control de zoom

 Aquest control ens permet escollir el zoom del GIS , aquest va des de nivell 0 (tot el mon)  25 (màxim detall).

 També podem canviar el nivel de zoom mitjançant el ratolí o en el cas d'usar dispositius tàctils amb el gest d'apmpliar/reduir.

### Control d'ubicació

 Aquest control permet situar el mapa a la nostra ubicació.

 ![](_static/permet_ubicacio.png)

 Un cop premem el boto el navegador ens demanara si volem permetre el GIS coneixer la nostra ubicació

 Seguidament podem veure la nostra ubicació. L'indicador mostrara el centre de la zona aproximada de l'ubicació i el cercle la zona aproximada.

 ![](_static/ubicacio.png)

### Exportació

  Control que permet exportar les dades del visor tot seleccionant el format del fitxer de sortida i les capes que s'hi han de representar.
  En l'assistent hi trobem les següents opcions de configuració:
  
  * Capes: S'utilitza per escollir les capes que es representaran en l'exportació.
  ![](_static/export_doc/capes.png)

  * Text: Amb aquest opció escollim si volem que es mostri o no text en l'exportació.
  ![](_static/export_doc/text.png)

  * Format del fitxer: Permet seleccionar el format del fitxer exportat.
  ![](_static/export_doc/format_fitxer.png)

  * Format de la pàgina: Permet escollir el format de la pàgina, que pot ser vertical (Retrat) o horitzontal (Apaisat).

  ![](_static/export_doc/format_pagina.png)

  * Nota: S'utilitza per afegir una nota al peu del document.
  ![](_static/export_doc/nota2.png)

  ![](_static/export_doc/nota.png)

  * Àrea: Ens permet seleccionar l'area exportada del visor. Per defecte és el centre de la vista actual del mapa, pero podem definir manualment l'àrea d'impresió amb un asistent. Per a la selecció manual s'ha de clicar "Seleccionar manualment".
  ![](_static/export_doc/area.png)

  ![](_static/export_doc/area2.png)



### Quadre de coordenades

 Aquest control esta situat a la cantonada inferior esquerra i ens permt verue les coordenades del punt on tenim el ratolí. També permet buscar una coordenada concreta, clicant sobre el control apareixerà un formulari per indicar la coordenada a bucar. Un Cop introduïda la coordenada prement retorn apereixerà un indicador de la situacio de la coordenada.

 ![](_static/coordenades.png)

## Simulacions

### Simulacions AT

1. Seleccionar un tram de AT. Això farà aparèixer en pantalla una targeta amb la informació del tram i del botó "Simula".
    ![](_static/sim_at/step_1.png)

2. Prémer "Simula". Això obrirà el llistat d'interruptors maniobrables **oberts** i en el mapa mostrara els interruptors oberts (vermell) i tancats (verd).
    ![](_static/sim_at/step_2.png)

    !!! Info "Nota"
        Si apareix el missatge "No hi ha nodes oberts" significa que no hi ha interruptors de AT oberts.

3. Si volem canviar l'estat d'un interruptor ho podem fer prement l'interruptor al mapa(1). També el podem modificar l'estat del interruptor en el llistat d'interruptors(2), en el cas que no estigui tancat el podem buscar(3).
    ![](_static/sim_at/step_3.png)

    !!! Info "Nota"
        A la capçalera del llistat d'interruptors podem veure el nombre d'interruptors oberts


4. Prémer el botó de "Simula" que haurà canviat a un simbol de "Play".
    ![](_static/sim_at/step_4.png)

    !!! Info "Nota"
        - Es dibuixaran els trams desconnectats en vermell i els connectats en verd.
        - En la part inferior de la targeta apareix el llistat de clients afectats.

5. Per sortir de la simulació podem tancar o prémer "ESC".
    ![](_static/sim_at/step_5.png)


### Simulacions BT

1. Seleccionar el CT que volem simular.
    ![](_static/sim_bt/step_1.png)

2. Prémer "Simula". Aixo obrirà el llistat d'interruptors maniobrables, també apareixeran els interruptors oberts(vermell) i tancats(verd) al mapa.
    ![](_static/sim_bt/step_2.png)

    !!! Info "Nota"
        Si apareix el missatge "No hi ha nodes oberts" significa que en aquest CT no hi ha interruptors oberts.

3. Si volem canviar l'estat d'un interruptor ho podem fer prement l'interruptor al mapa. També el podem modificar l'estat del interruptor en el llistat d'interruptors, en el cas que no estigui tancat el podem buscar.
    ![](_static/sim_bt/step_3.png)

4. Premer el botó de "Simula" que haura canviat a un simbol de "Play".
    ![](_static/sim_bt/step_4.png)

    !!! Info "Nota"
        - Es dibuixaran en vermell els trams desconnectats i els connectats en verd.
        - En la part interior de la targeta apareix el llistat de clients afectats.

5. Per sortir de la simulació podem tancar o prémer "ESC".
    ![](_static/sim_bt/step_5.png)

## Qualitat

### Qualitat AT

1. Fer una simulacio AT i en lloc de tancar-la convertir-la en una inicidencia de qualitat.

2. Seleccionar l'opció de qualitat en el llitat d'interruptors

    ![](_static/calidad_at/iniciar_qualitat.png)

3. Si es vol crear una incidència escollim "Crear incidència" en el llistat d'incidencies(1) i posem el nom de la incidència(2), en el cas que volguem afegir un interval a una incidència la selecionem en el llistat de incidències(1).

    ![](_static/calidad_at/crear_inc_at.png)

4. Seleccionar el origen de la incidència.

    ![](_static/calidad_at/origen.png)

5. Seleccionar el tipus d'incidència.

    ![](_static/calidad_at/tipus.png)

6. Seleccionar la causa de la incidència

    ![](_static/calidad_at/causa.png)

7. Assignar la data d'inici de la incidència (en format dia/mes/any hora:minuts:segons)

    ![](_static/calidad_at/inici.png)

8. Assignar la data de fi de la incidència (en format dia/mes/any hora:minuts:segons)

    ![](_static/calidad_at/fi.png)

9. Crear la la incidència. Un cop creada l'icona canviará a un "tick".

    ![](_static/calidad_at/crear.png)

!!! Info "Nota"
    Un cop creada la incidència la podem consultar al ERP a Qualitat/Traçabilitat/Incidències

### Qualitat BT

1. Fer una simulacio BT i en lloc de tancar-la convertir-la en una inicidencia de qualitat.

2. Seleccionar l'opcio de qualitat en el llitat d'interruptors

    ![](_static/calidad_at/iniciar_qualitat.png)

3. Si es vol crear una incidència escollim "Crear incidencia" en el llistat d'incidències(1) i posem el nom de la incidència(2), en el cas que volguem afegir un interval a una inicidencia la seleccionem en el llistat de incidències(1).

    ![](_static/calidad_bt/crear_inc_bt.png)

4. Seleccionar el origen de la incidència.

    ![](_static/calidad_at/origen.png)

5. Seleccionar el tipus d'incidència.

    ![](_static/calidad_bt/tipus.png)

6. Seleccionar la causa de la incidencia

    ![](_static/calidad_bt/tipus.png)

7. Assignar la data d'inici de la incidència (en format dia/mes/any hora:minuts:segons)

    ![](_static/calidad_bt/inici.png)

8. Assignar la data de fi de la incidència (en format dia/mes/any hora:minuts:segons)

    ![](_static/calidad_bt/fi.png)

9. Crear la la incidència

    ![](_static/calidad_bt/crear.png)

!!! Info "Nota"
    Un cop creada la incidència la podem consultar al ERP a Qualitat/Traçabilitat/Incidències

## Actualització de les dades

### Introducció

Per tal d'actualitzar les dades del visor web s'ha de seguir el següent procés:

![](_static/update/esquema_update.png)

### Procediment

1. Activar el mode actualització:

    Per activar el mode actualització hem d'anar a "GIS>Mode actualització de dades"

    ![](_static/update/wizard_mode_update.png)

    Un cop activat el mode actualització apareixerà un missatge al entrar al visor web avisant de que s'està realitzant una actualització de dades.

2. Preparar actualització:

    Aquest pas es opcional ja que la seva funció es fer que la carrega de les dades des del Autocad sigui mes rapida.
    L'assistent per preparar l'actualització es pot trobar a "GIS>Preparar actualització de dades".

    ![](_static/update/wizard_preparar.png)

3. Fer actualitzacio de dades amb el Autocad:

    Realitzar la actualització de dades mitjançant les eines de l'Autocad

4. Carregar shapes:

    La carrega de shapes dependrà de les capes que usem o que vulguem actualitzar. Les disponibles son les següents:

    * LAT i LBT
    * Cartografia
    * Rases
    * Cabines
    * Fibra òptica
    * Fora de servei
    * Defectes BT

    La carrega es pot realitzar mitjançant els assistents que es troben a "GIS>Carregadors".

    ![](_static/update/wizard_web.png)

    Aquests assistents ens obriran la pagina web per a la carrega dels fitxers.

    ![](_static/update/web_load.png)

    !!!Note "Format dels fitxers"
        Els fitxers només es poden carregar en format WINZIP

    Un cop carregat el fitxer ens apareixerà la seguent pagina informant-nos de que s'iniciara una tasca en segon pla:

    ![](_static/update/carrega_shapes_background.png)


5. Desactivar el mode actualització:

    Per desactivar el mode actualització hem d'anar a "GIS>Mode actualització de dades"

    ![](_static/update/wizard_mode_update.png)

    Quan es desactivi el mode actualització desapareixerà l'avís al visor web

!!!Note "En cas d'error"
    En cas d'algun error en el proces s'ha de repetir el pas
