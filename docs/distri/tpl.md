# Índex

1. [Objecte](#objecte)
2. [Normativa](#normativa)
3. [Termes i definicions](#termes-i-definicions)
4. [Requeriments del sistema i instal·lació](tpl/requisitos.md)
	1. [Requeriments del sistema](tpl/requisitos.md#requeriments-del-sistema)
	2. [Instal·lació](tpl/requisitos.md#installacio)
5. [Procés de treball](tpl/proceso_de_trabajo.md)
	1. [Introducció](tpl/proceso_de_trabajo.md#introduccio)
	2. [Fluxogrames de processos](tpl/proceso_de_trabajo.md#fluxorames-de-processos)
	3. [Organització dels fitxers d'intercanvi en el TPL](tpl/proceso_de_trabajo.md#organitzacio-dels-fitxers-dintercanvi-en-el-tpl)
	4. [Menú de Gestió de Rutes](tpl/proceso_de_trabajo.md#menu-de-gestio-de-rutes)
	5. [Presa de Lectures de forma Manual](tpl/proceso_de_trabajo.md#presa-de-lectures-de-forma-manual)
    	1. [Tarifes de 1 o 2 períodes](tpl/proceso_de_trabajo.md#tarifes-de-1-o-2-periodes)
    	2. [Tarifes de 3 i 6 períodes](tpl/proceso_de_trabajo.md#tarifes-de-3-i-6-periodes)
	6. [Incidències i Observacions](tpl/proceso_de_trabajo.md#incidencies-i-observacions)
	7. [Menú Navegació](tpl/proceso_de_trabajo.md#menu-navegacio)
	8. [Buscar un comptador](tpl/proceso_de_trabajo.md#buscar-un-comptador)
	9. [Avisos i situació del Punt de Mesura](tpl/proceso_de_trabajo.md#avisos-i-situacio-del-punt-de-mesura)
6. [Descàrrega electrònica de Tancaments i Curves](tpl/descarga_cierres_y_curvas.md)
	1. [Descàrrega automàtica pel Port Òptic](tpl/descarga_cierres_y_curvas.md#descarrega-automatica-pel-port-optic)
    	1. [Configuració de la descàrrega](tpl/descarga_cierres_y_curvas.md#configuracio-de-la-descarrega)
    	2. [Descàrrega de Tancaments](tpl/descarga_cierres_y_curvas.md#descarrega-de-tancaments)
    	3. [Descàrrega de Corbes](tpl/descarga_cierres_y_curvas.md#descarrega-de-corbes)
7. [Fitxers d'intercanvi per GISCE-TPL](tpl/intercambio_tpl.md)
	1. [Especificacions comuns a tots els fitxers](tpl/intercambio_tpl.md#especificacions-comuns-a-tots-els-fitxers)
	2. [Codificació dels camps Data/Hora](tpl/intercambio_tpl.md#codificacio-dels-camps-datahora)
	3. [Codificació del camp "_Configuración Puerto_"](tpl/intercambio_tpl.md#codificacio-del-camp-configuracion-puerto)
	4. [Codificació del camp "_Calidad_"](tpl/intercambio_tpl.md#codificacio-del-camp-calidad)
	5. [Fitxer de Ruta (GISCE-ERP → GISCE-TPL)](tpl/intercambio_tpl.md#fitxer-de-ruta-gisce-erp-gisce-tpl)
	6. [Fitxer de Lectures (GISCE-TPL → GISCE-ERP)](tpl/intercambio_tpl.md#fitxer-de-lectures-gisce-tpl-gisce-erp)
	7. [Fitxer de corbes (GISCE-TPL → GISCE-ERP)](tpl/intercambio_tpl.md#fitxer-de-corbes-gisce-tpl-gisce-erp)
	8. [Catàleg d'anomalies](tpl/intercambio_tpl.md#cataleg-danomalies)
	9. [Catàleg de situacions](tpl/intercambio_tpl.md#cataleg-de-situacions)
	10. [Catàleg d'Avisos](tpl/intercambio_tpl.md#cataleg-davisos)
8. [Fitxers d'intercanvi entre GISCE-TPL i GISCE-ERP](tpl/intercambio_tpl_erp.md#fitxers-dintercanvi-entre-gisce-tpl-i-gisce-erp)
	1. [Exportació del fitxer de Rutes](tpl/intercambio_tpl_erp.md#exportacio-del-fitxer-de-rutes)
	2. [Exportació del fitxer de Lectures](tpl/intercambio_tpl_erp.md#exportacio-del-fitxer-de-lectures)

# Objecte

Aquest manual descriu la aplicació "GISCE-TPL", que serveix per recollir les
lectures d'un o més conjunts d'equips de mesura, tant de forma manual
com de forma automàtica utilitzant els ports sèrie del equip
de mesura òptic o DB-9 amb el protocol IEC-870.

# Normativa

Reglament de punts de mesura. Protocol de comunicacions entre registradors i
concentradors de mesures o terminals portàtils de lectures. Protocol
**IEC870REE** definit per _Red Elèctrica de España_:

Norma internacional **IEC 870-5-102**, tal com apareix en la edició de _1996_.

ORDRE **ITC/1723/2009** del 26 de Juny, per la que es revisen els petges
d'accés a partir de 1 de juliol de 2009 i les tarifes i primes de determinades
instal·lacions de règim especial.

"**_Tablas de codigos\_CNE\_V\_11\_(220109).doc_**", i es pot modificar o
ampliar fàcilment, apartat "**Fitxers d'intercanvi**"

# Termes i definicions

En la descripció del procés d'obtenció dels indicadors de _Continuitat de
Subministre_ apareixen alguns termes amb les següents definicions:

- **TPL**: Corresponen a "_Terminal Portàtil de Lectura_", i en aquest manual
  es refereix a un _ordinador portàtil_ o una _PDA_ basats en _Windows Mobile_;
  Per a les lectures automàtiques es necessita un terminal amb un port sèrie
  **RS232**.
- **Punt de mesura**: El lloc concret de la xarxa on s'ubica l'equip de mesura
- **Ruta**: Consisteix en una col·lecció de _punts de mesura_, disposats en un
  ordreapropiat perquè una persona els recorri tots per dur a terme alguna
  feina, per exemple, en el cas que ens ocupa, recollir les lectures i/o corbes
  de la càrrega.
- **Ordre** Es el lloc que ocupa un _punt de mesura_ dins
  d'una _ruta_ de lectura.
- **Avís comptador**: Es denomina _avís_ a qualsevol advertència que es
  realitza al operador de _TPL_ i que hauria de hauria de tenir en compte abans
  de realitzar la lectura d'un determinat _equip de mesura_.
- **Situació comptador**: Es la informació referida a un punt de mesura per la
  seva fàcil localització i que serveix d'ajuda al operador de _TPL_ per
  localitzar l'_equip de mesura_.
