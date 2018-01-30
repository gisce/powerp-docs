# Documentació del mòdul de Canvis d'ATR (Switching)

## Introducció


El mòdul de canvis d'ATR o switching  ``giscedata_switching`` permet a
GISCE-ERP la gestió de l'intercanvi de fitxers entre distribuidores i
comercialitzadores que es generen per la mobilitat dels consumidors i la
intermediació de les comercialitzadores entre les distribuidores i els abonats.
Aquests fitxers venen definits per **CNMC** (abans **OCSUM**).

Actualment, aquest mòdul és capaç de llegir i generar:

* **C1**: Una pólissa canvia de comercialitzadora. Intervenen la
  comercialitzadora entrant, la comercialitzadora sortint i la distribuïdora

* **C2**: Una pólissa canvia de comercialitzadora amb modificació de dades. És
  el mateix cas que un C1 però es modifiquen característiques com la potència
  contractada, el titular o la tarifa

* **M1**: Modificació de dades. La pólissa modifica alguna de les seves
  característiques com la potència contractada, titular o la tarifa. Intervenen
  la comercialitzadora actual i la distribuidora actual. Actualment es poden
  fer canvis de titular, modificacions de potència i canvis de tarifa d'accés.

* **B1**: Baixa per finalització d'activitat. Intervenen la
  comercialitzadora sortint i la distribuidora.

* **D1**: Notificació de modificació de característiques ATR per part de la
  distribuidora.

* **A3**: Alta directa a mercat. En el procés intervé la comercialitzadora
  entrant i la distribuidora.

* **R1**: Reclamacions a distribuïdora. En el procés intervé la comercialitzadora
  actual.

* **W1**: Notificació de autolectures a la distribuïdora des de la comercialitzadora.

Per facilitar el processat massiu de casos, s'han afegit diverses eines i
assistents per realitzar accions en múltiples casos.

Els fitxers d'intercanvi de lectures i factures entre distribuidores i
comercialitzadores s'implementen en els mòduls
``giscedata_facturacio_switching`` i ``giscedata_lectures_switching`` per
processar els fitxers **F1** i **Q1** respectivament i no es tracten en aquest
document.

---

## Documentació específica

[Gestió ATR Comercialitzadores](../../comer/atr.md)

---

## Conceptes


Per entrendre el funcionament del mòdul de switching, cal tenir clar alguns
conceptes.


#### Agent

Qualsevol de les empreses que intervenen en un procés de switching és un agent.
Qui comença un procés sempre és una comercialitzadora. Com a mínim intervenen
sempre una distribuidora i una comercialitzadora. En el cas d'un canvi de
comercialitzadora (p.e. ``C1``) podem parlar de *comercialitzadora entrant*
(qui demana el canvi), *comercialitzadora sortint* (qui té la pólissa
actualment) i *distribuídora* a la qual pertany el CUPS.

Els fitxers s'intercanvien sempre entre dos agents, un dels qual es
l'origen i l'altre el destinatari.


#### Processos

Un procés defineix el flux de passos i actuacions que realitzaràn tots els
agents implicats.

Un procés comença amb una sol·licitud des d'un agent que genera un fitxer amb
el format addient. L'iniciador, generarà un fitxer de **pas 1** del
procediment. Cada procediment té el seu fluxe específic amb diferents passos.

Un procés defineix quin són els agents implicats i els possibles passos
(obligatoris o no)

P.e.: **C1** és un procés que pot tenir fins a 10 passos


#### Passos

Un pas és qualsevol transició entre els estats en el qual es pugui trobar un
procés. A cada pas, li correspon un format de fitxer. Per tant tenim un fitxer
de *pas n* del proces *P*.

Alguns dels passos són obligatoris i d'altres opcionals. Un exemple de pas
opcional pot ser un pas de ``Rebuig``.

Tots els passos d'un procés tenen definit l'origen i el destí.


#### Casos

GISCE-ERP modelitza un procés en concret com un cas de CRM del propi ERP.
Concretament es crea una secció Switching en l'arbre de casos. Mitjançant el
cas podem accedir a l'historial de missatges generats i visualitzar l'estat
actual del proces concret, p.e. "Pendent de reposta després de pas 2". Tot el
seguiment del fluxe es pot fer mitjançant el cas.

La generació dels fitxers XML on l'origen siguem nosaltres, utilitzarà la
informació ja disponible dels diferents passos emmagatzemats en el cas.

---

## Configuració

Alguns dels paràmetres que han d'estar correctament configurats són:

* **Power Email**: Es necessita activar el Power Email si es volen enviar els
  mails directament des de l'ERP. Caldrà configurar els comptes que es vulguin
  i assegurar-se que funcionen
* **Código REE**: La empresa associada a la companyia ha de tenir el codi de
  **REE** correctament emplenat al camp ``Codi``. També hauran de tenir-ho
  correctament configurat les companyies susceptibles de ésser agents implicats
  en un procés de switching
