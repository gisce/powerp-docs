# Índex

1. [Objecte i àmbit d'aplicació](#objecte-i-ambit-daplicacio)
2. [Normativa](#normativa)
3. [Termes i definicions](qualitat/termes_i_def.md)
    1. [Definició de zones](qualitat/termes_i_def.md#definicio-de-zones)
    2. [Recollida d'informació](qualitat/termes_i_def.md#recollida-dinformacio)
    3. [Obtenció de la potencia total instal·lada](qualitat/termes_i_def.md#obtencio-de-la-potencia-total-instalada)
    4. [Emmagatzematge de dades](qualitat/termes_i_def.md#emmagatzematge-de-dades)
    5. [Informació associada a una incidència](qualitat/termes_i_def.md#informacio-associada-a-una-incidencia)
    6. [Criteris per la determinació del nombre i duració de les interrupcions](qualitat/termes_i_def.md#criteris-per-la-determinacio-del-nombre-i-duracio-de-les-interrupcions)
    7. [Desagregació de les dades de la interrupció](qualitat/termes_i_def.md#desagregacio-de-les-dades-de-la-interrupcio)
    8. [Informació associada a instal·lacions i clients](qualitat/termes_i_def.md#informacio-associada-a-instalacions-i-clients)
    9. [Metodologia pel càlcul de l'indicador percentil 80 de TIEPI](qualitat/termes_i_def.md#metodologia-pel-calcul-de-linicador-percentil-80-de-tiepi)
    10. [Metodologia per la obtenció d'informació zonal d'interrupcions en BT](qualitat/termes_i_def.md#metodologia-per-la-obtencio-dinformacio-zonal-dinterrupcions-en-bt)
    11. [Avaluació de la qualitat individual](qualitat/termes_i_def.md#avaluacio-de-la-qualitat-individual)
    12. [Documentació Suport](qualitat/termes_i_def.md#documentacio-suport)
        1. [Generació d'avisos d'incidències](qualitat/termes_i_def.md#generacio-davisos-dincidencies)
        2. [Dades introduïdes en el sistema de forma manual](qualitat/termes_i_def.md#dades-introduides-en-el-sistema-de-forma-manual)
        3. [Modificació de dades](qualitat/termes_i_def.md#modificacio-de-dades)
        4. [Classificació de la interrupció com a programada](qualitat/termes_i_def.md#classificacio-de-la-interrupcio-com-a-programada)
        5. [Classificació de la interrupció com originada per tercers](qualitat/termes_i_def.md#classificacio-de-la-interrupcio-com-originada-per-tercers)
        6. [Classificació de la interrupció com originada per forca Major](qualitat/termes_i_def.md#classificacio-de-la-interrupcio-com-originada-per-forca-major)
    13. [Sistemes Informàtics](qualitat/termes_i_def.md#sistemes-informatics)
    14. [Model d'informe](qualitat/termes_i_def.md#model-dinforme)
4. [Marc de referència del model de Qualitat](qualitat/marc_ref_model.md)
    1. [Enfocs de qualitat](qualitat/marc_ref_model.md#enfocs-de-qualitat)
    2. [Qualitat del producte i cicle de vida](qualitat/marc_ref_model.md#qualitat-del-producte-i-cicle-de-vida)
    3. [Elements a ser avaluats](qualitat/marc_ref_model.md#elements-a-ser-evaluats)
    4. [Us d’un model de qualitat](qualitat/marc_ref_model.md#us-dun-model-de-qualitat)
5. [Model de qualitat per la qualitat interna i externa](qualitat/model_interna_i_externa.md)
6. [Model de qualitat per la qualitat en us](qualitat/model_en_us.md)
7. [Generació d'incidencies](qualitat/generacio_incidencies.md)
8. [Obtenció de resultats](qualitat/obtencio_resultats.md)

# Objecte i àmbit d'aplicació

La "_Orden ECO / 797/2002_" del 22 de març per la que s'aprova el procediment
de mesura i control de la continuïtat del subministre eléctric. Estableix els
criteris i la metodologia a seguir per la recollida i tractament de les dades
de la continuitat del subministre, incloent els necessaris per la elaboració
dels índexos de qualitat zonal, _TIEPI_, percentil **80** del _TIEPI_ i _NIEPI_.
De la mateixa manera es defineixen les característiques del sistema de registre
d'incidéncies, la informació de base necessaria i la recollida i tractament de
les dades de continuitat necessaries per poder evaluar per cada client si s'han
incomplert les seves condicions de qualitat individual, i en cas de ser així,
poder aplicar-li el perceptiu descompte en la facturació.

Aquest procediment defineix les característiques del programa
[módul "_GISCE-ERP_QS_"](qualitat_individual.md), que està integrat en el
programa de _GIS_ i _Base de Dades_ d'instal·lacions per companyies
eléctriques "_GISCE-ERP_".

Aquest manual d'ús està dissenyat perquè un usuari del programa _GISCE-ERP_
tingui la capacitat de realitzar les tasques d'entrada, consulta, comprobació
i obtenció de resultats de qualitat de servei zonal i individual amb el módul
anomenat "_GISCE-ERP_QS_".

Aquest procediment s'aplicarà al programa "_GISCE-ERP_QS_", per al càlcul de la
qualitat zonal i individual definida en la "_ORDEN ECO / 797/2002_", per les
companyies de distribució eléctrica.

# Normativa

**Real Decret 1955/2000 de 1 de desembre** pel qual es regulen les activitats
de transport, distribució, comercialització, subministrament i procediments
d’autorització d’instal·lacions d’energia elèctrica.

**ORDEN ECO /797/2002 de 22 de març** per la que s’aprova el procediment de
mesura i control de la continuïtat del subministrament elèctric.

"Norma **UNE-ISO/IEC 9126-1**, INGENIERIA DEL SOFTWARE, CALIDAD DEL PRODUCTO
DE SOFTWARE, MODELO DE CALIDAD”.
