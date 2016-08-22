*****************************
Gestió de pòlisses/contractes
*****************************

.. inheritref:: base/polisses:section:tarifes_acces

Tarifes d'accés
===============

Les tarifes d'accés que venen definides amb l'ERP són les que marca la legislació
vigent.

- 2.0A (0 - 10 kW)
- 2.1A (10 - 15 kW)
- 2.0DHA (0 - 10 kW) amb discriminació horària
- 2.1DHA (10 - 15 kW) amb discriminació horària
- 2.0DHS (0 - 10 kW) amb discriminació horària "supervalle"
- 2.1DHS (10 - 15 kW) amb discriminació horària "supervalle"
- 3.0A (més de 15 kW)
- 3.1A
- 3.1A LB
- 6.1A
- 6.1B
- 6.2
- 6.3
- 6.4
- 6.5

Pòlisses/contractes
===================

Formulari d'una pòlissa/contracte
---------------------------------

.. inheritref:: base/polisses:section:fields_sec_general

Secció general
^^^^^^^^^^^^^^

.. inheritref:: base/polisses:bullet_list:fields_sec_general

* **Pòlissa**
* **Auto**
* **Data firma contracte**
* **Activa**
* **Renovació automàtica**
* **Distribuidora**
* **Referència distribuidora**
* **Titular**
* **CNAE**
* **Data alta**
* **Data baixa**

.. inheritref:: base/polisses:section:fields_page_general

Pestanya general
^^^^^^^^^^^^^^^^

.. inheritref:: base/polisses:bullet_list:fields_page_general

* **CUPS**
* **Direcció CUPS**
* **Tarifa d'accés**
* **Potència contractada**
* **Tensió**
* **Potències contractades per període**
* **Tipus de vivenda**

.. inheritref:: base/polisses:section:fields_page_contactes

Contactes
^^^^^^^^^

.. inheritref:: base/polisses:bullet_list:fields_page_contactes

* **NIF Titular**

.. inheritref:: base/polisses:section:fields_page_modcontractuals

Modificacions contractuals
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. inheritref:: base/polisses:bullet_list:fields_page_modcontractuals

* **Modificació contractual actual**
* **Llistat de modificacions contractuals**

.. inheritref:: base/polisses:section:fields_page_observacions

Observacions
^^^^^^^^^^^^

.. inheritref:: base/polisses:bullet_list:fields_page_observacions

* **Observacions**



Canvi data firma contracte
--------------------------

En un contracte podem actualitzar la data de firma de contracte sense la
necessitat de fer una modificació contractual mitjançant un assistent creat
expresament

Des de una pólissa o des del botó acció del llistat de pólisses podem prèmer
sobre el botó **Actualitzar data firma contracte**. Ens apareixerà el formulari
:ref:`wizdatafirma` on podrem veure la pólissa seleccionada i la data de firma
de contracte actual (si en té). Prement en el botó continuar, actualitzarà la
data de firma de contracte de la **pólissa** i la **modificació contractual
activa**.

.. warning::

   No es farà cap tipus de validació sobre la data introduïda. Si és una data
   vàlida es modificarà la data actual sense tenir en compte cap altra
   consideració com la data d'alta i de baixa de la pòlissa o la data actual

.. _wizdatafirma:
.. figure:: _static/polisses/WizardDataFirmaContracte.png

   Assistent per canviar la data de firma de contracte

Modificacions contractuals
==========================

