# Índex

1. [Objecte i àmbit d'aplicació](#objecte-i-ambit-daplicacio)
2. [Normativa](#normativa)
3. [Termes i definicions](calidad/terminos_y_definicion.md)
    1. [Definició de zones](calidad/terminos_y_definicion.md#definicio-de-zones)
    2. [Recollida d'informació](calidad/terminos_y_definicion.md#recollida-dinformacio)
    3. [Obtenció de la potencia total instal·lada](calidad/terminos_y_definicion.md#obtencio-de-la-potencia-total-instalada)
    4. [Emmagatzematge de dades](calidad/terminos_y_definicion.md#emmagatzematge-de-dades)
    5. [Informació associada a una incidència](calidad/terminos_y_definicion.md#informacio-associada-a-una-incidencia)
    6. [Criteris per la determinació del nombre i duració de les interrupcions](calidad/terminos_y_definicion.md#criteris-per-la-determinacio-del-nombre-i-duracio-de-les-interrupcions)
    7. [Desagregació de les dades de la interrupció](calidad/terminos_y_definicion.md#desagregacio-de-les-dades-de-la-interrupcio)
    8. [Informació associada a instal·lacions i clients](calidad/terminos_y_definicion.md#informacio-associada-a-instalacions-i-clients)
    9. [Metodologia pel càlcul de l'indicador percentil 80 de TIEPI](calidad/terminos_y_definicion.md#metodologia-pel-calcul-de-linicador-percentil-80-de-tiepi)
    10. [Metodologia per la obtenció d'informació zonal d'interrupcions en BT](calidad/terminos_y_definicion.md#metodologia-per-la-obtencio-dinformacio-zonal-dinterrupcions-en-bt)
    11. [Avaluació de la qualitat individual](calidad/terminos_y_definicion.md#avaluacio-de-la-qualitat-individual)
    12. [Documentació Suport](calidad/terminos_y_definicion.md#documentacio-suport)
        1. [Generació d'avisos d'incidències](calidad/terminos_y_definicion.md#generacio-davisos-dincidencies)
        2. [Dades introduïdes en el sistema de forma manual](calidad/terminos_y_definicion.md#dades-introduides-en-el-sistema-de-forma-manual)
        3. [Modificació de dades](calidad/terminos_y_definicion.md#modificacio-de-dades)
        4. [Classificació de la interrupció com a programada](calidad/terminos_y_definicion.md#classificacio-de-la-interrupcio-com-a-programada)
        5. [Classificació de la interrupció com originada per tercers](calidad/terminos_y_definicion.md#classificacio-de-la-interrupcio-com-originada-per-tercers)
        6. [Classificació de la interrupció com originada per forca Major](calidad/terminos_y_definicion.md#classificacio-de-la-interrupcio-com-originada-per-forca-major)
    13. [Sistemes Informàtics](calidad/terminos_y_definicion.md#sistemes-informatics)
    14. [Model d'informe](calidad/terminos_y_definicion.md#model-dinforme)
4. [Marc de referència del model de Qualitat](calidad/marco_ref_modelo.md)
    1. [Enfocs de qualitat](calidad/marco_ref_modelo.md#enfocs-de-qualitat)
    2. [Qualitat del producte i cicle de vida](calidad/marco_ref_modelo.md#qualitat-del-producte-i-cicle-de-vida)
    3. [Elements a ser avaluats](calidad/marco_ref_modelo.md#elements-a-ser-evaluats)
    4. [Us d’un model de qualitat](calidad/marco_ref_modelo.md#us-dun-model-de-qualitat)
5. [Model de qualitat per la qualitat interna i externa](calidad/modelo_interna_y_externa.md)
    1. [Funcionalitat](calidad/modelo_interna_y_externa.md#funcionalitat)
    2. [Fiabilitat](calidad/modelo_interna_y_externa.md#fiabilitat)
    3. [Usabilitat](calidad/modelo_interna_y_externa.md#usabilitat)
    4. [Eficiència](calidad/modelo_interna_y_externa.md#eficiencia)
    5. [Mantenibilitat](calidad/modelo_interna_y_externa.md#mantenibilitat)
    6. [Portabilitat](calidad/modelo_interna_y_externa.md#portabilitat)
6. [Model de qualitat per la qualitat en us](calidad/modelo_en_uso.md)
7. [Generació d'incidencies](calidad/generacion_incidencias.md)
8. [Obtenció de resultats](calidad/obtencion_resultados.md)

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
[módul "_GISCE-ERP_QS_"](calidad_individual.md), que està integrat en el
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
