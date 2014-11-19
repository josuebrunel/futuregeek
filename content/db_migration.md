Title: Migration base de donnee Openerp production a developpement
Date: 2013-02-04
Tags: postgresql , openerp, linux, database
Category: Openerp
Author: Josue Kouka
Summary: Migration de Base de donnees , prod vers preprod

Salut !!!!
Etant un petit programmeur _openerp_ , il m'arrive tres souvent de vouloir travailler avec un environement 
de production. Chose assez simple a realiser , par rapport a openerp, car il suffit d'exporter la base de 
donnees de __production__ et  l'importer en __developpement__ .
Oui oui !!! je n'utilise pas d'outils GUI comme _pgAdmin_ ^_^ .

Prérequis :

*  	Connaissances basiques en administration linux/unix
*	Connaissances basiques SQL et administration PostgreSQL

Context :

*	serveur de bdd production : 192.168.1.2  # HOSTNAME = prod
*	serveur de  bdd developpement : 192.168.1.3 # HOSTNAME = preprod
*   Le nom de notre base de données est __pikachu__

###Production

Se connecter au serveur de base de données

	:::console
	ssh root@192.168.1.2

Se connecter en tant qu'utilisateur __postgres__

	:::console
	#su postgres

Exporter la base de données

	:::console
	postgres@prod:/root/backup$ pg_dump pikachu -U postgres > ./backup/db_backup

**db_backup** est le nom du fichier contenant la base de données exportée

###Developpement

	:::console
	prod:~#ssh root@192.168.1.3

Copier la base de données de production sur le serveur de développement

	:::console
	preprod:~# scp root@192.168.1.2:/root/backup/db_backup ./backups/

Stopper les services Openerp et Apache(Web, si necéssaire)

	:::console
	preprod:~#/etc/init.d/openerp stop #Arret du serveur openerp de developpement
	preprod:~#/etc/init.d/apache2 stop #Arret du serveur web de developpement

Connecter vous en tant qu'utilisqteur __postgres__ (on est sur le serveur de developpement cette fois-ci)
	
	:::console
	preprod:~#su postgres

Créer une base de données temporaire
	
	:::console
	postgres@preprod:/root$psql
	postgres=# create database pikachu_prod with owner=openerp template=template0 encoding='UTF-8' ;
	postgres=#\q


Charger le fichier de base de données recuperé en production vers la base de données de développement

	:::console
	postgres@preprod:/root/backups$ cat db_backup | psql pikachu_prod

Vous pouvez vérifier qu'on a deux bases ( pikachu , pikachu_prod) avec la commande:

	:::console
	postgres=#\l

Supprimer la base de développement et renommer la base de production avec le nom de celle de développement

	:::console
	postgres@preprod:/root/backups$ psql
	postgres=# drop database pikachu ;
	postgres=# alter DATABASE pikachu_prod RENAME TO pikcachu ;
   	

Relancez les services Openerp et Apache(Web)

	:::console
	preprod:~#/etc/init.d/openerp start #Demarrage du serveur openerp de développement
	preprod:~#/etc/init.d/apache2 start #Demarrage du serveur web de développement


Voila !!!