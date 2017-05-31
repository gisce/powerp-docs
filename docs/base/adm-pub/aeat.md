# Subministrament Immediat d'Informació

## Introducció


## Possibles configuracions


### Opció 1: Utilitzant proxy

Aquesta opció ens permet utilitzar un servidor intermediari, el qual guardarà el certificat digital de l'empresa per l'AEAT. D'aquesta manera limitem
l'accés al certificat a únicament les persones amb accés a aquest servidor i evitem que l'ERP hi tingui accés directe, afegint així una capa de seguretat extra.

L'ERP farà peticions al servidor utilitzant un certificat local/client i aquest les reenviarà als serveis de l'AEAT afegint el certificat digital de l'empresa. 
L'esquema de connexió serà el següent:

blockdiag {
    span_width = 150;
    node_width = 50;
    A [label = "ERP", color = none];
    B [label = "Proxy", style = dashed, color = none];
    C [label = "AEAT", color = none];
    A <-> B [label = "Certificat local"];
    B <-> C [label = "Certificat empresa"];
}

### Opció 2: Connexió directe

Aquesta opció ens estalvia la necessitat d'utilitzar un servidor intermediari, però permet que qualsevol usuari amb permisos d'administrador en el
servidor de l'ERP tingui accés directe al certificat oficial de l'empresa per l'AEAT.

blockdiag {
    span_width = 150;
    node_width = 50;
    A [label = "ERP", color = none];
    B [label = "AEAT", color = none];
    A <-> B [label = "Certificat empresa"];
}