# Autentificació

 El primer que ens trobem al entrar es la pantalla d'autentificació
 
 ![](_static/login.png)

 Per accedir s'ha d'introduir el nostre usuari i contrasenya i prémer retorn o el boto de login. El usuari i la contrasenya es el mateix que per al ERP.

# Interfície

 ![](_static/interficie.png)
 
 La interfície es composa dels següents elements:

 1. Control de cerca
 2. Selector de capes
 3. Control de zoom
 4. Control d'ubicació
 5. Exportació
 6. Quadre de coordenades
 
## Control de cerca
 
 Esta situat a la parte superior esquerra i ens permet cercar elements al GIS. 

## Selector de capes
 
 El selector de capes es l'eina que ens permet selecionar quines capes volem veure, al passar el per sobre el control o clicar sobre d'ell es mostrara un llistat de les capes disponibles.
 
 ![](_static/capes.png)
 
 En aquest control es poden diferenciar en dos tipus, capes de base (part superior del contol) i capes sobreposades(part inferior del control)
 
 - Capes base:
    -  Només podem seelcionar una capa base a l'hora i aquest sera el fons per el nostre GIS, per exemple un mapa cartografic o ortofotografies.

 - Capes sobreposades:
    - Aquestes capes son les que podem sobreposar a la nostra capa base i en poem selecionar múltiples a l'hora.

## Control de zoom
 
 Aquest control ens permet escollir el zoom del GIS , aquest va des de nivell 0 (tot el mon)  25 (màxim detall).
 
 També podem canviar el nivel de zoom mitjançant el ratolí o en el cas d'usar dispositius tàctils amb el gest d'apmpliar/reduir.

## Control d'ubicació
 
 Aquest control permet situar el mapa a la nostra ubicació.
 
 ![](_static/permet_ubicacio.png)
 
 Un cop premem el boto el navegador ens demanara si volem permetre el GIS coneixer la nostra ubicació
 
 Seguidament podem veure la nostra ubicació. L'indicador mostrara el centre de la zona aproximada de l'ubicació i el cercle la zona aproximada.
 
 ![](_static/ubicacio.png)

## Exportació
  
  Control que permet exportar dades del GIS a diferents formats 
 
## Quadre de coordenades

 Aquest control esta situat a la cantonada inferior esquerra i ens permt verue les coordenades del punt on tenim el ratolí. També permet buscar una coordenada concreta, clicant sobre el control apareixerà un formulari per indicar la coordenada a bucar. Un Cop introduïda la coordenada prement retorn apereixerà un indicador de la situacio de la coordenada.
  
 ![](_static/coordenades.png)

# Simulacions

## Simulacions AT

1. Seleccionar un tram de AT. Això farà apareixer en pantalla una targeta amb la informació del tram i del botó "Simula".
    ![](_static/sim_at/step_1.png)
 
2. Premer "Simula". Això obrirà el llistat d'interruptors maniobrables **oberts** i en el mapa mostrara els interruptors oberts (vermell) i tancats (verd).
    ![](_static/sim_at/step_2.png)
    
    !!! note
        Si apareix el missatge "No hi ha nodes oberts" significa que no hi ha interruptors de AT oberts.
 
3. Si volem canviar l'estat d'un interruptor ho podem fer prement l'interruptor al mapa(1). Tambè el podem modificar l'estat del interruptor en el llistat d'interruptors(2), en el cas que no estigui tancat el podem buscar(3).
    ![](_static/sim_at/step_3.png)
    
    !!! note
        A la capçalera del llistat d'interruptors podem veure el nombre d'interruptors oberts

 
4. Premer el botó de "Simula" que haura canviat a un simbol de "Play".
    ![](_static/sim_at/step_4.png)
    
    !!! note
        * Es dibuixaran els trams desconectats en vermell i els conectats en verd.
        * En la part inferior de la targeta apreix el llistat de clients afectats, es a dis que es quederien sense corrent.
 
5. Per sortir de la simulacio podem tancar o premer "ESC".
    ![](_static/sim_at/step_5.png)


## Simulacions BT

1. Selecionar el CT que volem simular.
    ![](_static/sim_bt/step_1.png)

2. Premer "Simula". Axo obrirà el llistat d'interrutpros maniobrables, també apareixeran els interruptors oberts(vermell) i tancats(verd) al mapa.
    ![](_static/sim_bt/step_2.png)
    
    !!! note
        Si apareix el missatge "No hi ha nodes oberts" significa que en aquest CT no hi ha interruptors oberts.
 
3. Si volem canviar l'estat d'un interruptor ho podem fer prement l'interruptor al mapa. Tambè el podem modificar l'estat del interruptor en el llistat d'interruptors, en el cas que no estigui tancat el podem buscar. 
    ![](_static/sim_bt/step_3.png)
 
4. Premer el botó de "Simula" que haura canviat a un simbol de "Play".
    ![](_static/sim_bt/step_4.png)
    !!! note
        * Es dibuixaran en vermell els trams desconectats i els conectats en verd.
        * En la part interior de la targeta apreix el llitat de clients afectats, és a dir els que es quedarien sense corrent.

5. Per sortir de la simulacio podem tancar o premer "ESC".
    ![](_static/sim_bt/step_5.png)