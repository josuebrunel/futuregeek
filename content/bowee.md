Title: Bowee
Date: 2013-01-15
Author: Josue Kouka
Tags: python, bottle, peewee, web
Category: Projects 
Summary: Little Bottle project builder

##What's __BoWee__

**BoWee** is a **bottle** project builder. It generates an project architecture and useful files for **bottle** projects.
It was previously name _TinyCocktail_ , but it has been changed. 

It uses the [MVC](http://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller) architecture. 
Actually is more ***Model View Template*** architecture like in the [Django Framework](http://en.wikipedia.org/wiki/Django_(web_framework)).

It's currently in development but it's quite usable, i advise you to use a ___virtual environment___ though. 

**BoWee** uses **peewee** as ORM and obviously **bottle** as Web Framework. 

##Requirements
To be able to use *BoWee*, it's required to :

* Know and have installed Peewee

* Know and have installed Bottle

Those packages can be installed like this:

    :::console
    yosuke@loking:~$sudo pip install bottle peewee

##Download

You can directly download **bowee** [here](./static_files/bowee/bowee-1.1.tar.gz) or check the [github repository](https://github.com/josuebrunel/bowee) to see the last updates.


##Installation

####Via the tar.gz

    :::console
    (bottle)yosuke@loking:~$ tar xvzf bowee-1.1.tar.gz 
    bowee-1.1/
    bowee-1.1/bowee/
    bowee-1.1/bowee/bowee.py
    bowee-1.1/bowee/__init__.py
    bowee-1.1/bowee_admin.py
    bowee-1.1/PKG-INFO
    bowee-1.1/setup.py
    (bottle)yosuke@loking:~$ cd bowee-1.1/
    (bottle)yosuke@loking:~/bowee-1.1$ ls
    bowee  bowee_admin.py  PKG-INFO  setup.py
    (bottle)yosuke@loking:~/bowee-1.1$ python setup.py install
    running install
    running build
    running build_py
    creating build
    creating build/lib.linux-i686-2.7
    creating build/lib.linux-i686-2.7/bowee
    copying bowee/__init__.py -> build/lib.linux-i686-2.7/bowee
    copying bowee/bowee.py -> build/lib.linux-i686-2.7/bowee
    running build_scripts
    creating build/scripts-2.7
    copying and adjusting bowee_admin.py -> build/scripts-2.7
    changing mode of build/scripts-2.7/bowee_admin.py from 664 to 775
    running install_lib
    running install_scripts
    copying build/scripts-2.7/bowee_admin.py -> /home/yosuke/.virtualenvs/bottle/bin
    changing mode of /home/yosuke/.virtualenvs/bottle/bin/bowee_admin.py to 775
    running install_egg_info
    Removing /home/yosuke/.virtualenvs/bottle/lib/python2.7/site-packages/bowee-1.1-py2.7.egg-info
    Writing /home/yosuke/.virtualenvs/bottle/lib/python2.7/site-packages/bowee-1.1-py2.7.egg-info
    (bottle)yosuke@loking:~/bowee-1.1$ 


####Via pip
    :::console

    yosuke@loking:~$sudo pip install bowee

##Turorial

    :::console

    yosuke@loking:~$bowee_admin project test
    yosuke@loking:~$tree test
    test/
    ├── __init__.py
    ├── models.py
    ├── static_files
    ├── templates
    └── views.py

    2 directories, 3 files

***models.py***:   

    :::python
    import peewee
    #import db_driver
    
    #Example with Sqlite database
    #database = peewee.SqliteDatabase('sample.db',check_same_thread=False)
    
    def create_tables():
        '''code such as : ModelName.create_table()'''
    
    class BaseModel(peewee.Model):
        class Meta:
            database = database

    if __name__ == '__main__'
        create_tables()

***views.py***:

    :::python
    from bottle import run , debug , route
    from bottle import request , response , redirect , template
    import models
    import peewee

    #create your views

    @route('/')
    @route('/index')
    def index():
        return "Hello World !!!"

***templates***: Contains all template files (.tpl, .html.tpl)

***static_files***: Contains all the static files

Now that everything is setup, i wish you a __Happy Coding__
