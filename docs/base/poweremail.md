# Documentació del mòdul de PowerEmail

Documentació per al mòdul de PowerEmail.

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
