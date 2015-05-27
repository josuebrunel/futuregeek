Title: Virtualenv avec une autre version de python
Slug: virtualenv-avec-une-autre-version-de-python
Date: 2014-11-19 20:12:06
Tags: virtualenv, python, 
Category: Programming
Author: Josue Kouka
Lang: fr
Summary: Comment creer un virtualenv avec un autre version de python

Il arrive des moments ou pour des raisons particulieres, l'on voudrait creer un *environment virtual python* 
utilisant une version de python differente de celle par defaut. 
De plus, generalement plus d'une version de *python* sont installés sur nos OS. Alors pour pouvoir créer un environement virtual python avec la version de python que vous voulez, voici la commande à entrer dans votre terminal:

```shell
yosuke@loking$ virtualenv -p /usr/bin/python2.6 <path/to/new/virtualenv/>
```