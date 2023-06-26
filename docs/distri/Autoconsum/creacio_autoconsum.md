# **Generació fitxes autoconsum**
## **La fitxa autoconsum**

La fitxa d'autoconsum es genera en esborrany quan generem el M1 01
d'autoconsum i s'activarà amb el M1 05.

En alguns casos aquesta fitxa no es fa automàticament i cal crear la fitxa
d'autoconsum, el generador i associar el generador al CUPS manualment:
Anar a Menú de l'ERP a l'apartat d'autoconsum:

![](../_static/autoconsum/1a_auto.png)

Fer una primera cerca amb el CUPS a l'espai de CAU per cercar si ja està creat o no.

![](../_static/autoconsum/2a_auto.png)

Si no està creat hem de crear un de nou, “Nuevo” i omplir els següents camps:

![](../_static/autoconsum/3a_auto.png)

A la data d'alta posarem la data que indica l'xml i a la resta de camps igualment.
Si es tracta d'una fitxa d'autoconsum que estem creant per un canvi de comercialitzadora amb autoconsum com data d'alta, farem constar la data d'activació del contracte amb nosaltres. La modalitat l'escollirem segons el camp TipoAutoconsumo del CX 05. 

Si és 41 és que té excedents, no col·lectiu i subsecció Con excedentes y mecanismo de compensación simplificado. Haurem de demanar les dades de la seva instal·lació.

![](../_static/autoconsum/4a_auto.png)

Un cop desat, la fitxa queda en esborrany. Quan s'activa la Cx 05 o la
M1 05 la fitxa ja s'activarà amb la data del 05.
Només activem manualment les fitxes d'auto en casos que no hi hagi cas
ATR. 

**Generador**

Un cop creada la fitxa cal crear el "Generador". Anar al mateix apartat d'autoconsum a la secció "Generadors autoconsum".

![](../_static/autoconsum/5a_auto.png)

Creem un “nuevo” i omplim els diferents camps de les següents imatges.

![](../_static/autoconsum/6a_auto.png)

![](../_static/autoconsum/7a_auto.png)

Autoconsum: el CAU del xml D1 01

Tipus instal·lació:

### 01 - Red interior
### 02 - Red interior de varios consumidores (instalación de enlace)
### 03 - Próxima a través de red

Esquema mesura:

### A - EdM Bidireccional en PF
### B - EdM Bidireccional en PF y EdM gen. Neta
### C - EdM Consumo Total y EdM bidireccional gen. Neta
### D - EdM Consumo Total y EdM gen bruta y EdM SSAA
### E - Configuración singular

És necessari també indicar la referència cadastral que ens informen a l'xml
per evitar problemes si ens indiquen modificacions sobre el mateix
generador.

## **Associació del Generador amb el CUPS**

Un cop creat el generador cal associar-ho al CUPS, perquè aparegui la
pestanya “Autoconsum” en el contracte. Anem a l'apartat de CUPS,
cerquem el CUPS que li correspon.

![](../_static/autoconsum/8a_auto.png)

Donem d'alta l'autoconsum des de CUPS -> Acció -> "Donar d'alta/baixa
un autoconsum".

![](../_static/autoconsum/9a_auto.png)

S'activarà amb el M 05 d'autoconsum (Si és un canvi de comercialitzadora
no es crearà la M 05).

Si s'ha produït un error i la fitxa d'autoconsum no és correcta, possiblement perquè el titular ens ha indicat malament les dades d'auto o per error en el registre, només hem de desvincular el CAU del CUPS fent la mateixa acció, però indicant la data de baixa.
Recomanem revisar que la data de baixa no sigui igual o posterior a la data d'activació del cas ATR que volem activar (Cx05, D101, etc…). La data de baixa sempre haurà de ser anterior al cas que vulguem activar.