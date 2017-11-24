# Documentació del mòdul de PowerEmail

Aquest mòdul no està integrat en el codi del ERP, però està disponible a
[GitHub/gisce/PowerEmail](https://github.com/gisce/poweremail).

## Instal·lació

Aquest mòdul no està integrat en el codi de GISCE-ERP, pel que cal descarregar-lo
com un repositori apart. Des de GISCE-TI tenim un FORK a GitHub on mantenim la
branca `v5_backport`, ja que aquest mòdul està pensat per Odoo i nosaltres
utilitzem la versió 5 de OpenERP.

Com tots els mòduls externs, cal realitzar els links adients a la carpeta
d'OpenERP `server/bin/addons`.

Com que s'ha canviat el codi, caldrà reiniciar el servidor (o iniciar-lo en un
altre port) i procedir a la instal·lació com qualsevol mòdul de OpenERP.

Una vegada instal·lat el mòdul, ja disposarem de diferents vistes noves en un
nou menú:

![](_static/poweremail/poweremail_main_menu.png)

### Creació d'un compte PowerEmail

PowerEmail funciona amb comptes _smtp_. Tant si volem enviar com si volem rebre
correus, és necessari afegir un compte PowerEmail.

En un mateix compte s'hi pot configurar l'entrada o sortida de correu.

Per afegir un compte, cal accedir al menú "**Menú OpenERP → PowerEmail →
Configuració → Tots els comptes**" i fer _click_ al botó `NEW`.

Independentment del tipus de compte a crear, sempre cal inicialitzar el `nom
del compte`. Aquest ha de ser únic entre els comptes PowerEmail.

#### Configuració d'un compte per l'enviament de correu electrònic

Quan creem (o editem) un nou compte de PowerEmail, ens mostrarà un formulari
amb els camps necessaris per la connexió amb un servidor _smtp_.

![](_static/poweremail/pwmail_account_sortida.png)

Es disposa dels camps:

|          Nom del Camp            |                                  Descripció                                |
|:--------------------------------:|:---------------------------------------------------------------------------|
| Servidor                         | Nom del servidor de correu                                                 |
| Port SMTP                        | Port SMTP utilitzat per el servidor de correu                              |
| Utilitzar TLS                    | Si es desitja utilitzar transmissió segura mitjançant claus                |
| ID correu electrònic             | Nom del correu electrònic a utilitzar en el servidor                       |
| Nom d'usuari                     | Nom d'usuari a utilitzar en el servidor (Per defecte el correu electrònic) |
| Contrasenya                      | Contrasenya a utilitzar en el servidor                                     |
| Usuari Relacionat                | Usuari del OpenERP relacionat amb aquest compte de PowerEmail              |
| Compte de correu de la companyia | Si es desitja configurar com a compte de la companyia                      |
| Format del correu electrònic     | Format a utilitzar per construir el "body" del correu                      |

Una vegada entrats els valors, es pot comprobar la connexió amb el servidor
_smtp_ amb el botó `comprobar connexió de sortida`.

![](_static/poweremail/pwmail_account_sortida_check.png)

##### Configuració d'un compte per l'enviament de correu de la companyia

Creant un compte normal per a l'enviament de correu electrònic, caldrà
seleccionar el camp `Compte de correu de la companyia` amb el valor `Si`.

Això farà que ens aparegui una pestanya `seguretat` en la vista del compte.

![](_static/poweremail/pwmail_account_sortida_example.png)

Per tal d'utilitzar un compte de companyia és necessari assignar un grup
d'usuaris al compte. En la pestanya `seguretat` es pot seleccionar quins
grups poden utilitzar aquest compte que estem creant.

!!! Note "Exemple"
    Podem fer un compte genèric afegint el grup `Employee`.

    ![](_static/poweremail/pwmail_account_sortida_example_security.png)
