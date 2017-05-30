# Subministrament Immediat d'Informació

## Introducció


## Possibles configuracions


### Opció 1: Utilitzant proxy

Aquesta opció ens permet utilitzar un servidor intermediari, el qual guardarà el certificat oficial de l'empresa per l'AEAT. D'aquesta manera limitem
l'accés al certificat a únicament les persones amb accés a aquest servidor i evitem que l'ERP hi tingui accés directe, afegint així una capa de seguretat extra.

Per tal d'establir la connexió entre l'ERP i el nou servidor, s'utilitzarà un nou certificat que crearem específicament per aquesta funció, de tal forma
que l'esquema de connexió serà el següent:


#### Configuracio del proxy

...

### Opció 2: Connexió directe

Aquesta opció ens estalvia la necessitat d'utilitzar un servidor intermediari, però permet que qualsevol usuari amb permisos d'administrador en el
servidor de l'ERP tingui accés directe al certificat oficial de l'empresa per l'AEAT.
