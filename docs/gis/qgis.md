# Introduccio 
Qgis es un programa per el la gestió, consulta i anàlisis de dades GIS.
El seu funcionament pot ser estès mitjançant plugins.

Es pot consultar el manual d'usuari de QGIS a la següent adreça:
[http://www.qgis.org/es/docs/index.html](http://www.qgis.org/es/docs/index.html)


# Instal·lació
Per instal·lar el plugin de Qgis per accedir al Giscegis s'ha d'anar a:

1. Connectors
2. Gestiona i instal·la connectors
![](_static/connectors.png)

3. Anar a la secció de Configuracio
4. Activar la opció "Comprova si hi ha actualitzacions al arrancar"
5. Afegir un nou repositori de connectors amb les següents dades:
    * Nom:Gisce
    * URL: https://qgis-plugins.gisce.net/plugins/plugins.xml
    * Activar la casella d'activat
6. Tornar a carregar tots els rositoris mitjançant el boto
7. Anar a la secció de "Tot" i buscar el plugin "TileLayer Plugin" i instal·lar-lo
8. Buscar i instal·lar el plugin de "Giscegis"


# Configuració d'accés a Giscegis
Per configurar l'accés al servidor de Giscegis s'han de fer els següents passos:

1. Connectors
2. Giscegis
3. Configuració
4. Omplir el camp URL gis, Postgres Host, Postgres Port, Postgres databse, Postgres user i Postgres password amb les dades facilitades
    ![1](_static/configuracio.png)
5. Prémer el boto de + per afegir un nou servidor
6. Posar el nom del nou servidor i premer ok
    ![2](_static/dialeg.png)



