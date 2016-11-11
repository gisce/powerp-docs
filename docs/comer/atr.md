# Gestió ATR

## Generar casos ATR

Podem generar casos ATR de forma automatica si utilitzem un wizard. Per tal d'utilitzar
aquest wizard hem d'anar a *Gestió de Pòlisses>Pòlisses* (Figura 1).

![Figura 1](_static/switching/menu.png)

Allà haurem de seleccionar una pòlissa i premer el botò d'accions, on haurem de
seleccionar *Generar cas Gestió ATR* (Figura 2).

![Figura 2](_static/switching/selection.png)

Altrament podem entrar a la polissa i també premer el botò que diu *Generar cas Gestió ATR* (Figura 3).

![Figura 3](_static/switching/actions.png)

Això ens obrirà la següent finestra amb el wizard:

![Figura 4](_static/switching/wizard_general.png)

Des d'aqui podrem crear diferents casos segons l'estat de la polissa.
Aquestses són les condicions que haurem de complir per crear un cas:

 * **C1/C2/A3**: La polissa ha d'estar en estat borrador
 * **M1/B1**: La polissa ha d'estar en estat actiu
 * **W1**: La polissa ha d'estar en estat actiu i amb autolectures

A més, mai no pot haver-hi un altre cas de gestió ATR actiu si en volem crear un de nou.

Per tal de crear el cas que volem simplement hem de premer el botò corresponent.

### Wizard per M1 i C2

Si seleccionem que volem crear un M1 o un C2 la pantalla del wizard canviarà i podrem
entrar les dades necessaries per crear-lo.

![Figura 5](_static/switching/wizard_modcon.png)

Podem crear un canvi de tarifa o potència, un canvi de titular o un canvi de totes
dues a la vegada. Segons el que seleccionem haurem d'entrar unes dades o altres.

![Figura 6](_static/switching/wizard_modcon_changes.png)

Les primeres dades que hem d'entrar són sobre qui serà el contacte per la pòlissa.
Si premem la lupa i seleccionem una altre persona ens hauria d'omplir correctament la
resta de camps, però sempre es preferible comprovar-ho.

![Figura 7](_static/switching/wizard_modcon_contact.png)

Tot seguit tenim l'opció de canviar de tarifa comercialitzadora. Per defecte no es
canviarà i es deixarà la que té assignada la polissa però si no és possible s'haurà
de seleccionar quina tarifa volem aplicar. Si només existeix una tarifa comercialitzadora
per la tarifa ATR seleccionada aquesta es triarà automaticament.

![Figura 8](_static/switching/wizard_modcon_tariff.png)

Llavors, si hem seleccionat un canvi de tarifa o potència, ens apareixarà la part del
formulari per triar la tarifa que vol el client, si vol anar per ICP o Maxímetre i
les potencies de la tarifa. A l'hora d'entrar les potencies ens avisarà si estem posant
un valor de potencia incorrecte, ja sigui perquè el valor és massa gran o massa petit
per la tarifa seleccionada, perquè els valors de potència no tenen valors ascendents
en una tarifa que ho demana o perquè algun valor de potència no està normalitzat.
Es permeten crear casos amb valors de potència no normalitzats però si que s'han de
complir les dues altres condicions. També destacar que un canvi en la tarifa ATR seleccionada
ens pot fer canviar la tarifa comercialitzadora o borrar la que teniem assignada.

![Figura 9](_static/switching/wizard_modcon_powers.png)

Si hem seleccionat un canvi de propietari també ens apareixarà el formulari per fer un
canvi de titular. Aqui podem seleccionar el tipus de canvi que volem fer, un document
d'identitat i el titular. Si posem el mateix document d'identitat que un dels clients
que tenim entrats s'assignarà automaticament a aquest titular. El mateix passa en
l'altre sentit, de manera que si triem un titular s'omplirà automaticament el document
d'identitat. A més, sempre que no haguem canviat el contacte aquest s'actualitzarà
automàticament al assignar un titular.

![Figura 10](_static/switching/wizard_modcon_owner.png)

Finalment tenim un quadre de text per afegir comentaris, que poden tenir fins a un
màxim de 120 caracters.

Un cop entrades totes les dades podem premer el botò que apareixarà a sota, que dirà
**M1-Modificació contractual** o **C2-Canvi de comercialitzadora amb canvis** segons
el cas que estiguem intentant crear. Això comprovarà totes les dades entrades i
intentarà crear el cas corresponent. Finalment el wizard ens dirà si ha pogut crear
el cas correctament o no i en cas que hi hagui hagut algún error ens indicarà la
raò per la qual ha fallat. A més, ens permetrà obrir els casos creats si premem el
botò de **Obrir casos generats**.

![Figura 11](_static/switching/wizard_modcon_fin.png)