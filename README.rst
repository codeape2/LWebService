=====================
Eksempel, WCF-service
=====================

Implementasjon
==============

Tjeneste-laget er kodet mot et fasade-interface, ILiveLinkFacade. Tanken er
at man kan lage en variant av tjenesten som ikke bruker LiveLink i
backenden. Dette er nyttig for å teste bl.a. klient-server kommunikasjon
uten å måtte ha en kjørende LiveLink system i utviklingsmiljøet.

Det vil også være nyttig å ha det på denne måten dersom man senere går bort
fra WCF (og over på f.eks. ASP.NET MVC). Evt. nytt servicelag trenger bare
å kodes mot ILiveLinkFacade.

Klienter
========

lwebclient.py er en CPython 2.6-modul, uten andre systemkrav en Python 2.6
(2.7 fungerer sikkert også).

Kjør Visual Studio 2008-solutionen LWebService.sln, og kjør lwebclient.py
fra et kommandovindu. Da starter en testklient som gjør kall mot tjenesten.
