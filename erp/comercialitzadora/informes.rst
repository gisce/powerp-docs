#:after:base/informes:paragraph:informes#

Resum per tarifes
-----------------

Resum de facturació per tarifes amb el desglosament dels consums segons els periodes i energia.
L'informe inclou el resum en kWh, potència total, euros facturats i nombre de clients afectats

Resum per distribuïdora i tarifa
--------------------------------

Resum de facturació per distribuïdora i tarifa amb el desglosament dels consums segons els periodes i energia.
L'informe inclou el resum en kWh, potència total, euros facturats i nombre de clients afectats

Resum per grup cobratori
------------------------

Resum per grup de cobrament. Inclou el nombre de factures i el total facturat

Resum per municipi i tarifa
---------------------------

Resum de facturació per municipi i tarifa. Inclou el desglosament dels consums segons els periodes i energia.
L'informe inclou el resum en kWh, potència total, euros facturats i nombre de clients afectats

Detall per període i tarifa de peatge
-------------------------------------

Resum de facturació per tarifes que inclou el detall de l'energia facturada, potència facturada i potència contractada per periode

Resum per impostos i distribuïdora
----------------------------------

Resum de facturació per distribuïdora. Detalla base, impostos i total en euros facturats.

Detall d'altres conceptes
-------------------------

Resum de facturació per distribuïdora que inclou únicament els productes de tipus 'Altres'. El resum mostra els totals facturats.

Resum Factures (CSV)
--------------------

Resum de les factures en CSV.

Resum factures Excel
--------------------

Resum de les factures en Excel.


#:after:base/informes:paragraph:informes_adm#

ESCILA
------

Informe ESCILA

Model 606
---------

En la ubicació que es mostra en la `Figura 1`_ es troba el menú per a la
realizació de l'informe de preus de consumidors, model 606 que es detalla
en el BOE n. 69  Sec. I. Pàg. 30271.

El wizard de realització de l'informe es mostra en la `Figura 2`_.
Tal i com s'especifica en l'annex I del BOE esmentat anteriorment
l'informe, que s'entregarà dos cops l'any,  ha de recollir la informació
dels darrers 6 mesos. El període en qüestió s'especificarà en els apartats
'Data d'inici' i 'Data final'. La opció 'Extrapolar el consum anual', es
sel·leccionarà únicament en el cas de no existir històric d'un any (12 mesos
faturats complets), cas
en que caldrà especificar el factor de correcció a aplicar al resultat.
Per exemple, en el cas de tenir històric dels darrers 6 mesos, s'indicarà
a l'ERP que extrapoli el conum
i en el factor de correcció es sel·leccionarà 2. Si diposéssim de
12 mesos facturats únicament caldria especificar 1 al factor de correcció.
Trobeu altres exemples en la secció `Exemples de configuració`_.

En finalitzar l'informe, es mostrarà el missatge de la `Figura 3`_, que
en acceptar-se ens llistarà l'informe (veure `Figura 4`_). Únicament
cal prémer fent doble-click al damunt de l'informe per veure'n el resultat.
La `Figura 5`_ mostra el resultat d'un informe.

Finalment podem mostrar tots els informes generats anant al sub-menú
que s'indica en la `Figura 6`_ que resulta en el llistat de la
`Figura 7`_. Únicament caldria fer doble-click al damunt de l'informe escollit
per veure'n la seva informació.

Exemples de configuració
^^^^^^^^^^^^^^^^^^^^^^^^

.. _`Exemples de configuració`:

Cas 1: Hem facturat des de 01/01/2012 a 30/06/2012 (6 mesos)

    * Extrapolar consum: Sí
    * Factor de correcció: 2 (**2** x 6 mesos = 12 mesos)


Cas 2: Tenim factures de 01/04/2012 a 30/06/2012 (3 mesos)

    * Extrapolar el consum: Sí
    * Factor de correcció: 4 (**4** x 3 mesos = 12 mesos)


Cas 3: Tenim 12 mesos d'històric de facturació:

    * Extrapolar el consum: No
    * Factor de correcció: 1



Figures
^^^^^^^

.. _`Figura 1`:
.. figure::  ./_static/informes_static/informes/model_606/menu_wiz.png
   :align:  center

   Figura 1: Ubicació del formulari de generació de l'informe.

.. _`Figura 2`:
.. figure::  ./_static/informes_static/informes/model_606/wizard.png
   :align:  center

   Figura 2: Wizard

.. _`Figura 3`:
.. figure::  ./_static/informes/inf_de_0066_14_static/informes/model_606/accept.png
   :align:  center

   Figura 3: Missatge de finalització de l'informe de preus.

.. _`Figura 4`:
.. figure::  ./_static/informes/inf_de_0066_14_static/informes/model_606/inf_llist.png
   :align:  center

   Figura 4: Darrer informe realitzat.

.. _`Figura 5`:
.. figure::  ./_static/informes/inf_de_0066_14_static/informes/model_606/linies_informe.png
   :align:  center

   Figura 5: Informació associada a l'informe.

.. _`Figura 6`:
.. figure::  ./_static/informes/inf_de_0066_14_static/informes/model_606/menu_llist.png
   :align:  center

   Figura 6: Formulari per llistar tots els informes realitzats.

.. _`Figura 7`:
.. figure::  ./_static/informes/inf_de_0066_14_static/informes/model_606/tot_llist.png
   :align:  center

   Figura 7: Llistat d'informes realitzats.

Model 159
---------

