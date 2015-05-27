Title: Environement Python
Slug: environement-python
Date: 2012-10-07
Tags: python, shell
Category: Programming
Author: Josue Kouka
Summary: 

Salut !! le but de ce post est d'aider ceux qui debutent avec python a creer un environement minimal 
au developpement python .

###A- Autocomplention sur le shell python

Vu que vous aurez a enormement utiliser le shell python, ce petit script permettant l'auto-completion vous sera fort utile.
Dans votre **home directory** creer un fichier .pythonenv.py avec le contenu suivant

    :::python
    import readline,rlcompleter
    print("Loading python env ....")
    readline.parse_and_bind('tab: complete')
    print("Python env loaded . Enjoy autocompletion ^_^ ")

*Note*:Vous pouvez vous servir du meme fichier pour importer differentes libraries que vous voudriez avoir au lancement de votre shell python (e.g sqlite3, peewee, tweepy, ...)

puis ajouter ces deux lignes a votre fichier .bashrc

    :::bash
    #Python Shell Environment
    export PYTHONSTARTUP=$HOME/.pythonenv.py

Relancez votre terminal et l'autocompletion sur votre shell python sera active

###B- **VirtualEnv** et **VirtualenvWrapper**

[__VirtualEnv__](http://pypi.python.org/pypi/virtualenv) est un petit outil python permettant de creer des environements isoles dans lequel vous pourrez installer des packages sans interferer avec d'autres environements virtuels ou votre environement systeme .
Son utilite se fait fortement ressentir losque l'on est amene a travailler sur des versions differentes d'un meme packages ou lorsque l'on veut tester des packages.
__VirtualEnvWrapper__ est un **wrapper** comme son nom l'indique, qui expose plusieurs fonctionalites de **virtualenv** de maniere assez simple.

####Installation

  :::console
  yosuke@loking:~/workspace$pip install virtualenvwrapper

####Utilisation

    :::console
    yosuke@loking:~/workspace$ mkvirtualenv konoha #creation de nottre environement virtuel
    New python executable in konoha/bin/python
    Installing setuptools............done.
    Installing pip...............done.
    virtualenvwrapper.user_scripts creating /home/yosuke/.virtualenvs/konoha/bin/predeactivate
    virtualenvwrapper.user_scripts creating /home/yosuke/.virtualenvs/konoha/bin/postdeactivate
    virtualenvwrapper.user_scripts creating /home/yosuke/.virtualenvs/konoha/bin/preactivate
    virtualenvwrapper.user_scripts creating /home/yosuke/.virtualenvs/konoha/bin/postactivate
    virtualenvwrapper.user_scripts creating /home/yosuke/.virtualenvs/konoha/bin/get_env_details
    (konoha)yosuke@loking:~/workspace$ pip install peewee #installation d'un package dans l'environement virtuel
    Downloading/unpacking peewee
    Downloading peewee-2.0.7.tar.gz (662kB): 662kB downloaded
    Running setup.py egg_info for package peewee
      
    Installing collected packages: peewee
    Running setup.py install for peewee
    changing mode of build/scripts-2.7/pwiz.py from 664 to 775
      
    changing mode of /home/yosuke/.virtualenvs/konoha/bin/pwiz.py to 775
    Successfully installed peewee
    Cleaning up...
    (konoha)yosuke@loking:~/workspace$ deactivate #sortie de l'environement virtuel
    yosuke@loking:~/workspace$ 

Voila !!! Vous etes prets (enfin je pense)
 