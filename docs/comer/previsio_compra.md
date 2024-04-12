# Introducció a l'aprovisionament d'energia

En aquesta secció introductòria s'expliquen amb detall tant les **Previsions de compra** com els **Històrics de consum**,
conceptes clau que cal tenir clars abans d'entendre el funcionament de **orakWlum**, l'eina d'aprovisionament d'energia
de l'ERP de Comercialitzadora.

## Previsions de Compra

La previsió de compra serveix per a poder comprar a mercat l'energia per la cartera de clients d'una Comercialitzadora,
intentant reduïr, dins el possible, la desviació entre l'energia comprada i l'energia demandada.

La manera més fiable de poder fer la previsió de consum a futur, és basar-se en l'històric de consum de la pròpia cartera
de clients, a través de les corbes reals que les Distribuïdores publiquen (fitxers `F1`, `P1`, `F5D`, `P5D`).

Si hi ha clients pels quals no es troba disponible un històric de consum real, es pot fer servir el perfilat de les `factures
de proveïdor` o dels `SIPS`, que habitualment seran una aproximació millor que un consum totalment fictici.

Finalment, pels clients que no disposen de `SIPS` ni de `factures de proveïdor` (és el cas de les noves altes, principalment), 
per a aquests es pot estimar en base a la mitjana de consum de cada hora de tota la cartera de clients que comparteixin 
tarifa d'accés i/o tipus de punt.

Per tal d'ajudar amb l'aprovisionament de compra, l'ERP de Comercialitzadora compta amb **orakWlum**, una eina de predicció
de consum a futur que permet generar de forma fàcil i intuitiva les previsions de consum de la cartera de clients d'una
Comercialitzadora, de manera que el responsable de la compra d'energia tingui una base sobre la que treballar a l'hora de
determinar la quantitat d'energia a comprar per a cada hora del dia d'una data a futur en particular.

**orakWlum** compta amb diversos **algoritmes de previsió**, que es troben explicats en subapartats d'aquesta secció dels 
manuals. A l'hora de generar una previsió de compra, a més de triar la data a futur per la qual es generarà, també es pot
indicar quin dels algoritmes disponibles es vol emprar.

## Històrics de consum

A més a més de poder generar previsions de consum a futur com a suport a l'hora de comprar l'energia al mercat, **orakWlum**
també permet generar històrics de consum. Aquests no apliquen cap algoritme ni càlcul, sinó que el que fan és recollir 
totes les corbes reals que han publicat les Distribuïdores a la Comercialitzadora i obtenir així la demanda real hora a hora
per a tota la cartera de clients, donada una data passada.

Aquests històrics poden generar-se per a estudiar-los comparant-los amb informes i resums de facturació o amb els propis
registres de la compra d'energia d'OMIE. D'aquesta manera, es pot valorar el marge de desviament entre les previsions de
consum que fa **orakWlum** i la demanda real dels clients, de manera que el responsable de la compra sempre podrà ajustar
manualment l'energia a comprar, incrementant-la o decrementant-la en base a la tendència que tingui **orakWlum** a l'hora
d'aproximar-se a la demanda real de la cartera de clients.

És important recordar que la integritat d'aquests històrics de consum dependrà de la diligència amb que les Distribuïdores
hagin anat publicant els corbes de consum. Per tant, fins passats uns dies, o fins i tot unes setmanes, és possible que no
es pugui obtenir la suma total de consum demandat pels clients, mitjançant aquestes corbes reals.
