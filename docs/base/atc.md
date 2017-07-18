# Módul d'Atenció al Client

## Introducció


El mòdul de atenció al client (ATC) permet a GISCE-ERP la gestió de les
reclamacions dels consumidors a través de casos i la generació dels fitxers amb
tota la informació referent a ells, complint així amb el que ve definit en la
circular [2/2016](http://www.boe.es/diario_boe/txt.php?id=BOE-A-2016-7979)
de la CNMC sobre petició de informació sobre reclamacions de
consumidors de energia elèctrica i gas natural als comercialitzadors i
distribuidors.

El format i les dades d'aquests fitxers venen definits per la CNMC.


## Casos

GISCE-ERP modelitza una reclamació en concret com un cas de CRM del propi ERP.
Mitjançant el cas podem accedir a tota la informació referent a la reclamació.

Aquest mòdul extén els casos CRM del ERP, per tant, el seu funcionament és el
mateix.
Tot i aixó, s'afageixen nous camps per tal de obtenir tota la informació
requerida per la CNMC:

* A la pestanya **General**:

    * **Imputació de Temps**: Agent al que se l'hi imputarà el temps gastat en
        l'estat actual. Hi ha 4 agents definits per la CNMC: Comercilitzador,
        Distribuidor, Client i Altres. Només es pot modificar a través de
        **l'assistent de canvi d'estat**.

    * **Agent Actual**: Agent que te accions pendents. Coincideix amb l'agent al
        que se l'hi imputa el temps excepte en el cas que aquest sigui 'Altres',
        que s'ha de indicar especificament quin és.

    * **Reclamant**: Agent que planteja la reclamació.

    * **Resultat**: Resultat final de la reclamació.

![](_static/atc/camps_nous_general.png)


* A la pestanya **Extra Info**:
    * **Número total afectats**: Numero total de cups afectades en la reclamació.


    * **Subtipus**: Subtipus de la reclamació. Si n'hi ha varis s'indica el
        princpal.

![](_static/atc/camps_nous_extra.png)


## Assistent Canvi d'Estat
En un cas d'atenció al client, quan es vol canviar d'estat s'utilitza un assistent.
Aquest assistent es crida des del propi cas amb un botó en la pestanya "General" a la part inferior:


![](_static/atc/assistent_atc.png)


Al clicar el botó apareix una finestra en que es demana:

*   **Imputació de Temps**: s'ha de escollir a quin agent se l'hi imputarà
el temps que es gasti en el nou estat del cas.
*   **Agent Actual**: quan s'escull 'Otros' a "imputacio de Temps", s'ha
d'especificar l'agent.
*  ** Nou Estat **: estat al que es passarà el cas.
*  ** Resultat **: quan el cas es passa a "Tancat", s'ha de indicar el
resultat final.

Clicant a "Acceptar" es pasarà el cas a l'estat escollit i s'actualitzaran
la imputació de temps i l'agent actual amb la informació escollida.

## Guia d'Atenció al Client

El funcionament del procés d'atenció al client és el mateix tant per les
distribuïdores com per les comercialitzadores. L'única diferència entre elles
és que una distribuïdora gestionarà les reclamacions rebudes de les
comercialitzadores a través del procés de ATR R1 en comptes de fer-ho en el
present módul.

Per veure un procés complet d'atenció al client, a continuació s'exposa un
exemple en el qual un client va a fer una reclamació a la comercialitzadora.
En aquest supòsit, el procés d'atenció al client, des que s'obre fins que es
tanca el cas, és el següent:


 * Arriba una reclamació per algun canal: un client truca per telèfon, envia un
 mail, ve a l'oficina, etc.


 * Es busca la pòlissa del client en qüestió i s'utilitza l'assistent per obrir
 un cas de ATC: pitjar el botó "Generar cas Atenció al Client"

 ![](_static/atc/guia_atc1.png)


 * Automàticament s'omple la descripció (que es pot canviar), la data (serà la
 del dia en què es generi) i el canal.

 * Per defecte el canal és "Directe", és a dir, que el client ha anat a l'oficina.
 S'ha d'escollir el canal correcte d'entre totes les opcions (telèfon, mail, web, etc.).

 * Omplir el subtipus al qual pertany la reclamació d'entre tots els definits segons la
 circular 2/2016. S'ha de determinar segons la informació proporcionada pel
 client a quin pertany. Si en aquell moment se n'escull un que acaba sent
 incorrecte, sempre es pot canviar més endavant (a la pestanya "Extra Info").
 Pitjant el botó "Crear" es generarà un cas de ATC amb la informació introduïda.

 ![](_static/atc/guia_atc2.png)


 * El següent pas és emplenar la resta d'informació del cas:
     * A la pestanya "General":
         * Reclamant: en l'exemple actual seria el client, però podrien ser
         altres com una asseguradora, una persona no titular del CUPS, etc.
         * Imputació de temps: es tracte de l'agent que tingui accions pendents
         i que per tant se l'hi imputarà el temps. En el supòsit actual seria
         la comercialitzadora.
             * Aquest camp és un dels més importants, ja que mesura al llarg
             del procés quant de temps ha trigat cada agent a realitzar les
             seves accions, informació que s'inclourà en la generació d'informes
              de la circular 2/2016.
             * Es canvia a través de l'assistent de canvi d'estat.
         * Descripció: en aquest camp s'escriu una breu descripció sobre la
         reclamació. És un camp totalment informatiu en què es va explicant
         l'estat en què es troba la reclamació.

     ![](_static/atc/guia_atc3.png)

     * A la pestanya "Extra Info":
         * Numero total afectats: número total de punts de suministre afectats.
         Per defecte és 1.

     ![](_static/atc/guia_atc4.png)


 * Un cop emplenada tota la informació, ja es pot obrir el cas (utilitzant l'assistent).
 Es demanarà a quin estat es vol passar (en aquest cas seria a "Obert") i a
 qui se l'hi imputarà el temps que el cas es mantingui en el nou estat.

En aquest punt poden ocórrer diferents situacions depenguen de com es
resolgui la reclamació. Alguns exemples:

 * La comercialitzadora pot resoldre la reclamació sense necessitar accions
 de cap altre agent. S'utilitza l'assistent per passar el cas a tancat i seleccionar
 el resultat que pertoqui.

 * La comercialitzadora necessita que un altre agent realitzi accions.
 Per exemple:
     * Necessita més informació del client i se l'hi envia un mail
       demanant-la. En aquest cas s'utilitzaria l'assistent per passar el cas
       a "Pendent" i seleccionar com a "Imputació de Temps" el "Client" fins
       que el client proporcioni la informació demanada. Un cop arribés la informació es
       passaria a "Obert" seleccionant com a "Imputació de Temps" un altre cop la
       "Comercialitzadora" per continuar amb la reclamació.
     * Es requereixen accions per part de la distribuïdora. Això implicaria
       l'inici d'un cas de gestió ATR R1. El procediment seria el mateix:
       passar a "Pendent" amb "Distribuïdora" com a "Imputació de Temps".
       En paral·lel es gestionaria el R1 i un cop es tanqués es
       passaria a "Obert" seleccionant com a "Imputació de Temps" la
       "Comercialitzadora". És recomanable a cada pas anar escrivint al camp
       "Descripció" l'estat de la reclamació per poder fer un seguiment més fàcil.

 * L'últim pas sempre és passar el cas a "Tancat". En aquest cas en l'assistent
 es demanarà com a informació extra el resultat final de la reclamació.


## Generació de Informes

La principal funcionalitat d'aquest mòdul és la de poder generar de forma
automatitzada fitxers amb la informació sobre les reclamacions demanats per la
CNMC. El format i la informació d'aquests fitxers segueixen les directrius
definides en la circular 2/2016 mencionada anteriorment.

El procediment complet per generar aquests informes es detalla en els apartats:

 * Distribuidora -> Administració Pública -> CNMC -> Generació de Informes sobre Reclamacions de Consumidors

 * Comercialitzadora -> Administració Pública -> CNMC -> Generació de Informes sobre Reclamacions de Consumidors
