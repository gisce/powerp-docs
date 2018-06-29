# Notificacions a client Final

Durant un procés de switching es dónen diverses situacions on és recomanable
una notificació al client final per part de la Comercialitzadora entrant.
GISCE-ERP permet estandaritzar aquestes notificacions mitjançant plantilles
**PowerEmail** per facilitar aquestes notificacions via email i incloure-les
dins el propi cas.

S'han definit tres notificacions:

 * [Acceptació del procés](#acceptacio-de-proces).
 * [Activació del procés](#activacio-del-proces-de-canvi-de-comercialitzadora).
 * [Notificació de cas ATR](#notificacions-a-clients-de-casos-atr)


## Acceptació de procés

Quan la comercialitzadora entrant rep un XML d'acceptació (C1-02, C2-02 o
M1-02) es pot notificar al client que ja s'ha acceptat la seva petició de canvi
o modificació de dades i properament serà activada. Per fer-ho podem anar a
l'acció **Switching: Notificació acceptació procés Mail Form** i omplir el
compte de correu des del qual es vol enviar el correu a la fitxa PowerEmail.


##### Formulari notificació acceptació canvi
![](../_static/atr/PowerEmailAcceptacio.png)


## Activació del procés de canvi de comercialitzadora

Quan la comercialitzadora rep un XML d'activació de canvi de comercialitzadora
(C1-05, C2-05 o C2-07) es pot notificar al client que el procés de canvi s'ha
acabat i que per tant ja és client de la nova comercialitzadora. Per fer-ho
podem anar a l'acció **Switching: Notifiació activacio Polissa (Canvi
Comercialitzador)** i omplir el compte de correu des del qual es vol enviar el
correu a la fitxa PowerEmail.


##### Formulari notificació activació canvi de comercialitzadora

![](../_static/atr/PowerEmailActivacio.png)

## Notificacions a clients de casos ATR

Hem desenvolupat un sistema que permet notificar als clients dels casos ATR.

Aquest sistema es basa en plantilles PowerEmail i un assistent per enviar
les notificacions als casos corresponents.

Per defecte s'utilitza la variable `sw_mail_user_notification_on_activation` per
saber si els nous passos creats s'han de notificar.

Els passos per notificar es poden notificar manualment, o bé
amb [l'assistent per notificar casos ATR](#assistent-per-notificar-casos-atr)

!!! Warning "Atenció"
    Els casos "pendents de notificar" només es marcaran com a notificats si
    s'utilitza l'assistent o si s'utilitza la funció "notifica_a_client".
    Aquesta funció es crida quan s'utilitza el botó "aplicar canvis".

### Configuració

Per a que funcioni correctament l'assistent, cal configurar les següents
variables de configuració en "**Menú OpenERP > Administració > Configuració >
Propietats**":

![](../_static/atr/correo_notificacion_variable.png)

* `sw_mail_user_notification_on_activation`:
    Adreça del compte des del que enviar els correus amb l'assistent.
    Cal tenir un compte PowerEmail actiu amb aquest valor.

* `sw_email_address_user_notification`:
    Passos ATR a notificar al activar-se.
    Es poden marcar tots o bé alguns amb un format de llista.

|               Nom de la Variable        |           Exemple              |
|:---------------------------------------:|:------------------------------:|
| sw_mail_user_notification_on_activation |  `all` // `['A3-01', 'A3-02']` |
| sw_email_address_user_notification      |  `atr@company.com`             |

### Plantilles PowerEmail

Aquestes notificacions utilitzen plantilles PowerEmail inicialitzades en el
mòdul de Gestió ATR. Aquestes plantilles són bastant simples però es poden
editar a través del mòdul de PowerEmail.

![](../_static/atr/PowerEmailPlantilles.png)

Es poden trobar filtrant amb el nom de plantilla "_ATR {nom_del_cas}{nom_del_pas}:_".
Per exemple: `ATR A301:`.

S'ha de tenir en compte que el `object` que s'utilitza és el cas ATR.

### Assistent per notificar casos ATR

Aquest assistent ens permet notificar de forma agrupada diversos passos i casos
ATR. Podem fer-ho des de la vista de casos ATR "**Menú OpenERP > Gestió ATR >
Casos ATR**", prement sobre accions i escollint "_Enviar correu als casos
ATR pendents de notificar_".

![](../_static/atr/WizardNotificarAccio.png)

Seguidament l'assistent ens informarà sobre els passos marcats com "_pendent de
notificar_" dels casos seleccionats.

Si ens sembla correcte (podem repassar els passos de cada cas seleccionat),
podem procedir amb l'enviament. Prement el botó "_enviar correus pendents_":

![](../_static/atr/WizardNotificarPrevi.png)

Aquest procés pot tardar una estona segons la quantitat de casos seleccionats.

Una vegada finalitzat el procés, l'assistent s'actualitzarà i mostrarà els casos
notificats i si ha trobat algun error en el procés que ha impedit la notificació.
El resultat de la tasca es quedarà registrat en la finestra de peticions, que
es troba en la cantonada d'abaix a la dreta de la finestra del ERP.

![](../_static/atr/WizardNotificarPeticions.png)

---