# orakWlum

**orakWlum** és una eina capaç de generar **previsions de consum** a partir de les mesures històriques de l'ERP de Comercialitzadora
amb la finalitat de tenir una base sòlida sobre la que generar les ofertes de compra a publicar a l'Operador del Mercat
(OMIE).

A més a més d'aquestes previsiones, **orakWlum** permet també generar **històrics**, amb la finalitat de poder mesurar el consum
real de la cartera de subministraments de la Comercialitzadora.

En ambdós elements, tant les previsions com els històrics, les dades per a alimentar el càlcul i la mesura són les diverses
col·leccions de perfils horaris (corbes publicades per les Distribuïdores i perfilats de diversos tipus) existents en el
propi ERP.

Trobareu totes les eines de **orakWlum** al menú principal amb el mateix nom, i a continuació s'indiquen els llistats i assistents
disponibles.

[ ![Menú d'orakWlum](_static/orakWlum/menu_orakWlum.png)](_static/orakWlum/menu_orakWlum.png)

* **Manteniment:** Eines auxiliars de orakWlum, com per exemple l'importador de **pèrdues de ESIOS**.

* **Previsions de consum:** Eines per a generar i revisar **Previsions de consum**.

* **Històrics de consum:** Eines per a generar i revisar **Històrics**.

Cada un dels submenús anteriors conté llistats per a revisar els elements existents i també assistents per a actuar-hi.

# Pèrdues del sistema

Les ofertes de compra publicades a mercat han d'expressar el consum **elevat en barres de central** i en **MWh amb un únic
decimal**
d'arrodoniment. Per tant, quan es generin previsions i històrics, caldrà que l'energia es mostri elevada aplicant-hi les
pèrdues corresponents.

El menú de **Manteniment** compta amb dos assistents:

* **Importar coeficients de pèrdues anuals:** Permet descarregar les pèrdues del sistema que publica l'Operador del Sistema
(REE) a `ESIOS` i enregistrar-les a l'ERP. Aquestes pèrdues seràn necessàries per a generar tant previsions de consum com
històrics. L'assistent permet triar l'any, la tarifa d'accés i el subsistema pel qual es volen importar les pèrdues, però
també és possible importar-ho tot amb una sola acció si es tria l'opció `Tots`/`Totes` als camps corresponents.

[ ![Importar pèrdues](_static/orakWlum/importar_perdues.png)](_static/orakWlum/importar_perdues.png)

!!! Info "Nota 1"
    Per tal de poder descarregar les pèrdues des de `ESIOS` serà necessari disposar d'un `token d'autenticació`, que caldrà
    tenir ja configurat a l'ERP, de la mateixa manera que és requerit també per a facturar a preu indexat a mercat.

Un cop importades les pèrdues, si es vol es poden revisar al llistat **Coeficients de pèrdues** on es mostrarà el percentatge
de pèrdues, la tarifa d'accés i el subsistema al que corresponen i la versió de la publicació que s'ha importat (**orakWlum**
sempre importarà la versió més recent publicada a `ESIOS`.). 

[ ![Llistat pèrdues](_static/orakWlum/llistat_perdues.png)](_static/orakWlum/llistat_perdues.png)

També es pot veure la data/hora de la importació i el fitxer
d'`ESIOS` del qual s'han importat.

[ ![Formulari pèrdues](_static/orakWlum/formulari_perdues.png)](_static/orakWlum/formulari_perdues.png)

* **Actualitzar coeficients de pèrdues:** Com que els coeficients de pèrdues es van actualitzant amb cada publicació de
`ESIOS`, **orakWlum** permet actualitzar els registres de les mateixes a l'ERP de Comercialitzadora. Per a fer-ho, podeu
utilitzar aquest assistent indicant la data per a la qual voleu actualitzar a la versió més recent les pèrdues de la tarifa
d'accés i el subsistema indicat.

[ ![Actualitzar pèrdues](_static/orakWlum/actualitzar_perdues.png)](_static/orakWlum/actualitzar_perdues.png)

!!! Info "Nota 2"
    Les previsions de consum, com que es solen generar a futur, sempre faran servir la versió `A2` de les pèrdues, però
    els històrics, al generar-se "a passat" podran fer servir versions més recents com la `C2`, `C3`, etc.

Amb tot aquest conjunt d'eines senzilles, es pot tenir un registre clar i precís de les pèrdues del sistema a utilitzar
a **orakWlum**. Tot i que les previsions de consum i els històrics ja descarreguen i importen les pèrdues dels dies en qüestió
automàticament, s'aconsella fer una primera importació massiva per any per si cal revisar les pèrdues d'algun dia en concret.

# Previsions de consum



# Històrics de consum



