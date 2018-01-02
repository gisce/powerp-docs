# Apendix

## Apendix A: Exemple de procés C1


## Apendix B: Traducció de codi REE

El càlcul del codi REE de la distribuidora té algunes particularitats en el cas
que el CUPS pertanyi a les distribuidores **ENDESA** (0031) o **FENOSA** (0390)

S'utilitza la part del CUPS que correspon al codi de la distribuidora i algun
caràcter més.

Aquestes distribuidores demanen que els casos generats portin en el codi REE de
destinatari el de la distribuidora original.

!!! Warning "Atenció"
    És molt important que les distribuidores estiguin creades i tinguin com a
    **Empresa principal** la empresa segons el CUPS. Si no és així, no es
    validaran correctament els XML's de resposta

![](../_static/atr/EmpresaPrincipal.png)

   Empresa principal per distribuidores absorbides

L'algoritme que es segueix és el següent i en aquest ordre:


### ENDESA 0031

* Si el CUPS comença per **00314** s'utilitza la **província** a la que pertany per
  escollir la distribuidora

  * Osca, Terol, Saragossa:  **0029** (``FECSA Aragó``)
  * Altres:

    * **0396** (``Hidroelèctrica de l'Empordà``) si comença per **003144**
    * **0024** (``FECSA Catalunya``) tots els altres

* Si el CUPS comença per **003130**: **0029** (``FECSA Aragó``)
* La resta, es fa seguint aquesta taula:


| CUPS  | Distribuidora                        |
|:-----:|:-------------------------------------|
| 00311 | 0023 (Cia sevillana)                 |
| 00313 | 0120 (Aragonesa Act.)                |
| 00315 | 0288 (Balears Gas y E.)              |
| 00316 | 0363 (Unión Eléctrica Canarias SUP)  |


### FENOSA 0039

* Si el CUPS comença per **03900**: **0022** (``Jallas``)