En la ubicació que es mostra en la `Figura 8`_ es troba el menú per a la
generació de l'informe del model 159, tal i com es detalla en el BOE n. 182
Sec. I. Pàg. 64838.

La `Figura 9`_ mostra el wizard de generació de l'informe. Es generarà un nou
informe amb la data final indicada en prémer 'Generar informe'.  En finalitzar
el procés de realització de l'informe es mostren els errors ocurreguts
(`Figura 10`_). Prement 'Veure Informe' es llista l'informe generat
(`Figura 11`_). Finalment, fent doble click en l'informe generat, veurem les
línies de l'informe (`Figura 12`_) i tindrem la possibilitat d'exportar-lo
prement 'Exportar document'.

En exportar el document, es sol·licita informació relativa a la
persona de contacte, informació relativa al suport que s'utilitzarà
per la transmissió del document i el número d'informe que es correspon. El
número d'informe és un número seqüencial relatiu a cada informe entregat.

Valors per defecte
^^^^^^^^^^^^^^^^^^

Per tal que el resultat de la validació sigui correcte, hi ha una sèrie de
camps als quals se'ls assigna un valor per defecte en cas de no tenir valor
a l'ERP. La següent taula en detalla el nom del camp, la posició
en la línia del registre de tipus 2 i el valor assignat per defecte.

==================   ========== ============
Camp                 Posició    Valor
==================   ========== ============
NIF del titular      18         12345678Z
Tipus de via         76         CL
Tipus de numeració   131        NUM o S/N (en funció de si hi ha número)
Codi postal          264        12321
Data d'alta          367        01/07/2009 (data d'inici del règim de lliure competència)
                                en el cas de ser anterior a l'any 1930
==================   ========== ============

Errors de validació
^^^^^^^^^^^^^^^^^^^


El programa de validació del model 159, en la versió v1.0 de 2011 [1], genera una sèrie d'errors pels quals no hi ha sol·lució. Es llisten a continuació:

==================   =================================================== ============
Codi d'error         Camp                                                Motiu
==================   =================================================== ============
2 0801               Tipus de via (Direcció del subministre)             Certs tipus de via proporcionats pel catastre.
2 0701               Cognoms i nom, raó social o denominació del titular Noms que contenen nombres. També noms amb una única paraula.
==================   =================================================== ============



[1] http://www.agenciatributaria.es/static_files/AEAT/Contenidos_Comunes/La_Agencia_Tributaria/Descarga_Programas/Descarga/prevalid/2011/CobolWindows/Prevalidacion_159_2011_v10.exe

Figures
^^^^^^^

.. _`Figura 8`:
.. figure:: ./_static/informes/inf_de_0066_14/model_159/menu.png
   :align:  center

   Figura 8: Ubicació del menú per a la generació de l'informe del model 159.

.. _`Figura 9`:
.. figure:: ./_static/informes/inf_de_0066_14/model_159/wiz_generar.png
   :align: center

   Figura 9: Wizard de generació de l'informe.

.. _`Figura 10`:
.. figure:: ./_static/informes/inf_de_0066_14/model_159/wiz_mostrar.png
   :align:  center

   Figura 10: Wizard que es mostra en finalitzar l'informe i que mostra els errors apareguts.

.. _`Figura 11`:
.. figure:: ./_static/informes/inf_de_0066_14/model_159/imp_inf.png
   :align:  center

   Figura 11: Informe generat.

.. _`Figura 12`:
.. figure:: ./_static/informes/inf_de_0066_14/model_159/linia_tree.png
   :align:  center

   Figura 12: Línies de l'informe generat.


.. _`Figura 13`:
.. figure:: ./_static/informes/inf_de_0066_14/model_159/wiz_exportar.png
   :align:  center

   Figura 13: Wizard per exportar l'informe.

.. _`Figura 14`:
.. figure:: ./_static/informes/inf_de_0066_14/model_159/imp_tree.png
   :align:  center

   Figura 14: Llistat de tots els informes generats.


INF/DE/0066/44
--------------

Introducció
^^^^^^^^^^^

Per poder fer una auditoria de canvis de comercialitzadora, la CNMC demana un
CSV amb el format definit a INF/DE/0066/14

Generació
^^^^^^^^^

Per generar el fitxer, hem d'executar l'assistent que trobarem a
`Administració pública > CNMC > Informe INF/DE/0066/14`

.. image:: _static/informes/inf_de_0066_14/menu.png


Només caldrà introduïr l'any del qual es vol fer l'informe, que per defecte ja
és 2013 i prèmer el botó **Exportar**.

Des de **Fitxer** es podrà obrie el CSV i descarregar-lo a disc

.. image:: _static/informes/inf_de_0066_14/assistent.png

Dades utilitzades
^^^^^^^^^^^^^^^^^

Per omplir el fitxer es tenen en compte totes les pólisses creades dins l'any
escollit que tinguin la corresponent modificació contractual de tipus `alta`.

Així doncs, el fitxer generat serà correcte si les altes a la comercialitzadora
es registren com a modificació contractual de la pòlissa de tipus `alta`
correctament.

+----------------------------+------------------------------------------------+
| **CODIGO_INFORMANTE**      | Camp `Codi R2` de la companyia                 |
+----------------------------+------------------------------------------------+
| **CODIGO_CUPS**            | CUPS                                           |
+----------------------------+------------------------------------------------+
| **FECHA_ACTIVACION**       | Data inici de la modificació contractual nova  |
+----------------------------+------------------------------------------------+
