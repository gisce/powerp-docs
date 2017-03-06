# Validacions

## Validacions al lot

Cada validació té un codi associat que permet la cerca de diferents pòlisses amb el mateix problema.

Les validacions que apareixen a continuació es realitzen en els lots de facturació abans de crear les factures. Les següents validacions es realitzen tant a les empreses comercialitzadores com en les distribuidores.

- [V001] Hi ha hagut una volta de comptador
- [V002] Comprovació de que existeixin lectures anteriors respecte les que haurem de comparar
- [V003] Comprovació de que hi ha lectures per a cada periode de la tarifa
- [V004] Control dels canvis de contador
- [V005] Comprovació de que la pòlissa tingui un comptador actiu en les dates de facturació
- [V006] Validació de que el consum no sigui negatiu
- [V007] Validació de que existeixin intervals pels quals facturar
- [V008] Validació de que el consum no sigui inferior a un cert limit
- [V009] Validació de que la lectura del maxímetre no sigui superior en més d'un percentatge a la potència contractada, per periode
- [V010] Validació de que el consum no sigui superior a un cert limit, que depén de la tarifa
- [V011] Validació de que les lectures de reactiva no siguin superiors a un percentatge de l'activa, per periode
- [V012] Analisi de quins periodes falten per les dates de facturació
- [V013] Les lectures anteriors i actuals són iguals
- [V014] Falta la lectura de tancament per un comptador de baixa dins del periode de facturació

Les següents validacions només es realitzen en les empreses comercialitzadores:

- [V015] Hi ha algun problema amb el mandato

Les següents validacions només es realitzen en les empreses distribuidores:

- [V016] Comprovació si un comptador està al TPL

## Validacions en la creació de factures

Les següents validacions es realitzen quan creem una factura després de passar o saltar-nos les validacions de lot.

- [F001] El consum (kWh) del mes és superior en un percentatge al màxim dels últims n mesos
- [F002] La potencia (kW) del mes és superior en un marge absolut al màxim dels últims n mesos
- [F003] El consum (kWh) del mes és superior en un marge absolut al màxim dels últims n mesos
- [F004] L'import d'energía facturat (€) és inferior o igual a un valor mínim
- [F005] L'import de potència facturat (€) és inferior o igual a un valor mínim
- [F006] L'import total facturat (€) és inferior o igual a un valor mínim
- [F007] L'import total és superior a un valor màxim, que depèn de la tarifa
- [F008] El consum (kWh) del mes no esta dins d'un marge. Aquests marge ve definit a partir d'un percentatge de la mitjana de consum dels ultims n mesos. També hi ha un valor absolut que defineix el marge mínim.
